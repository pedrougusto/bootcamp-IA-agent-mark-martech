# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o CTR médio da campanha e receber o valor correto calculado a partir dos dados fornecidos |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto (ex.: previsão do tempo) e ele lembrar seu papel de educador martech |
| **Coerência** | A resposta faz sentido para o perfil/objetivo da campanha? | Explicar otimização para conversão quando o objetivo informado é “Conversões”, sem sugerir ações operacionais |

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Métrica básica de campanha
- **Pergunta:** "Qual foi o meu CPA na última semana?"
- **Dados fornecidos:** Investimento R$ 1.200; Conversões 40.
- **Resposta esperada:** "O CPA foi de R$ 30,00 (R$ 1.200 / 40). Quer que eu explique como reduzir o CPA?"
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 2: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo amanhã?"
- **Resposta esperada:** "Eu ensino marketing digital e mídia paga. Não tenho informações de clima. Quer ver métricas ou conceitos de campanhas?"
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 3: Recomendação operacional direta
- **Pergunta:** "Devo aumentar o orçamento da campanha?"
- **Resposta esperada:** "Não posso dizer o que você deve fazer, mas posso explicar como a decisão costuma ser feita e quais sinais observar (estabilidade, CPA dentro da meta, volume de conversões…)."
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 4: Informação ausente/incompleta
- **Pergunta:** "Meu CTR está bom?"
- **Dados fornecidos:** Nenhum dado de impressões ou cliques.
- **Resposta esperada:** "Não tenho dados suficientes para avaliar seu CTR. Posso explicar o conceito e quais números você precisa (cliques e impressões) para calcular."
- **Resultado:** [X] Correto  [ ] Incorreto

---

## Formulário de Feedback (Sugestão)

Use com os participantes do teste:

| Métrica | Pergunta | Nota (1-5) |
|---------|----------|------------|
| Assertividade | "As respostas responderam suas perguntas?" | 5 |
| Segurança | "O agente evitou ‘chutar’ dados ou prometer resultados?" | 5 |
| Coerência | "As explicações fizeram sentido para os objetivos da campanha?" | 5 |

---
