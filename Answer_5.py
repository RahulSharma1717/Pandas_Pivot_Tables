# Find the maximum payment for each payment method.

import pandas as pd

df = pd.read_csv('retail_data.csv')
#pd.set_option('display.max_columns', None)

pivot_table = df.pivot_table(index='Payment_Method', values='Total_Amount', aggfunc='max').reset_index()
print(pivot_table)


"""Output:
  Payment_Method  Total_Amount
0           Cash   4999.340097
1    Credit Card   4999.171428
2     Debit Card   4998.306569
3         PayPal   4999.625796
"""