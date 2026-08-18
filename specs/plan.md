# Plano de implementação

## 1. Estado atual

A apresentação possui 19 slides, navegação por teclado, tela cheia,
barra de progresso, suporte a toque, animações e cursor personalizado.

## 2. Estratégia

A implementação será incremental, preservando o comportamento atual.

Ordem:

1. Criar backup.
2. Criar controle de estados.
3. Implementar persistência.
4. Criar tela inicial.
5. Criar Universo de Slides.
6. Criar transições.
7. Implementar quiz.
8. Implementar cronômetros.
9. Implementar sons.
10. Implementar modo apresentador.
11. Aplicar acessibilidade.
12. Executar testes.

## 3. Arquitetura

- AppState: estado principal;
- NavigationController: navegação;
- UniverseController: cards flutuantes;
- QuizController: perguntas e respostas;
- TimerController: cronômetros;
- AudioManager: sons;
- StorageManager: persistência;
- ModalController: camadas;
- PresenterController: modo apresentador.

## 4. Riscos

- Conflito entre atalhos do quiz e dos slides;
- Mais de um cronômetro em execução;
- Áudio bloqueado pelo navegador;
- Animações pesadas;
- Alteração acidental dos slides existentes.

## 5. Mitigações

- Controlador central de atalhos;
- Gerenciador único de timers;
- Inicialização do áudio após interação;
- Movimento reduzido;
- Backup antes da implementação.