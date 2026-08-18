# Registro da implementação

## Resumo

A experiência foi implementada como uma camada modular dentro de `presentation.html`, sem alterar os blocos dos 19 slides. O conteúdo de cada slide foi comparado byte a byte com `backup/presentation-original.html`.

O registro anterior dizia que a tela inicial estava concluída, mas ela não existia no HTML analisado. Esse estado inconsistente foi substituído pelo registro real abaixo.

## Arquivos modificados

- `presentation.html`
- `specs/plan.md`
- `specs/tasks.md`
- `specs/test-plan.md`
- `specs/validation.md`
- `specs/final-report.md`

## Arquivos criados

- `backup/presentation-original.html`
- `tests/validate-static.js`
- `tests/runtime-cdp.py`
- Capturas de evidência visual em `tests/*.png`

## Componentes implementados

- `AppState`: modo principal, camada ativa, preferências, visitados e notas.
- `StorageManager`: leitura, escrita e limpeza protegidas por `try/catch`.
- `TimerController`: um único intervalo para o quiz e controle central de pausa/cancelamento.
- `AudioManager`: contexto Web Audio único, envelopes, sequências distintas e cancelamento.
- `ModalController`: camada única, focus trap, foco inicial e restauração de foco.
- `NavigationController`: navegação preservada, transições direcionais, progresso e persistência.
- `UniverseController`: 19 cards gerados dos slides, categorias, visitados, atual e parallax limitado.
- `QuizController`: três perguntas oficiais, timeout exclusivo, pontuação, resultado e retomada.
- `PresenterController`: painel, cronômetros, próximo slide e notas por slide.
- Roteador central de teclado, tratamento de toque e `visibilitychange`.

## Funcionalidades

- Tela inicial com iniciar, continuar condicionado ao progresso e explorar.
- Universo responsivo com cinco, três ou duas colunas conforme viewport.
- Transições de 480 ms e sequenciamento original por `.animate-in`.
- Quiz de três perguntas, 60 segundos, estados verde/laranja/vermelho, pulso final e avanço manual.
- Fórmula `100 + segundos restantes`, máximo 480 e média de tempo.
- Sons de abertura, navegação, acerto, erro, contagem, timeout e resultado.
- Modo apresentador, notas persistentes, cronômetros e controles.
- Ajuda, atalhos, tela cheia, limpeza de dados e movimento reduzido manual/persistente.
- ARIA, anúncios pontuais, foco visível, focus trap e alvos mínimos de 44 px.
- Pausa automática na aba oculta; quiz exige retomada manual.
- Redução automática de efeitos em hardware indicado como limitado.
- Confetes limitados a 24 elementos, removidos após animação e desativados com movimento reduzido.
- Operação offline: removidas Google Fonts e a referência externa injetada; usados fallbacks locais.

## Decisões e conflitos

- O requisito offline teve prioridade sobre as referências externas existentes. A tipografia mantém a pilha local definida no CSS.
- A função pública dos controles inline foi preservada por wrappers globais de `nextSlide`, `prevSlide` e `goToSlide`.
- O `Esc` fecha primeiro a camada superior e, sem camada, alterna tela cheia.
- Fechar um quiz em andamento pausa a tentativa; reabrir oferece continuar ou reiniciar, evitando timers paralelos.
- O texto e a ordem dos slides não foram normalizados nem corrigidos, mesmo quando isso seria visualmente tentador, para cumprir a preservação integral.

## Problemas encontrados e soluções

- Registros prévios divergiam do código: revalidados e substituídos por evidência executada.
- O primeiro executor Playwright não inicializou no ambiente: foi criada uma suíte via Chrome DevTools Protocol usando o Edge headless local.
- Um teste de `Esc` inicialmente sintetizava o evento no alvo errado: o teste foi corrigido para disparar no elemento focado e passou.
- A simulação de falha de armazenamento coincidiu com a trava de transição: o caso foi isolado e retestado, comprovando a tolerância.
- A retomada do quiz podia agendar uma partida redundante em uma janela curta; `renderQuestion` passou a receber o tempo restante e criar apenas um timer.

## Pendências

Não há requisito funcional crítico pendente. Testes manuais com leitor de tela real e execução automatizada no Firefox permanecem recomendações de compatibilidade, não falhas conhecidas.
