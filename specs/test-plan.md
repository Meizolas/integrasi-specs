# Plano de testes

## Execução

- Estático: `node tests/validate-static.js`
- Funcional: `python tests/runtime-cdp.py`
- Visual: capturas da home, Universo e quiz em `tests/*.png`

## Casos

| ID | Caso | Resultado esperado |
|---|---|---|
| T01 | Preservação | 19 slides e blocos idênticos ao backup |
| T02 | Sintaxe/offline | Scripts compilam e não há URL externa |
| T03 | Tela inicial | Iniciar abre slide 1; continuar depende de progresso |
| T04 | Navegação | Botões, setas, espaço, Page Up/Down, Home/End e contador |
| T05 | Toque | Swipe horizontal navega uma vez e não atua no quiz |
| T06 | Tela cheia | Controle entra e sai com gesto do usuário |
| T07 | Universo | 19 cards, nomes acessíveis, atual/visitado e abertura individual |
| T08 | Quiz correto | Bloqueia opções, cancela timer e soma 100 + segundos |
| T09 | Quiz incorreto | Bloqueia opções e soma zero |
| T10 | Timeout | Bloqueia, revela correta, explica e mantém avanço manual |
| T11 | Último segundo | Resolve uma vez e soma 101, sem timeout concorrente |
| T12 | Reinício | Limpa índice, respostas, pontos, tempos e mantém timer único |
| T13 | Resultado | Exibe acertos, pontuação, média, mensagem e persiste |
| T14 | Visibilidade | Aba oculta pausa; retorno exige retomada manual do quiz |
| T15 | Áudio | On/off persiste; falha da API não bloqueia a aplicação |
| T16 | Armazenamento | Falha simulada não bloqueia navegação |
| T17 | Apresentador/notas | Dados corretos, timers controláveis e notas por slide |
| T18 | Teclado/foco | Foco entra no modal, fica contido, Esc fecha e retorna |
| T19 | Movimento | Preferência elimina efeitos contínuos |
| T20 | Responsividade | Desktop, tablet em três colunas e celular em duas |
| T21 | Zoom/alvos | Em escala 200%, controles visíveis mantêm 44 px |
| T22 | Persistência | Recarregar exibe Continuar e retorna ao último slide |
| T23 | Limpeza | Remove apenas chaves `devIa.*` após confirmação |

## Casos extremos

- Resposta no instante final.
- Fechar e reabrir tentativa em andamento.
- Reiniciar com timer ativo.
- Pressionar espaço com botão focado.
- Trocar de aba com quiz ativo.
- Web Audio ausente.
- `localStorage.setItem` lançando exceção.
- Viewport curta e dispositivo móvel.
