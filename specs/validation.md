# Validação

Data: 18/08/2026

## Resultado automatizado

| Teste | Resultado | Evidência |
|---|---|---|
| T01 Preservação | Aprovado | 19 blocos comparados byte a byte com o backup |
| T02 Sintaxe/offline | Aprovado | 2 scripts compilados; zero URLs HTTP(S) |
| T03 Tela inicial | Aprovado | R01, R03, R20 e R21 |
| T04 Navegação | Aprovado | R04; contador atualizado e wrappers preservados |
| T05 Toque | Aprovado | R16E; swipe avançou exatamente um slide |
| T06 Tela cheia | Aprovado | R03B com clique real via CDP |
| T07 Universo | Aprovado | R05–R07; 19 cards e nomes acessíveis |
| T08 Resposta correta | Aprovado | R09; 159 pontos com 59s restantes na execução final |
| T09 Resposta incorreta | Aprovado | R10; pontuação inalterada |
| T10 Timeout | Aprovado | R11; timer zero, opções bloqueadas e correta revelada |
| T11 Último segundo | Aprovado | R13B; 101 pontos e resolução única |
| T12 Reinício/timer único | Aprovado | R13 e R13E |
| T13 Resultado | Aprovado | R12; resultado visível e salvo |
| T14 Aba oculta | Aprovado | R13C–R13E; pausa e retomada manual |
| T15 Áudio/falha | Aprovado | R14 e R16G; preferência salva e fallback funcional |
| T16 Armazenamento/falha | Aprovado | R16F; navegação manteve-se funcional |
| T17 Apresentador/notas | Aprovado | R16C e R16D |
| T18 Foco/teclado | Aprovado | R15, R16 e R16B |
| T19 Movimento reduzido | Aprovado | R18 e regra CSS do sistema |
| T20 Responsividade | Aprovado | Captura 1440×900, R17 mobile e R17A tablet |
| T21 Zoom/alvos | Aprovado | R17B; controles visíveis >= 44 px |
| T22 Persistência | Aprovado | R19–R21 |

## Evidências visuais

- `tests/home-desktop.png`
- `tests/universe-desktop.png`
- `tests/quiz-desktop.png`

As três capturas foram inspecionadas quanto a hierarquia, legibilidade, foco visível e ausência de sobreposição crítica.

## Correções e retestes

- O teste de `Esc` foi refeito no elemento com foco e passou.
- O caso de armazenamento foi isolado da trava de transição e passou.
- A retomada do quiz foi ajustada para iniciar somente um timer e retestada.

## Conclusão

Todos os testes automatizados e visuais executados foram aprovados. Não há requisito crítico reprovado.
