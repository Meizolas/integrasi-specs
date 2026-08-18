# DEV + IA Interactive Experience - Quiz

## 1. Regras gerais

- Exatamente três perguntas.
- Quatro alternativas por pergunta.
- Apenas uma resposta correta.
- Uma tentativa por pergunta.
- 60 segundos por pergunta.
- Avanço manual após resposta ou tempo esgotado.
- Ordem fixa para a demonstração ser previsível.
- Textos devem ser armazenados em uma estrutura JavaScript, separados da renderização.

## 2. Estrutura de dados sugerida

```js
const quizQuestions = [
  {
    id: 1,
    question: 'Como uma LLM gera texto?',
    options: ['...', '...', '...', '...'],
    correctIndex: 2,
    explanation: '...',
    topic: 'LLMs'
  }
];
```

## 3. Pergunta 1

**Tema:** LLMs

**Pergunta:** Como uma LLM gera texto?

**Alternativas:**

A. Pensando na frase completa antes de responder.

B. Consultando obrigatoriamente a internet.

C. Prevendo o próximo token com base no contexto.

D. Copiando uma frase completa dos dados de treinamento.

**Resposta correta:** C

**Explicação:** Uma LLM calcula probabilidades para possíveis próximos tokens e repete esse processo considerando o contexto disponível. A analogia com autocomplete é útil, mas não descreve toda a complexidade do modelo.

## 4. Pergunta 2

**Tema:** Agentes

**Pergunta:** Qual é a principal diferença entre um chatbot e um agente?

**Alternativas:**

A. Um agente sempre possui mais parâmetros.

B. Um chatbot não utiliza inteligência artificial.

C. Um agente pode planejar ações e utilizar ferramentas.

D. Um agente funciona somente no terminal.

**Resposta correta:** C

**Explicação:** Um chatbot normalmente responde mensagens. Um agente pode receber um objetivo, planejar, utilizar ferramentas, observar resultados e decidir a próxima ação.

## 5. Pergunta 3

**Tema:** SDD

**Pergunta:** Qual é a ideia central do Spec-Driven Development?

**Alternativas:**

A. Escrever o código antes de definir os requisitos.

B. Deixar todas as decisões para a inteligência artificial.

C. Especificar claramente o que será construído antes da implementação.

D. Utilizar vários agentes em qualquer projeto.

**Resposta correta:** C

**Explicação:** No SDD, requisitos, comportamento, design, restrições e tarefas são definidos antes da implementação. O código passa a ser consequência de uma especificação clara.

## 6. Pontuação

```text
Resposta correta = 100 pontos + segundos restantes
Resposta incorreta = 0 pontos
Tempo esgotado = 0 pontos
Pontuação máxima = 3 x (100 + 60) = 480 pontos
```

- Arredondar tempo restante para inteiro antes do cálculo.
- Não conceder pontos duas vezes.
- Exibir `+N pontos` após resposta correta.

## 7. Resultado final

### Três acertos

`Você entendeu a ferramenta. Agora é hora de usá-la.`

### Dois acertos

`Muito bom! Só falta ajustar alguns tokens.`

### Um acerto

`O modelo precisa de mais contexto.`

### Zero acertos

`Calma. Antes do apocalipse, vamos revisar a tecnologia.`

## 8. Critérios de aceite do quiz

- O cronômetro reinicia em 60 para cada pergunta.
- Uma resposta não pode ser alterada depois de selecionada.
- Responder nos últimos instantes não pode gerar resposta e tempo esgotado simultaneamente.
- Ao acabar o tempo, a resposta correta é revelada.
- O botão de próxima pergunta aparece somente após a resolução.
- O resultado corresponde exatamente às três respostas registradas.
- Reiniciar limpa índice, pontuação, acertos, tempos e estados visuais.
- Fechar e reabrir o quiz durante uma tentativa deve solicitar reinício ou retomada; nunca criar dois timers.

