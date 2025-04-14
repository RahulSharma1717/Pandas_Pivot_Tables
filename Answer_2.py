# How many transactions were made for each unique total purchase count, categorized by customer segments?

import pandas as pd

df = pd.read_csv('retail_data.csv')
#pd.set_option('display.max_columns', None)

pivot_table = df.pivot_table(index='Total_Purchases', values='Customer_Segment', aggfunc='count').reset_index()
print(pivot_table)


"""Output:
   Total_Purchases  Customer_Segment
0                1             31050
1                2             31084
2                3             31070
3                4             30795
4                5             31112
5                6             27767
6                7             27696
7                8             27966
8                9             27757
9               10             27614
"""