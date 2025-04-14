# Find the total sales amount for each year.

import pandas as pd

df = pd.read_csv('retail_data.csv')
pd.set_option('display.max_columns', None)
print(df)
total_sales = df.pivot_table(index='Year', values='Total_Amount', aggfunc=sum)
print(total_sales.round())


"""Output:
      Total_Amount
Year              
2023   335835955.0
2024    66142294.0
"""