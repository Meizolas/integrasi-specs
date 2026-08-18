# DEV + IA Interactive Experience - Requisitos

## 1. Objetivo

Evoluir a apresentação web existente em `presentation.html` para uma experiência interativa, animada e adequada a uma apresentação ao vivo, preservando integralmente o conteúdo dos 19 slides e todas as funcionalidades já existentes.

## 2. Escopo funcional

### RF01 - Tela inicial

- Ao abrir a aplicação, exibir uma tela inicial antes dos slides.
- A tela deve apresentar o título `DEV + IA` e o subtítulo `O que as empresas realmente esperam de você`.
- Deve conter os botões `Iniciar apresentação`, `Continuar` e `Explorar slides`.
- `Continuar` só deve aparecer quando existir progresso salvo.
- `Iniciar apresentação` deve abrir o slide 1.
- `Continuar` deve abrir o último slide visitado.
- `Explorar slides` deve abrir o Universo de Slides.

### RF02 - Universo de Slides

- Representar os 19 slides como cards flutuantes.
- Cada card deve apresentar número, título, categoria e estado de visualização.
- Os cards devem possuir movimento suave, profundidade e parallax discreto.
- O usuário deve poder abrir qualquer slide clicando no card correspondente.
- O slide atual deve possuir destaque visual.
- Slides já visitados devem exibir um indicador de conclusão.
- O Universo deve ser acessível pela tecla `M` durante a apresentação.

### RF03 - Navegação da apresentação

- Preservar os botões de próximo e anterior.
- Preservar a navegação pelas setas, espaço, Page Up, Page Down, Home e End.
- Preservar suporte a gestos horizontais em telas sensíveis ao toque.
- Atualizar contador, número do slide e barra de progresso.
- Permitir retornar ao Universo de Slides sem recarregar a página.

### RF04 - Transições e animações

- Animar a entrada e a saída dos slides.
- Revelar cards, fluxos e timelines em sequência.
- Utilizar transições entre 400 ms e 700 ms.
- Pausar animações quando a aba ficar oculta.
- Reduzir efeitos automaticamente em dispositivos de menor desempenho.
- Respeitar `prefers-reduced-motion`.

### RF05 - Quiz

- O quiz deve conter exatamente três perguntas.
- Cada pergunta deve possuir quatro alternativas e apenas uma correta.
- Exibir uma pergunta por vez.
- Permitir apenas uma resposta por pergunta.
- Após a resposta, bloquear as alternativas.
- Informar visualmente se a resposta está correta ou incorreta.
- Exibir uma explicação depois da resposta ou do término do tempo.
- Permitir avanço manual para a próxima pergunta.
- Exibir resultado final com acertos, pontuação e tempo médio.
- Permitir reiniciar o quiz.
- Permitir retornar à apresentação.

### RF06 - Cronômetro do quiz

- Cada pergunta deve possuir 60 segundos.
- O cronômetro deve começar quando a pergunta estiver completamente visível.
- Exibir tempo no formato `00:60` até `00:00`.
- Exibir também progresso visual circular ou linear.
- Usar estado verde de 60 a 31 segundos.
- Usar estado laranja de 30 a 11 segundos.
- Usar estado vermelho de 10 a 0 segundos.
- Pulsar visualmente nos últimos cinco segundos.
- Ao chegar a zero, bloquear alternativas, revelar a correta e reproduzir o som de tempo esgotado.
- O avanço após o tempo acabar deve ser manual.

### RF07 - Pontuação

- Resposta correta deve valer 100 pontos base.
- Adicionar um ponto de bônus por segundo restante.
- Resposta incorreta ou não respondida deve valer zero.
- Pontuação máxima deve ser 480 pontos.
- Exibir os pontos conquistados depois de cada resposta correta.
- Exibir pontuação acumulada durante o quiz.

### RF08 - Sons

- Disponibilizar sons para abertura do quiz, acerto, erro, últimos segundos, tempo esgotado, resultado final e navegação.
- Gerar os sons localmente com Web Audio API.
- Não depender de arquivos ou serviços externos.
- Não reproduzir áudio antes da primeira interação do usuário.
- Disponibilizar controle de som ligado/desligado.
- Salvar a preferência no `localStorage`.

### RF09 - Modo apresentador

- Disponibilizar um painel discreto para o apresentador.
- Mostrar slide atual, título do próximo slide, tempo total e tempo no slide atual.
- Permitir abrir o Universo, iniciar o quiz, controlar o som e reiniciar cronômetros.
- Disponibilizar uma área de anotações por slide.
- Salvar as anotações no navegador.

### RF10 - Persistência

- Salvar o último slide visitado.
- Salvar a lista de slides visualizados.
- Salvar preferência de som e movimento.
- Salvar anotações do apresentador.
- Salvar o resultado mais recente do quiz.
- Disponibilizar opção para limpar os dados salvos.

### RF11 - Ajuda e atalhos

- Exibir um modal de ajuda ao pressionar `?`.
- A ajuda deve listar os atalhos disponíveis.
- `M`: abrir ou fechar o Universo.
- `Q`: abrir o quiz.
- `T`: iniciar ou pausar o cronômetro geral.
- `F`: alternar tela cheia.
- `N`: abrir anotações.
- `S`: ativar ou desativar sons.
- `Esc`: fechar o componente aberto; se nenhum estiver aberto, alternar tela cheia conforme o comportamento existente.

## 3. Requisitos não funcionais

### RNF01 - Tecnologias

- Usar apenas HTML, CSS e JavaScript puro.
- Não usar frameworks, bibliotecas, APIs ou CDNs.
- Funcionar ao abrir o arquivo localmente.

### RNF02 - Compatibilidade

- Suportar as versões atuais de Chrome, Edge e Firefox.
- Funcionar em desktop, tablet e celular.
- Priorizar o uso em notebook conectado a projetor 16:9.

### RNF03 - Desempenho

- Manter animações próximas de 60 FPS em hardware comum.
- Evitar criar partículas ou elementos DOM ilimitados.
- Cancelar intervalos e animações que não estiverem visíveis.
- Não executar mais de um cronômetro do quiz simultaneamente.

### RNF04 - Preservação

- Não alterar o conteúdo textual dos 19 slides.
- Não remover navegação, tela cheia, barra de progresso, suporte a toque, ícones ou cursor personalizado.
- Novas funcionalidades não podem impedir a apresentação básica de funcionar.

### RNF05 - Segurança da apresentação

- A apresentação deve continuar navegável se áudio, animações ou armazenamento falharem.
- Erros do `localStorage` devem ser tratados sem interromper a aplicação.
- O quiz deve possuir estado inicial determinístico e opção de reinício.

## 4. Fora do escopo

- Backend, login ou banco de dados remoto.
- Envio de respostas pela internet.
- Quiz com celulares da plateia.
- Integração com IA ou API externa durante a apresentação.
- Edição do conteúdo dos slides pela interface.
- Sincronização entre dispositivos.

## 5. Critérios gerais de aceite

- Os 19 slides originais continuam presentes e navegáveis.
- A aplicação funciona totalmente offline.
- O Universo permite acessar qualquer slide.
- O quiz possui três perguntas funcionais com 60 segundos cada.
- Sons de acerto, erro e tempo esgotado são diferentes e podem ser desativados.
- A interface funciona com mouse, teclado e toque.
- Preferências e progresso sobrevivem ao recarregamento da página.
- O modo de movimento reduzido desativa flutuação, parallax e animações intensas.

