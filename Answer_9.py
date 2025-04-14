# Find the average revenue from each city and segment.

import pandas as pd

df = pd.read_csv('retail_data.csv')
#pd.set_option('display.max_columns', None)

pivot_table = df.pivot_table(index='City', columns='Customer_Segment', values='Total_Amount', aggfunc='mean')
print(pivot_table)


"""Output:
Customer_Segment          New      Premium      Regular
City                                                   
Adelaide          1369.313135  1341.971086  1375.674019
Albuquerque       1422.536802  1283.270134  1422.539740
Albury-Wodonga    1338.948198  1355.163718  1400.024683
Arlington         1461.008394  1351.804828  1374.576625
Atlanta           1366.889174  1336.929332  1519.515216
...                       ...          ...          ...
Wichita           1350.645689  1455.371135  1412.965164
Windsor           1391.934619  1365.263345  1393.146160
Winnipeg          1378.766203  1274.070543  1352.827470
Wollongong        1472.783467  1392.782376  1357.131103
Wuppertal         1366.524067  1372.380386  1384.728925

[130 rows x 3 columns]
"""