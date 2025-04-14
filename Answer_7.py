# Find the total purchases made in each month across years.

import pandas as pd

df = pd.read_csv('retail_data.csv')
#pd.set_option('display.max_columns', None)

pivot_table = df.pivot_table(index='Month', columns='Year', values='Total_Purchases', aggfunc='sum')
print(pivot_table)


"""Output:
Year         2023    2024
Month                    
April      196563   19656
August     160573   12014
December    98493     196
February     1420   94283
January     80903  113377
July       151209   10570
June        95443     327
March       99971     297
May        139731    7993
November    95188     253
October     99394     290
September   96945     234
"""