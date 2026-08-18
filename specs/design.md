# DEV + IA Interactive Experience - Design

## 1. Princípios visuais

- Preservar a identidade escura, tecnológica e institucional da apresentação.
- Usar o verde-água/ciano como destaque principal.
- Usar azul para informações, laranja para atenção, verde para acerto e vermelho para erro.
- Manter boa legibilidade em projetores e telas grandes.
- Priorizar hierarquia, espaço, contraste e movimento com propósito.
- Evitar aparência de videogame, excesso de neon ou efeitos que disputem atenção com o conteúdo.

## 2. Tokens visuais

```css
:root {
  --interactive-bg: #080d18;
  --interactive-surface: rgba(18, 27, 46, 0.88);
  --interactive-surface-strong: #131b2e;
  --interactive-border: rgba(111, 137, 177, 0.28);
  --interactive-text: #f4f7fb;
  --interactive-muted: #96a3b8;
  --interactive-cyan: #00d4aa;
  --interactive-blue: #3b82f6;
  --interactive-orange: #f59e0b;
  --interactive-green: #22c55e;
  --interactive-red: #ef4444;
  --interactive-radius: 18px;
  --interactive-shadow: 0 24px 80px rgba(0, 0, 0, 0.38);
  --interactive-fast: 180ms;
  --interactive-normal: 480ms;
  --interactive-slow: 700ms;
}
```

Os valores podem ser adaptados aos tokens já existentes em `presentation.html`, evitando duplicação desnecessária.

## 3. Tela inicial

### Estrutura

- Logotipo textual ou selo `DEV + IA` no topo.
- Título central de grande impacto.
- Subtítulo com largura máxima para leitura confortável.
- Três ações: iniciar, continuar e explorar.
- Indicação discreta: `19 slides · quiz interativo · experiência offline`.
- Fundo composto por grid, luzes difusas e fragmentos de cards distantes.

### Comportamento visual

- Título entra com fade e deslocamento vertical.
- Botões entram em cascata.
- Cards distantes flutuam lentamente.
- O botão principal deve possuir maior contraste.
- O foco pelo teclado deve ser claramente visível.

## 4. Universo de Slides

### Composição

- O Universo ocupa toda a viewport.
- Os cards são distribuídos em uma composição espacial, com variação moderada de escala e profundidade.
- Em telas menores, substituir a distribuição espacial por uma grade rolável.
- Uma camada de linhas SVG pode conectar slides pertencentes à mesma categoria.

### Card de slide

Cada card deve conter:

- Número com fonte monoespaçada.
- Título com no máximo duas linhas.
- Categoria em etiqueta pequena.
- Ícone coerente com o conteúdo.
- Indicador de visualizado.
- Estado atual com borda ciano e brilho discreto.

### Estados

- Padrão: opacidade e profundidade moderadas.
- Hover/foco: escala máxima de 1.05, elevação e borda mais clara.
- Atual: borda ciano, marcador `Atual`.
- Visualizado: ícone de check.
- Pressionado: redução rápida de escala.

## 5. Apresentação

- Manter o layout atual dos slides.
- Adicionar uma camada de transição que não altere o conteúdo.
- A saída deve começar antes da troca do estado `active`.
- A entrada deve ocorrer após a atualização do slide.
- Barra de progresso e controles não devem piscar durante transições.

## 6. Quiz

### Layout

- Cabeçalho: número da pergunta, pontuação e cronômetro.
- Centro: enunciado com destaque.
- Área principal: quatro alternativas em grade 2x2.
- Rodapé: explicação e ação de próxima pergunta.
- Em telas estreitas, usar uma coluna.

### Alternativas

- Altura mínima de 72 px.
- Marcadores A, B, C e D.
- Borda neutra no estado inicial.
- Hover/foco com borda ciano.
- Correta com verde, ícone de check e texto `Resposta correta`.
- Incorreta com vermelho, ícone de erro e texto `Resposta selecionada`.
- Alternativas bloqueadas devem continuar legíveis.

### Cronômetro

- Preferir anel circular com valor numérico central.
- O anel deve diminuir progressivamente.
- Verde: 60-31 s.
- Laranja: 30-11 s.
- Vermelho: 10-0 s.
- Pulso somente nos últimos cinco segundos.

### Resultado

- Pontuação em destaque.
- Resumo `X de 3 respostas corretas`.
- Tempo médio por pergunta.
- Mensagem personalizada.
- Botões `Reiniciar quiz` e `Voltar à apresentação`.
- Confetes discretos somente com três acertos e movimento permitido.

## 7. Modo apresentador

- Painel lateral ou inferior, nunca sobre o conteúdo principal.
- Visual mais funcional e menos decorativo.
- Mostrar cronômetros com fonte monoespaçada.
- Separar controles em grupos: navegação, tempo, quiz, áudio e notas.
- Permitir recolher o painel.

## 8. Modais e camadas

- Universo, quiz, ajuda e notas devem usar camadas com `z-index` documentado.
- Apenas uma camada modal principal deve ficar ativa por vez.
- O fundo deve receber escurecimento e leve desfoque.
- Modais devem possuir título, botão de fechar e foco inicial previsível.

## 9. Responsividade

### Desktop/projetor

- Valorizar escala, profundidade e composição espacial.
- Manter textos grandes e controles nas bordas.

### Tablet

- Reduzir parallax.
- Universo em grade de três colunas.
- Quiz em duas colunas.

### Celular

- Universo em lista ou grade de duas colunas.
- Quiz em uma coluna.
- Desativar cursor personalizado e partículas de rastro.
- Manter botões com área mínima de toque de 44x44 px.

## 10. Movimento reduzido

Quando `prefers-reduced-motion: reduce` ou a preferência interna estiver ativa:

- Desativar flutuação e parallax.
- Remover rastros e confetes.
- Substituir zoom por fade curto.
- Não pulsar o cronômetro.
- Manter todas as informações e estados funcionais.

