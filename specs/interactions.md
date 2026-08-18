# DEV + IA Interactive Experience - Interações

## 1. Estados principais

```text
BOOT
  -> HOME
  -> UNIVERSE
  -> PRESENTATION
  -> QUIZ
  -> QUIZ_RESULT
```

- `BOOT`: carrega preferências e prepara elementos.
- `HOME`: tela inicial.
- `UNIVERSE`: mapa interativo dos 19 slides.
- `PRESENTATION`: apresentação tradicional.
- `QUIZ`: perguntas e cronômetros.
- `QUIZ_RESULT`: resultado final.

Somente um estado principal pode estar visível por vez.

## 2. Inicialização

1. Ler preferências do `localStorage` com tratamento de erro.
2. Registrar eventos globais apenas uma vez.
3. Preparar o sistema de áudio sem iniciar o contexto sonoro.
4. Gerar os cards do Universo com base nos slides existentes.
5. Exibir a tela inicial.
6. Mostrar `Continuar` somente quando houver um slide salvo.

## 3. Tela inicial

### Iniciar apresentação

1. Usuário ativa o botão.
2. Liberar áudio após a interação, caso esteja habilitado.
3. Executar animação de saída.
4. Abrir o slide 1.
5. Marcar o slide como visitado.

### Continuar

1. Ler o último índice válido.
2. Caso seja inválido, abrir o slide 1.
3. Abrir a apresentação no índice resolvido.

### Explorar slides

1. Animação da tela inicial se afasta.
2. Universo aparece com cards em cascata.
3. Foco é movido para o título ou primeiro card.

## 4. Universo de Slides

### Flutuação

- Usar animação CSS com duração variada por card.
- Limitar deslocamento vertical a aproximadamente 8-16 px.
- Não alterar a ordem de leitura nem a área clicável.
- Interromper a flutuação no hover/foco para facilitar a seleção.

### Parallax

- Calcular deslocamento normalizado do ponteiro em relação ao centro.
- Aplicar deslocamento por profundidade com `requestAnimationFrame`.
- Limitar a transformação total.
- Desativar em toque, movimento reduzido e aba oculta.

### Abertura de slide

1. Card selecionado recebe classe de expansão.
2. Demais cards reduzem opacidade.
3. Após a animação, ativar `PRESENTATION`.
4. Abrir o slide correspondente.
5. Atualizar persistência.
6. Mover foco para o conteúdo do slide.

## 5. Navegação entre slides

- Bloquear navegação repetida durante a transição.
- Ao avançar, aplicar saída à esquerda e entrada pela direita.
- Ao voltar, inverter a direção.
- Atualizar o slide somente uma vez por ação.
- Reiniciar as animações internas do slide ativado.
- Salvar o índice e atualizar slides visitados.
- Se o foco estiver dentro de um modal ou quiz, não navegar pelos slides.

## 6. Atalhos

| Atalho | Ação | Condição |
|---|---|---|
| `ArrowRight`, `Space`, `PageDown` | Próximo slide | apresentação ativa, sem modal |
| `ArrowLeft`, `PageUp` | Slide anterior | apresentação ativa, sem modal |
| `Home` | Primeiro slide | apresentação ativa |
| `End` | Último slide | apresentação ativa |
| `M` | Universo | fora de campo editável |
| `Q` | Quiz | fora de campo editável |
| `T` | Pausar/iniciar tempo geral | apresentação ativa |
| `F` | Tela cheia | sempre que permitido |
| `N` | Notas | apresentação ativa |
| `S` | Alternar som | fora de campo editável |
| `?` | Ajuda | sempre |
| `Esc` | Fechar camada superior | quando houver camada |

Não executar atalhos quando o usuário estiver digitando em `input`, `textarea`, `select` ou elemento editável.

## 7. Quiz

### Entrada

1. Salvar o slide atual para retorno.
2. Pausar o cronômetro geral, se configurado.
3. Abrir a camada do quiz.
4. Reproduzir som de abertura.
5. Renderizar a primeira pergunta.
6. Iniciar o cronômetro somente depois da animação de entrada.

### Resposta

1. Verificar se a pergunta ainda está ativa.
2. Bloquear imediatamente todas as alternativas.
3. Parar o cronômetro.
4. Comparar a alternativa selecionada.
5. Atualizar pontuação e acertos.
6. Reproduzir o som correspondente.
7. Mostrar estados correto/incorreto.
8. Mostrar explicação.
9. Mostrar botão de avanço.

### Tempo esgotado

1. Fixar tempo em zero.
2. Bloquear alternativas.
3. Marcar a pergunta como não respondida.
4. Destacar a resposta correta.
5. Reproduzir som de tempo esgotado.
6. Exibir explicação e botão de avanço.

### Próxima pergunta

- Não permitir avanço antes de responder ou terminar o tempo.
- Cancelar qualquer timer anterior.
- Atualizar índice, renderizar e reiniciar com 60 segundos.
- Após a terceira pergunta, abrir o resultado.

## 8. Sons

- Som de navegação pode tocar em volume baixo.
- Sons de feedback não podem se sobrepor.
- Ao desativar o som, interromper sons ativos quando possível.
- A contagem final deve tocar no máximo uma vez por segundo.

## 9. Visibilidade da página

Quando `document.hidden` for verdadeiro:

- Pausar o cronômetro da pergunta.
- Pausar o cronômetro geral.
- Suspender parallax e efeitos contínuos.

Quando a página voltar:

- Não retomar automaticamente o quiz; exibir estado `Pausado` e ação `Continuar`.
- O cronômetro geral pode retomar conforme configuração.

## 10. Persistência

Chaves sugeridas:

```text
devIa.lastSlide
devIa.visitedSlides
devIa.soundEnabled
devIa.reducedMotion
devIa.presenterNotes
devIa.lastQuizResult
```

- Validar todo valor lido.
- Usar `try/catch` em operações de armazenamento.
- Não armazenar intervalos, nós DOM ou dados transitórios.

## 11. Prevenção de conflitos

- `Esc` fecha primeiro ajuda/notas, depois quiz/universo e somente então atua na tela cheia.
- O espaço não avança slides quando um botão estiver focado.
- Toques dentro do quiz não acionam swipe da apresentação.
- A abertura repetida de um modal não deve duplicar eventos.
- Cronômetros devem possuir identificador único e função central de cancelamento.

