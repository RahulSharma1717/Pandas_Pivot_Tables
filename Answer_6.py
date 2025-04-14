# Find the minimum purchase amount of each product.

import pandas as pd

df = pd.read_csv('retail_data.csv')
#pd.set_option('display.max_columns', None)

pivot_table = df.pivot_table(index='products', values='Amount', aggfunc='min').reset_index()
print(pivot_table)


"""Output:
            products     Amount
0              4K TV  11.092281
1       A-line dress  10.617622
2    Acer Iconia Tab  10.106953
3         Acer Swift  10.325613
4             Action  11.265383
..               ...        ...
313       Wrap dress  10.155775
314           Wrench  10.367558
315        Xiaomi Mi  11.782073
316             iPad  11.002920
317           iPhone  10.458969

[318 rows x 2 columns]
"""