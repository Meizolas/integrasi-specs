# Plano de testes

## T01 — Preservação dos slides

Dado que a aplicação foi modificada  
Quando a apresentação for carregada  
Então os 19 slides devem continuar presentes.

## T02 — Resposta correta

Dado que uma pergunta está ativa  
Quando o usuário seleciona a resposta correta  
Então o timer deve parar, o som de acerto deve tocar e os pontos devem ser calculados.

## T03 — Tempo esgotado

Dado que o cronômetro chegou a zero  
Então as alternativas devem ser bloqueadas e a resposta correta deve ser revelada.

## T04 — Cronômetro duplicado

Dado que o quiz foi reiniciado  
Então apenas um timer deve permanecer ativo.