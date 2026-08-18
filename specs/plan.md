# Plano de implementação

## 1. Estado atual verificado

`presentation.html` é um documento único com CSS e JavaScript embutidos. Ele contém exatamente 19 elementos `.slide`, navegação por botões, teclado e swipe, barra de progresso, contador, tela cheia via `Esc`, animações de entrada, partículas, ícones SVG locais e cursor personalizado.

O estado atual é mantido apenas por `currentSlide`. As funções `updateSlide`, `nextSlide`, `prevSlide` e `goToSlide` alteram o slide ativo. Os eventos globais não distinguem apresentação, campos editáveis ou camadas modais.

Ainda não existem tela inicial, Universo, quiz, timer, pontuação, som, modo apresentador, notas, ajuda, preferências ou foco modal. `implementation.md` e `validation.md` contêm afirmações anteriores que não correspondem ao HTML e serão substituídas por evidências reais.

O HTML também referencia Google Fonts e um script externo injetado. Ambos contrariam o funcionamento offline estrito e serão removidos, mantendo fallbacks tipográficos locais.

## 2. Estratégia de preservação

1. Criar `backup/presentation-original.html` antes de alterar o arquivo principal.
2. Preservar a ordem, o texto e a estrutura dos 19 blocos `.slide`.
3. Acrescentar componentes como camadas independentes e integrar a navegação existente.
4. Manter os nomes públicos das funções de navegação para os controles inline existentes.
5. Comparar o conteúdo normalizado dos slides com o backup ao final.
6. Não usar bibliotecas, APIs remotas, CDNs ou arquivos de áudio.

## 3. Arquitetura proposta

- `AppState`: estado principal, slide, preferências, visitados e camada ativa.
- `StorageManager`: leitura, validação e gravação tolerantes a falhas.
- `TimerController`: timer geral, timer por slide e timer único do quiz.
- `AudioManager`: uma instância de Web Audio API e sequências não concorrentes.
- `ModalController`: abertura, fechamento, pilha de camadas, foco inicial, focus trap e restauração de foco.
- `NavigationController`: navegação, transições direcionais, progresso e persistência.
- `UniverseController`: geração dos 19 cards, estados, flutuação e parallax limitado.
- `QuizController`: três perguntas oficiais, resolução exclusiva, pontuação e resultado.
- `PresenterController`: painel, tempos, próximo slide e notas por slide.
- `AccessibilityController`: atalhos contextuais, anúncios, movimento reduzido e visibilidade da página.

## 4. Ordem de implementação

1. Backup e fundação de estado/armazenamento/timers.
2. Tela inicial e fluxo de entrada.
3. Universo gerado dos slides.
4. Navegação e transições integradas.
5. Quiz, timer, pontuação e resultado.
6. Sons e preferência persistida.
7. Painel do apresentador, cronômetros e notas.
8. Ajuda, limpeza de dados e controle de movimento.
9. Acessibilidade, responsividade, visibilidade e desempenho.
10. Testes, correções, validação e relatório final.

## 5. Dependências internas

- Universo depende da descoberta dos slides e seus títulos.
- Persistência depende de validação dos índices e valores armazenados.
- Quiz depende do timer central e o áudio depende de uma interação do usuário.
- Modais, atalhos e swipe dependem do estado principal para evitar conflitos.
- Painel e notas dependem da navegação e do armazenamento.

## 6. Riscos e mitigações

- **Alteração acidental dos slides:** backup e comparação estrutural/textual automatizada.
- **Atalhos conflitantes:** um único roteador que ignora campos editáveis e respeita a camada superior.
- **Timers duplicados:** identificadores privados e cancelamento antes de iniciar/reiniciar.
- **Resposta e timeout simultâneos:** flag de resolução definida antes de cancelar o timer.
- **Áudio bloqueado/indisponível:** inicialização após interação, `try/catch` e feedback visual equivalente.
- **Falha de armazenamento:** wrapper tolerante a exceções com defaults válidos.
- **Animações pesadas:** suspensão fora da apresentação, limites de partículas/parallax e movimento reduzido.
- **Zoom/telas pequenas:** camadas roláveis, grids adaptativos e controles de no mínimo 44 px.
- **Offline:** remover requisições externas e sintetizar sons localmente.

## 7. Estratégia de testes

- Testes estáticos: 19 slides, ausência de URLs externas, quatro opções por pergunta, conteúdo do quiz e atributos ARIA.
- Testes funcionais em navegador: início/continuar/Universo, navegação, atalhos, foco, quiz correto/incorreto/timeout/último segundo/reinício, áudio on/off, visibilidade e persistência.
- Testes de robustez: `localStorage` e Web Audio indisponíveis, timers únicos e funcionamento por `file://`.
- Testes responsivos: desktop 16:9, tablet, celular e zoom de 200%.
- Testes de preservação: comparar quantidade e texto normalizado dos 19 slides com o backup.

## 8. Rollback

Se uma regressão crítica não puder ser corrigida, restaurar `presentation.html` a partir de `backup/presentation-original.html`. O backup não será modificado durante a implementação.
