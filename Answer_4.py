# Find the number of transactions for each country.

import pandas as pd

df = pd.read_csv('retail_data.csv')
#pd.set_option('display.max_columns', None)

pivot_table = df.pivot_table(index='Country', values='Transaction_ID', aggfunc='count').reset_index()
print(pivot_table)


"""Output:
     Country  Transaction_ID
0  Australia           44170
1     Canada           44110
2    Germany           51433
3         UK           61398
4        USA           92800
"""