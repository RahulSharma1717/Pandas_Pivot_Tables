# Find the average purchase amount for each product category.

import pandas as pd

df = pd.read_csv('retail_data.csv')
#pd.set_option('display.max_columns', None)

pivot_table = df.pivot_table(index='Product_Category', values='Total_Amount', aggfunc='mean').reset_index()
print(pivot_table)


"""Output:
  Product_Category  Total_Amount
0            Books   1367.069440
1         Clothing   1368.820004
2      Electronics   1369.736547
3          Grocery   1366.061942
4       Home Decor   1366.480831
"""