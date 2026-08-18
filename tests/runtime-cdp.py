import json
import base64
import subprocess
import time
import urllib.request
import websocket

EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
URL = "file:///D:/TRABALHO/INTEGRASI/presentation.html"
PORT = 9333
PROFILE = r"D:\TRABALHO\INTEGRASI\.edge-cdp-profile"


class CDP:
    def __init__(self, ws_url):
        self.ws = websocket.create_connection(ws_url, timeout=15)
        self.counter = 0

    def call(self, method, params=None):
        self.counter += 1
        message_id = self.counter
        self.ws.send(json.dumps({"id": message_id, "method": method, "params": params or {}}))
        while True:
            message = json.loads(self.ws.recv())
            if message.get("id") == message_id:
                if "error" in message:
                    raise RuntimeError(message["error"])
                return message.get("result", {})

    def evaluate(self, expression):
        result = self.call("Runtime.evaluate", {
            "expression": expression,
            "returnByValue": True,
            "awaitPromise": True,
        })
        if "exceptionDetails" in result:
            raise RuntimeError(result["exceptionDetails"].get("text", "JavaScript exception"))
        return result.get("result", {}).get("value")

    def close(self):
        self.ws.close()


def wait_for_debugger():
    deadline = time.time() + 15
    while time.time() < deadline:
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json", timeout=1) as response:
                pages = json.load(response)
                pages.sort(key=lambda page: URL not in page.get("url", ""))
                for page in pages:
                    if page.get("type") == "page":
                        return page["webSocketDebuggerUrl"]
        except Exception:
            time.sleep(0.2)
    raise RuntimeError("Edge DevTools endpoint did not become available")


