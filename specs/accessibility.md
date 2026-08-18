# DEV + IA Interactive Experience - Acessibilidade

## 1. Objetivo

Garantir que a apresentação e seus novos componentes possam ser utilizados com teclado, tecnologias assistivas, toque e preferências de movimento reduzido.

## 2. Estrutura semântica

- Usar `button` para ações.
- Usar títulos em ordem coerente.
- Identificar a região principal com `main` ou papel equivalente.
- Usar `dialog`/`aria-modal="true"` para ajuda, notas, Universo modal e quiz quando aplicável.
- Associar diálogos a títulos com `aria-labelledby`.
- Não usar `div` clicável sem semântica e teclado equivalentes.

## 3. Teclado

- Todos os controles devem ser alcançáveis por Tab.
- Foco deve ser visível.
- Enter e Espaço devem ativar botões.
- Alternativas podem usar botões ou radiogroup acessível.
- Ao abrir um modal, mover foco para ele.
- Manter foco preso dentro do modal.
- Ao fechar, devolver foco ao elemento que o abriu.
- `Esc` deve fechar a camada superior.

## 4. Quiz

- Anunciar número da pergunta e tempo disponível.
- Não anunciar cada segundo do cronômetro.
- Anunciar mudanças importantes em regiões `aria-live`:
  - 30 segundos restantes;
  - 10 segundos restantes;
  - 5 segundos restantes;
  - resposta correta/incorreta;
  - tempo esgotado;
  - pontuação final.
- Não depender apenas de verde e vermelho; incluir ícone e texto.
- Bloquear alternativas com `disabled` depois da resolução.
- A explicação deve receber foco ou ser anunciada após a resposta.

## 5. Universo de Slides

- Garantir ordem de Tab previsível, mesmo com posição visual flutuante.
- Cada card deve possuir nome acessível: `Abrir slide N: Título`.
- O estado visualizado deve ser anunciado.
- Parallax não pode mover o foco real nem alterar a ordem do DOM.

## 6. Contraste e legibilidade

- Texto comum deve atingir contraste mínimo de 4.5:1.
- Texto grande deve atingir no mínimo 3:1.
- Estados de foco devem atingir 3:1 contra o entorno.
- Evitar texto pequeno em cards projetados.
- Não usar cor como único indicador.

## 7. Movimento

- Respeitar `prefers-reduced-motion: reduce` desde o primeiro carregamento.
- Disponibilizar controle manual de movimento.
- Desativar flutuação, parallax, rastros, confetes e pulsos intensos.
- Substituir transições espaciais por fade curto.
- Nunca piscar mais de três vezes por segundo.

## 8. Áudio

- Todo feedback sonoro deve possuir equivalente visual.
- Sons devem poder ser desativados.
- Não iniciar áudio automaticamente.
- O estado de som deve possuir rótulo textual.

## 9. Toque e responsividade

- Áreas interativas mínimas de 44x44 px.
- Manter espaço suficiente entre controles.
- Não exigir hover.
- Impedir que swipe de navegação interfira no quiz.

## 10. Conteúdo e tempo

- O cronômetro é parte da dinâmica, mas deve haver controle do apresentador para pausar.
- Ao mudar de aba, pausar automaticamente.
- Fornecer explicação textual da resposta independentemente do som.

## 11. Critérios de aceite

- É possível iniciar, navegar, abrir Universo, responder ao quiz e retornar usando apenas teclado.
- O foco nunca fica perdido atrás de um modal.
- Leitor de tela recebe feedback de resposta sem anúncios excessivos do cronômetro.
- Movimento reduzido elimina efeitos contínuos.
- Todos os feedbacks sonoros possuem correspondência visual.
- Zoom do navegador em 200% não impede acesso aos controles principais.

