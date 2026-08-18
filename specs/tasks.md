# DEV + IA Interactive Experience - Tarefas

## Fase 0 - Segurança e análise

- [ ] Criar cópia de segurança do `presentation.html`.
- [ ] Ler integralmente `presentation.html` e os arquivos de `specs/`.
- [ ] Mapear funções, seletores, atalhos e estilos existentes.
- [ ] Confirmar a quantidade de 19 slides.
- [ ] Registrar títulos e categorias dos slides.
- [ ] Definir uma estratégia de implementação que preserve o arquivo original.

## Fase 1 - Fundação

- [ ] Criar controlador de estados da aplicação.
- [ ] Centralizar abertura e fechamento de camadas.
- [ ] Criar funções seguras para leitura e escrita no `localStorage`.
- [ ] Criar gerenciador central de cronômetros.
- [ ] Evitar duplicação de event listeners.
- [ ] Implementar tratamento de `visibilitychange`.

## Fase 2 - Tela inicial

- [ ] Criar estrutura HTML da tela inicial.
- [ ] Criar estilos responsivos.
- [ ] Implementar animação de entrada.
- [ ] Implementar `Iniciar apresentação`.
- [ ] Implementar `Continuar` condicionado ao progresso.
- [ ] Implementar `Explorar slides`.
- [ ] Garantir navegação por teclado.

## Fase 3 - Universo de Slides

- [ ] Gerar cards automaticamente a partir dos slides existentes.
- [ ] Associar número, título, categoria e ícone.
- [ ] Implementar layout espacial para desktop.
- [ ] Implementar grade responsiva para tablet e celular.
- [ ] Implementar flutuação com variações controladas.
- [ ] Implementar parallax limitado com `requestAnimationFrame`.
- [ ] Implementar estados atual e visualizado.
- [ ] Implementar abertura animada de um slide.
- [ ] Implementar atalho `M`.
- [ ] Implementar retorno ao Universo.
- [ ] Desativar efeitos contínuos em movimento reduzido.

## Fase 4 - Transições da apresentação

- [ ] Preservar `updateSlide`, `nextSlide`, `prevSlide` e `goToSlide` ou equivalentes.
- [ ] Adicionar trava durante transições.
- [ ] Implementar direção de avanço e retorno.
- [ ] Reiniciar animações internas do slide ativo.
- [ ] Atualizar progresso e persistência depois da troca.
- [ ] Testar botões, teclado e toque.

## Fase 5 - Estrutura do quiz

- [ ] Criar dados das três perguntas conforme `quiz.md`.
- [ ] Criar camada e cabeçalho do quiz.
- [ ] Criar componente de pergunta.
- [ ] Criar alternativas acessíveis.
- [ ] Implementar resposta única.
- [ ] Implementar feedback correto/incorreto.
- [ ] Implementar explicação.
- [ ] Implementar avanço manual.
- [ ] Implementar reinício completo.

## Fase 6 - Cronômetro e pontuação

- [ ] Implementar cronômetro de 60 segundos.
- [ ] Implementar indicador visual de progresso.
- [ ] Implementar mudanças verde, laranja e vermelho.
- [ ] Implementar pulso nos últimos cinco segundos.
- [ ] Implementar resolução por tempo esgotado.
- [ ] Garantir exclusão mútua entre resposta e timeout.
- [ ] Implementar fórmula de pontuação.
- [ ] Exibir pontos conquistados e acumulados.
- [ ] Calcular tempo médio.
- [ ] Criar tela final e mensagens por desempenho.

## Fase 7 - Sons

- [ ] Criar gerenciador de Web Audio API.
- [ ] Desbloquear áudio somente após interação.
- [ ] Implementar som de navegação.
- [ ] Implementar som de abertura do quiz.
- [ ] Implementar som de acerto.
- [ ] Implementar som de erro.
- [ ] Implementar contagem dos últimos cinco segundos.
- [ ] Implementar som de tempo esgotado.
- [ ] Implementar som de resultado.
- [ ] Implementar controle e atalho `S`.
- [ ] Persistir preferência.
- [ ] Prevenir sobreposição indevida.

## Fase 8 - Modo apresentador

- [ ] Criar painel recolhível.
- [ ] Exibir slide atual e próximo slide.
- [ ] Implementar cronômetro geral.
- [ ] Implementar cronômetro do slide atual.
- [ ] Criar área de notas por slide.
- [ ] Persistir notas.
- [ ] Adicionar controles de Universo, quiz, som e tempo.
- [ ] Implementar atalho `N`.

## Fase 9 - Ajuda e preferências

- [ ] Criar modal de atalhos.
- [ ] Implementar atalho `?`.
- [ ] Criar controle manual de movimento reduzido.
- [ ] Criar ação para limpar progresso e preferências.
- [ ] Exibir toasts acessíveis para mudanças de configuração.

## Fase 10 - Acessibilidade

- [ ] Revisar semântica e rótulos ARIA.
- [ ] Implementar gerenciamento de foco.
- [ ] Implementar focus trap nos modais.
- [ ] Criar regiões `aria-live` para feedback importante.
- [ ] Garantir indicadores além de cor.
- [ ] Verificar contraste.
- [ ] Verificar áreas de toque.
- [ ] Testar com teclado.
- [ ] Testar com movimento reduzido.
- [ ] Testar zoom em 200%.

## Fase 11 - Desempenho e robustez

- [ ] Limitar partículas e remover elementos após animações.
- [ ] Cancelar `requestAnimationFrame` quando não necessário.
- [ ] Cancelar cronômetros ao mudar de estado.
- [ ] Garantir apenas um timer de pergunta.
- [ ] Testar falha de `localStorage`.
- [ ] Testar áudio indisponível.
- [ ] Testar funcionamento offline.

## Fase 12 - Testes de aceite

- [ ] Confirmar que os 19 slides continuam intactos.
- [ ] Testar todos os atalhos.
- [ ] Testar navegação por botões, teclado e toque.
- [ ] Testar acesso a cada slide pelo Universo.
- [ ] Testar pergunta correta.
- [ ] Testar pergunta incorreta.
- [ ] Testar tempo esgotado.
- [ ] Testar resposta no último segundo.
- [ ] Testar reinício do quiz.
- [ ] Testar fechamento e reabertura do quiz.
- [ ] Testar sons ligados e desligados.
- [ ] Testar pausa ao trocar de aba.
- [ ] Testar persistência após recarregar.
- [ ] Testar desktop, tablet e celular.
- [ ] Validar que nenhuma falha opcional impede a apresentação básica.

## Ordem recomendada para demonstração ao vivo

1. Mostrar a apresentação original funcionando.
2. Ler `requirements.md` e explicar o comportamento esperado.
3. Mostrar as decisões de `design.md` e `interactions.md`.
4. Pedir ao agente para implementar somente a tela inicial e o Universo de Slides.
5. Testar o acesso a um slide.
6. Mostrar a versão completa previamente preparada com quiz, sons e modo apresentador.
7. Comparar a implementação com os critérios de aceite.

