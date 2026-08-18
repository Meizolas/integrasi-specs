# DEV + IA Interactive Experience - Sons

## 1. Objetivo

Criar feedback sonoro curto, distinto e funcional usando Web Audio API, sem arquivos externos e sem comprometer a apresentação quando o áudio estiver indisponível.

## 2. Regras técnicas

- Criar `AudioContext` somente após interação do usuário.
- Reutilizar uma única instância.
- Se estiver suspensa, chamar `resume()` após interação.
- Todo som deve respeitar a preferência global.
- Usar ganho baixo para evitar sustos em caixas de som.
- Capturar falhas sem interromper a aplicação.
- Não criar loops permanentes.

## 3. Sons obrigatórios

### Navegação

- Clique curto e discreto.
- Duração aproximada: 40-80 ms.
- Volume muito baixo.

### Abertura do quiz

- Duas notas ascendentes.
- Transmitir início de uma nova etapa.
- Duração máxima: 500 ms.

### Resposta correta

- Três notas ascendentes.
- Timbre leve e positivo.
- Duração máxima: 700 ms.

### Resposta incorreta

- Duas notas descendentes.
- Som curto, sem ser agressivo.
- Duração máxima: 500 ms.

### Últimos cinco segundos

- Pulso curto uma vez por segundo.
- A última marca pode ser ligeiramente mais grave.
- Não tocar se o usuário responder antes.

### Tempo esgotado

- Três pulsos rápidos e uma nota final descendente.
- Deve ser diferente do som de erro.
- Duração máxima: 900 ms.

### Resultado final

- Com três acertos: sequência comemorativa curta.
- Com menos de três acertos: som neutro de conclusão.
- Duração máxima: 1,2 s.

## 4. Síntese sugerida

- Usar `OscillatorNode` e `GainNode`.
- Preferir ondas `sine` ou `triangle`.
- Aplicar ataque e decaimento para evitar cliques secos.
- Criar funções como `playTone`, `playSequence`, `playCorrect`, `playWrong` e `playTimeout`.

Exemplo conceitual:

```js
function playTone(frequency, duration, options = {}) {
  // Validar preferência, garantir AudioContext,
  // criar oscillator/gain, aplicar envelope e finalizar nós.
}
```

## 5. Controle de áudio

- Botão com estados `Som ativado` e `Som desativado`.
- Ícone deve refletir o estado.
- Atalho `S` alterna o som fora de campos editáveis.
- Exibir toast discreto ao alterar.
- Salvar preferência no `localStorage`.
- Estado inicial recomendado: ativado, mas silencioso até a primeira interação.

## 6. Concorrência

- Sons de resposta devem cancelar a contagem regressiva.
- Som de tempo esgotado deve tocar somente uma vez.
- Navegação não deve tocar durante sequência de acerto/erro.
- Reiniciar o quiz deve cancelar sons pendentes.

## 7. Critérios de aceite

- Acerto, erro e tempo esgotado são auditivamente diferentes.
- Nenhum áudio toca antes da primeira interação.
- Desativar som interrompe novos efeitos imediatamente.
- Recarregar preserva a preferência.
- Falha da Web Audio API não impede quiz ou navegação.
- Nenhum som continua depois de sair ou reiniciar o quiz.

