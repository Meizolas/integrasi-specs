# DEV + IA Interactive Experience - Tarefas

## Fase 0 - SeguranÃ§a e anÃ¡lise

- [x] Criar cÃ³pia de seguranÃ§a do `presentation.html`.
- [x] Ler integralmente `presentation.html` e os arquivos de `specs/`.
- [x] Mapear funÃ§Ãµes, seletores, atalhos e estilos existentes.
- [x] Confirmar a quantidade de 19 slides.
- [x] Registrar tÃ­tulos e categorias dos slides.
- [x] Definir uma estratÃ©gia de implementaÃ§Ã£o que preserve o arquivo original.

## Fase 1 - FundaÃ§Ã£o

- [x] Criar controlador de estados da aplicaÃ§Ã£o.
- [x] Centralizar abertura e fechamento de camadas.
- [x] Criar funÃ§Ãµes seguras para leitura e escrita no `localStorage`.
- [x] Criar gerenciador central de cronÃ´metros.
- [x] Evitar duplicaÃ§Ã£o de event listeners.
- [x] Implementar tratamento de `visibilitychange`.

## Fase 2 - Tela inicial

- [x] Criar estrutura HTML da tela inicial.
- [x] Criar estilos responsivos.
- [x] Implementar animaÃ§Ã£o de entrada.
- [x] Implementar `Iniciar apresentaÃ§Ã£o`.
- [x] Implementar `Continuar` condicionado ao progresso.
- [x] Implementar `Explorar slides`.
- [x] Garantir navegaÃ§Ã£o por teclado.

## Fase 3 - Universo de Slides

- [x] Gerar cards automaticamente a partir dos slides existentes.
- [x] Associar nÃºmero, tÃ­tulo, categoria e Ã­cone.
- [x] Implementar layout espacial para desktop.
- [x] Implementar grade responsiva para tablet e celular.
- [x] Implementar flutuaÃ§Ã£o com variaÃ§Ãµes controladas.
- [x] Implementar parallax limitado com `requestAnimationFrame`.
- [x] Implementar estados atual e visualizado.
- [x] Implementar abertura animada de um slide.
- [x] Implementar atalho `M`.
- [x] Implementar retorno ao Universo.
- [x] Desativar efeitos contÃ­nuos em movimento reduzido.

## Fase 4 - TransiÃ§Ãµes da apresentaÃ§Ã£o

- [x] Preservar `updateSlide`, `nextSlide`, `prevSlide` e `goToSlide` ou equivalentes.
- [x] Adicionar trava durante transiÃ§Ãµes.
- [x] Implementar direÃ§Ã£o de avanÃ§o e retorno.
- [x] Reiniciar animaÃ§Ãµes internas do slide ativo.
- [x] Atualizar progresso e persistÃªncia depois da troca.
- [x] Testar botÃµes, teclado e toque.

## Fase 5 - Estrutura do quiz

- [x] Criar dados das trÃªs perguntas conforme `quiz.md`.
- [x] Criar camada e cabeÃ§alho do quiz.
- [x] Criar componente de pergunta.
- [x] Criar alternativas acessÃ­veis.
- [x] Implementar resposta Ãºnica.
- [x] Implementar feedback correto/incorreto.
- [x] Implementar explicaÃ§Ã£o.
- [x] Implementar avanÃ§o manual.
- [x] Implementar reinÃ­cio completo.

## Fase 6 - CronÃ´metro e pontuaÃ§Ã£o

- [x] Implementar cronÃ´metro de 60 segundos.
- [x] Implementar indicador visual de progresso.
- [x] Implementar mudanÃ§as verde, laranja e vermelho.
- [x] Implementar pulso nos Ãºltimos cinco segundos.
- [x] Implementar resoluÃ§Ã£o por tempo esgotado.
- [x] Garantir exclusÃ£o mÃºtua entre resposta e timeout.
- [x] Implementar fÃ³rmula de pontuaÃ§Ã£o.
- [x] Exibir pontos conquistados e acumulados.
- [x] Calcular tempo mÃ©dio.
- [x] Criar tela final e mensagens por desempenho.

