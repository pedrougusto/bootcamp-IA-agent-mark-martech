# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Para que serve no Mark? |
|---------|---------|---------------------|
| `marketing_campaign_english.csv` | CSV | Contextualizar interações das campanhas de mídia Ads, ou seja, dar instruções e melhorias de forma mais eficiente. |

---

## Estratégia de Integração

### Como os dados são carregados?

Existem duas possibilidades, injetar os dados diretamente no prompt (Ctrl + C, Ctrl + V) ou carregar os arquivos via código, como no exemplo abaixo:

```python
import pandas as pd
import json

campanhas = pd.read_csv('./data/marketing_campaign_english.csv')

```

### Como os dados são usados no prompt?

Para simplificar, podemos simplesmente "injetar" os dados em nosso prompt, garantindo que o Agente tenha o melhor contexto possível. Lembrando que, em soluções mais robustas, o ideal é que essas informaçoes sejam carregadas dinamicamente para que possamos ganhar flexibilidade.

```text
CAMPANHAS DE MARKETING (data/marketing_campaign_english.csv):
id	caption	language	platform	post_time	reach	likes	comments	shares	conversion	quality_score
1	Take advantage of our seasonal promotions with unmatched discounts and special bundle offers designed to give you the best value for your money.	English	Instagram	9/9/2024 13:25	18909	5112	346	580	612	91
2	Celebrate this festive season with amazing gift options for your loved ones. Our carefully curated gift collections are sure to bring smiles and happiness!	English	Facebook	3/23/2024 5:31	6359	1477	79	219	451	68
3	Stay ahead of the trend with our cutting-edge tech gadgets designed to simplify your daily routine. Limited quantities available, so grab yours today before itâ€™s gone!	English	Facebook	5/31/2024 6:48	18805	2826	457	154	280	78
4	Boost your business growth with our all-in-one digital marketing solution, trusted by thousands of entrepreneurs worldwide. Start your journey towards success now!	English	Facebook	5/14/2024 20:04	12556	1422	132	200	467	59
5	Get the ultimate shopping experience with our mobile app that offers convenience, security, and personalized recommendations based on your preferences.	English	Facebook	7/2/2024 11:21	3907	354	58	18	170	68
6	Discover our brand new fashion arrivals with premium quality materials and elegant designs â€“ available now in limited stock. Donâ€™t miss the chance to upgrade your style today!	English	Twitter	6/13/2024 10:07	5263	1415	164	83	319	49
7	Join our community of satisfied customers and explore our innovative products that make your life easier and more enjoyable. Order today and enjoy fast delivery!	English	Twitter	5/14/2024 20:56	10140	793	85	103	391	89
8	Discover our brand new fashion arrivals with premium quality materials and elegant designs â€“ available now in limited stock. Donâ€™t miss the chance to upgrade your style today!	English	Twitter	11/10/2024 21:41	18480	5197	444	715	720	61
9	Boost your business growth with our all-in-one digital marketing solution, trusted by thousands of entrepreneurs worldwide. Start your journey towards success now!	English	Instagram	7/4/2024 18:55	625	34	4	4	11	70
10	Celebrate this festive season with amazing gift options for your loved ones. Our carefully curated gift collections are sure to bring smiles and happiness!	English	Twitter	8/24/2024 13:44	18700	4532	732	471	1078	79
11	Boost your business growth with our all-in-one digital marketing solution, trusted by thousands of entrepreneurs worldwide. Start your journey towards success now!	English	Instagram	8/3/2024 4:59	9056	1706	200	108	91	60
12	Shop smarter and save more with our exclusive deals and limited-time offers. Browse our latest collection and experience shopping like never before!	English	Facebook	9/29/2024 22:03	8412	2283	345	340	229	59
13	Celebrate this festive season with amazing gift options for your loved ones. Our carefully curated gift collections are sure to bring smiles and happiness!	English	Facebook	12/27/2024 18:19	10966	2204	301	155	878	63
14	Discover our brand new fashion arrivals with premium quality materials and elegant designs â€“ available now in limited stock. Donâ€™t miss the chance to upgrade your style today!	English	Facebook	5/6/2024 20:13	4925	1016	118	146	278	50
CONTINUE AT ID 1000
```