def main():
    flags = 0x08000000 if hasattr(subprocess, "CREATE_NO_WINDOW") else 0
    process = subprocess.Popen([
        EDGE, "--headless=new", "--disable-gpu", "--no-first-run",
        "--no-default-browser-check", "--disable-extensions",
        "--window-size=1440,900",
        "--remote-allow-origins=*", f"--remote-debugging-port={PORT}",
        f"--user-data-dir={PROFILE}", URL,
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags=flags)
    cdp = None
    results = []

    def check(identifier, condition, evidence):
        results.append((identifier, bool(condition), evidence))

    try:
        cdp = CDP(wait_for_debugger())
        cdp.call("Runtime.enable")
        cdp.call("Page.enable")
        cdp.call("Page.navigate", {"url": URL})
        time.sleep(1)
        cdp.evaluate("localStorage.clear(); location.reload()")
        time.sleep(1)
        check("R01-BOOT", cdp.evaluate("document.querySelectorAll('.slide').length") == 19 and cdp.evaluate("!homeLayer.hidden"), "Home visível e 19 slides carregados")
        check("R02-API", cdp.evaluate("!!window.DEVIA && DEVIA.quizQuestions.length === 3"), "Controladores disponíveis sem erro de inicialização")

        cdp.evaluate("startBtn.click()")
        time.sleep(0.15)
        check("R03-START", cdp.evaluate("document.body.dataset.mode === 'presentation' && currentSlide === 0 && homeLayer.hidden"), "Iniciar abre o slide 1")
        fullscreen_rect = cdp.evaluate("(()=>{const r=fullscreenBtn.getBoundingClientRect(); return {x:r.x+r.width/2,y:r.y+r.height/2}})()")
        cdp.call("Input.dispatchMouseEvent", {"type": "mousePressed", "x": fullscreen_rect["x"], "y": fullscreen_rect["y"], "button": "left", "clickCount": 1})
        cdp.call("Input.dispatchMouseEvent", {"type": "mouseReleased", "x": fullscreen_rect["x"], "y": fullscreen_rect["y"], "button": "left", "clickCount": 1})
        time.sleep(0.2)
        check("R03B-FULLSCREEN", cdp.evaluate("!!document.fullscreenElement"), "Controle entra em tela cheia com gesto do usuário")
        cdp.evaluate("document.exitFullscreen()")

        cdp.evaluate("nextSlide()")
        time.sleep(0.65)
        check("R04-NAV", cdp.evaluate("currentSlide === 1 && current.textContent === '2'"), "Botão/função avança, contador acompanha")

        cdp.evaluate("universeBtn.click()")
        time.sleep(0.1)
        check("R05-UNIVERSE", cdp.evaluate("!universeLayer.hidden && universeGrid.children.length === 19"), "Universo abre com 19 cards")
        with open(r"D:\TRABALHO\INTEGRASI\tests\universe-desktop.png", "wb") as screenshot:
            screenshot.write(base64.b64decode(cdp.call("Page.captureScreenshot", {"format": "png"})["data"]))
        check("R06-UNIVERSE-A11Y", cdp.evaluate("[...universeGrid.children].every((c,i)=>c.getAttribute('aria-label').startsWith('Abrir slide '+(i+1)))"), "Todos os cards têm nome acessível")
        cdp.evaluate("universeGrid.children[9].click()")
        time.sleep(0.15)
        check("R07-UNIVERSE-OPEN", cdp.evaluate("currentSlide === 9 && document.body.dataset.mode === 'presentation'"), "Card abre o slide solicitado")

        cdp.evaluate("quizBtn.click()")
        time.sleep(0.65)
        check("R08-QUIZ", cdp.evaluate("!quizLayer.hidden && document.querySelectorAll('.quiz-option').length === 4 && DEVIA.TimerController.quizId !== 0"), "Quiz abre com quatro opções e timer único")
        with open(r"D:\TRABALHO\INTEGRASI\tests\quiz-desktop.png", "wb") as screenshot:
            screenshot.write(base64.b64decode(cdp.call("Page.captureScreenshot", {"format": "png"})["data"]))
        cdp.evaluate("document.querySelectorAll('.quiz-option')[2].click()")
        time.sleep(0.1)
        correct_score = cdp.evaluate("DEVIA.QuizController.score")
        check("R09-CORRECT", 100 <= correct_score <= 160 and cdp.evaluate("DEVIA.TimerController.quizId === 0 && document.querySelectorAll('.quiz-option:disabled').length === 4"), f"Acerto bloqueia opções e soma {correct_score} pontos")

        cdp.evaluate("nextQuestionBtn.click()")
        time.sleep(0.65)
        cdp.evaluate("document.querySelectorAll('.quiz-option')[0].click()")
        time.sleep(0.1)
        check("R10-WRONG", cdp.evaluate(f"DEVIA.QuizController.score === {correct_score} && document.querySelector('.quiz-option.wrong') !== null"), "Erro vale zero e recebe estado textual/visual")

        cdp.evaluate("nextQuestionBtn.click()")
        time.sleep(0.65)
        cdp.evaluate("DEVIA.QuizController.timeout()")
        time.sleep(0.1)
        check("R11-TIMEOUT", cdp.evaluate("DEVIA.TimerController.quizId === 0 && document.querySelector('.quiz-option.correct') !== null && document.querySelectorAll('.quiz-option:disabled').length === 4"), "Timeout cancela timer, bloqueia e revela resposta")

        cdp.evaluate("nextQuestionBtn.click()")
        time.sleep(0.1)
        check("R12-RESULT", cdp.evaluate("document.querySelector('.result-score') !== null && !!localStorage.getItem('devIa.lastQuizResult')"), "Resultado final exibido e persistido")
        cdp.evaluate("restartQuizBtn.click()")
        time.sleep(0.65)
        check("R13-RESTART", cdp.evaluate("DEVIA.QuizController.index === 0 && DEVIA.QuizController.score === 0 && DEVIA.QuizController.answers.length === 0 && DEVIA.TimerController.quizId !== 0"), "Reinício limpa estado e mantém um timer")

        cdp.evaluate("DEVIA.TimerController.quizRemaining=1; document.querySelectorAll('.quiz-option')[2].click()")
        time.sleep(0.1)
        check("R13B-LAST-SECOND", cdp.evaluate("DEVIA.QuizController.score === 101 && DEVIA.QuizController.answers.length === 1 && DEVIA.TimerController.quizId === 0"), "Resposta no último segundo resolve uma vez e soma 101")

        cdp.evaluate("DEVIA.QuizController.reset(false)")
        time.sleep(0.65)
        cdp.evaluate("Object.defineProperty(document,'hidden',{value:true,configurable:true}); document.dispatchEvent(new Event('visibilitychange'))")
        check("R13C-HIDDEN", cdp.evaluate("DEVIA.QuizController.paused && DEVIA.TimerController.quizId === 0"), "Troca de aba pausa o quiz")
        cdp.evaluate("Object.defineProperty(document,'hidden',{value:false,configurable:true}); document.dispatchEvent(new Event('visibilitychange'))")
        time.sleep(0.1)
        check("R13D-NO-AUTO-RESUME", cdp.evaluate("DEVIA.QuizController.paused && !!document.getElementById('resumeQuizBtn')"), "Retorno à aba exige retomada manual")
        cdp.evaluate("resumeQuizBtn.click()")
        time.sleep(0.65)
        check("R13E-RESUME", cdp.evaluate("!DEVIA.QuizController.paused && DEVIA.TimerController.quizId !== 0"), "Retomada cria somente o timer ativo")

        previous_sound = cdp.evaluate("DEVIA.AppState.soundEnabled")
        cdp.evaluate("soundBtn.click()")
        check("R14-SOUND", cdp.evaluate(f"DEVIA.AppState.soundEnabled === {str(not previous_sound).lower()} && localStorage.getItem('devIa.soundEnabled') !== null"), "Som alterna e persiste")

        cdp.evaluate("document.querySelector('[data-close-layer]').click()")
        time.sleep(0.1)
        cdp.evaluate("helpBtn.click()")
        time.sleep(0.1)
        check("R15-FOCUS", cdp.evaluate("helpLayer.contains(document.activeElement)"), "Foco entra no modal")
        cdp.evaluate("document.activeElement.dispatchEvent(new KeyboardEvent('keydown',{key:'Escape',code:'Escape',bubbles:true,cancelable:true}))")
        time.sleep(0.1)
        check("R16-ESC", cdp.evaluate("helpLayer.hidden && document.body.dataset.mode === 'presentation'"), "Esc fecha a camada superior")

        before_space = cdp.evaluate("currentSlide")
        cdp.evaluate("universeBtn.focus(); universeBtn.dispatchEvent(new KeyboardEvent('keydown',{key:' ',code:'Space',bubbles:true,cancelable:true}))")
        time.sleep(0.1)
        check("R16B-SPACE", cdp.evaluate(f"currentSlide === {before_space}"), "Espaço em botão focado não navega slides")

        cdp.evaluate("document.querySelector('.slide.active .slide-content').focus(); document.activeElement.dispatchEvent(new KeyboardEvent('keydown',{key:'n',bubbles:true,cancelable:true}))")
        time.sleep(0.1)
        cdp.evaluate("modalNotes.value='Nota automatizada'; modalNotes.dispatchEvent(new Event('input',{bubbles:true}))")
        check("R16C-NOTES", cdp.evaluate("JSON.parse(localStorage.getItem('devIa.presenterNotes'))[String(currentSlide)] === 'Nota automatizada'"), "Notas por slide persistidas")
        cdp.evaluate("DEVIA.ModalController.close(false); presenterToggle.click()")
        check("R16D-PRESENTER", cdp.evaluate("!presenterPanel.hidden && presenterCurrent.textContent.includes(String(currentSlide+1).padStart(2,'0'))"), "Painel mostra slide, próximo e cronômetros")
        cdp.evaluate("presenterToggle.click()")

        start_touch = cdp.evaluate("currentSlide")
        cdp.evaluate("let a=new Event('touchstart',{bubbles:true}); Object.defineProperty(a,'changedTouches',{value:[{screenX:300,screenY:200}]}); document.dispatchEvent(a); let b=new Event('touchend',{bubbles:true}); Object.defineProperty(b,'changedTouches',{value:[{screenX:120,screenY:205}]}); document.dispatchEvent(b)")
        time.sleep(0.65)
        check("R16E-TOUCH", cdp.evaluate(f"currentSlide === Math.min({start_touch}+1,18)"), "Swipe horizontal avança um slide")

        cdp.evaluate("let p=Storage.prototype.setItem; window.__setItem=p; Storage.prototype.setItem=function(){throw new Error('blocked')}; window.__storageResult=DEVIA.StorageManager.set('probe',1); DEVIA.AppState.transitionLocked=false; DEVIA.NavigationController.go(3,1,true)")
        time.sleep(0.1)
        check("R16F-STORAGE-FAIL", cdp.evaluate("window.__storageResult === false && currentSlide === 3"), "Falha de armazenamento não impede navegação")
        cdp.evaluate("Storage.prototype.setItem=window.__setItem")

        cdp.evaluate("window.__AudioContext=window.AudioContext; window.__webkitAudioContext=window.webkitAudioContext; window.AudioContext=undefined; window.webkitAudioContext=undefined; DEVIA.AudioManager.context=null; DEVIA.AppState.soundEnabled=true; DEVIA.AudioManager.play('correct'); DEVIA.NavigationController.go(4,1,true)")
        time.sleep(0.1)
        check("R16G-AUDIO-FAIL", cdp.evaluate("currentSlide === 4"), "Web Audio indisponível não impede navegação")
        cdp.evaluate("window.AudioContext=window.__AudioContext; window.webkitAudioContext=window.__webkitAudioContext")

        cdp.call("Emulation.setDeviceMetricsOverride", {"width": 390, "height": 844, "deviceScaleFactor": 1, "mobile": True})
        time.sleep(0.2)
        cdp.evaluate("universeBtn.click()")
        columns = cdp.evaluate("getComputedStyle(universeGrid).gridTemplateColumns.split(' ').length")
        check("R17-MOBILE", columns == 2 and cdp.evaluate("getComputedStyle(document.querySelector('.cursor-dot')).display === 'none'"), "Layout móvel usa duas colunas e remove cursor customizado")

        cdp.call("Emulation.setDeviceMetricsOverride", {"width": 900, "height": 700, "deviceScaleFactor": 1, "mobile": False})
        time.sleep(0.2)
        tablet_columns = cdp.evaluate("getComputedStyle(universeGrid).gridTemplateColumns.split(' ').length")
        check("R17A-TABLET", tablet_columns == 3, "Layout tablet usa três colunas")

        cdp.call("Emulation.setDeviceMetricsOverride", {"width": 640, "height": 360, "deviceScaleFactor": 2, "mobile": False})
        time.sleep(0.2)
        check("R17B-ZOOM", cdp.evaluate("[...document.querySelectorAll('button')].filter(b=>b.offsetParent!==null).every(b=>b.getBoundingClientRect().height>=44)"), "Controles visíveis mantêm alvo mínimo de 44px em escala 200%")

        cdp.evaluate("DEVIA.ModalController.close(false); DEVIA.AppState.reducedMotion=true; document.body.classList.add('reduced-motion')")
        check("R18-MOTION", cdp.evaluate("getComputedStyle(document.querySelector('.universe-card')).animationName === 'none' || document.body.classList.contains('reduced-motion')"), "Preferência de movimento reduzido aplicada")
        check("R19-STORAGE", cdp.evaluate("localStorage.getItem('devIa.lastSlide') !== null && localStorage.getItem('devIa.visitedSlides') !== null"), "Slide e visitados persistidos")

        cdp.evaluate("DEVIA.AppState.reducedMotion=false; document.body.classList.remove('reduced-motion'); DEVIA.NavigationController.go(6,1,true)")
        time.sleep(0.1)
        cdp.call("Page.reload", {"ignoreCache": True})
        time.sleep(1)
        check("R20-CONTINUE", cdp.evaluate("!continueBtn.hidden"), "Progresso recarregado exibe Continuar")
        cdp.evaluate("continueBtn.click()")
        time.sleep(0.15)
        check("R21-CONTINUE-SLIDE", cdp.evaluate("currentSlide === 6 && document.body.dataset.mode === 'presentation'"), "Continuar retorna ao último slide")

        cdp.evaluate("DEVIA.TimerController.cancelQuiz(); DEVIA.PresenterController.pause(); DEVIA.AudioManager.stop()")
    finally:
        if cdp:
            cdp.close()
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()

    for identifier, passed, evidence in results:
        print(f"{'PASS' if passed else 'FAIL'} {identifier}: {evidence}")
    if any(not passed for _, passed, _ in results):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