## Fase 7 - Sons

- [x] Criar gerenciador de Web Audio API.
- [x] Desbloquear Ã¡udio somente apÃ³s interaÃ§Ã£o.
- [x] Implementar som de navegaÃ§Ã£o.
- [x] Implementar som de abertura do quiz.
- [x] Implementar som de acerto.
- [x] Implementar som de erro.
- [x] Implementar contagem dos Ãºltimos cinco segundos.
- [x] Implementar som de tempo esgotado.
- [x] Implementar som de resultado.
- [x] Implementar controle e atalho `S`.
- [x] Persistir preferÃªncia.
- [x] Prevenir sobreposiÃ§Ã£o indevida.

## Fase 8 - Modo apresentador

- [x] Criar painel recolhÃ­vel.
- [x] Exibir slide atual e prÃ³ximo slide.
- [x] Implementar cronÃ´metro geral.
- [x] Implementar cronÃ´metro do slide atual.
- [x] Criar Ã¡rea de notas por slide.
- [x] Persistir notas.
- [x] Adicionar controles de Universo, quiz, som e tempo.
- [x] Implementar atalho `N`.

## Fase 9 - Ajuda e preferÃªncias

- [x] Criar modal de atalhos.
- [x] Implementar atalho `?`.
- [x] Criar controle manual de movimento reduzido.
- [x] Criar aÃ§Ã£o para limpar progresso e preferÃªncias.
- [x] Exibir toasts acessÃ­veis para mudanÃ§as de configuraÃ§Ã£o.

## Fase 10 - Acessibilidade

- [x] Revisar semÃ¢ntica e rÃ³tulos ARIA.
- [x] Implementar gerenciamento de foco.
- [x] Implementar focus trap nos modais.
- [x] Criar regiÃµes `aria-live` para feedback importante.
- [x] Garantir indicadores alÃ©m de cor.
- [x] Verificar contraste.
- [x] Verificar Ã¡reas de toque.
- [x] Testar com teclado.
- [x] Testar com movimento reduzido.
- [x] Testar zoom em 200%.

## Fase 11 - Desempenho e robustez

- [x] Limitar partÃ­culas e remover elementos apÃ³s animaÃ§Ãµes.
- [x] Cancelar `requestAnimationFrame` quando nÃ£o necessÃ¡rio.
- [x] Cancelar cronÃ´metros ao mudar de estado.
- [x] Garantir apenas um timer de pergunta.
- [x] Testar falha de `localStorage`.
- [x] Testar Ã¡udio indisponÃ­vel.
- [x] Testar funcionamento offline.

## Fase 12 - Testes de aceite

- [x] Confirmar que os 19 slides continuam intactos.
- [x] Testar todos os atalhos.
- [x] Testar navegaÃ§Ã£o por botÃµes, teclado e toque.
- [x] Testar acesso a cada slide pelo Universo.
- [x] Testar pergunta correta.
- [x] Testar pergunta incorreta.
- [x] Testar tempo esgotado.
- [x] Testar resposta no Ãºltimo segundo.
- [x] Testar reinÃ­cio do quiz.
- [x] Testar fechamento e reabertura do quiz.
- [x] Testar sons ligados e desligados.
- [x] Testar pausa ao trocar de aba.
- [x] Testar persistÃªncia apÃ³s recarregar.
- [x] Testar desktop, tablet e celular.
- [x] Validar que nenhuma falha opcional impede a apresentaÃ§Ã£o bÃ¡sica.

## Ordem recomendada para demonstraÃ§Ã£o ao vivo

1. Mostrar a apresentaÃ§Ã£o original funcionando.
2. Ler `requirements.md` e explicar o comportamento esperado.
3. Mostrar as decisÃµes de `design.md` e `interactions.md`.
4. Pedir ao agente para implementar somente a tela inicial e o Universo de Slides.
5. Testar o acesso a um slide.
6. Mostrar a versÃ£o completa previamente preparada com quiz, sons e modo apresentador.
7. Comparar a implementaÃ§Ã£o com os critÃ©rios de aceite.

