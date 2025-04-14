# Find the minimum revenue for each product brand and order status.

import pandas as pd

df = pd.read_csv('retail_data.csv')
#pd.set_option('display.max_columns', None)

pivot_table = df.pivot_table(index='Product_Brand', columns='Order_Status', values='Total_Amount', aggfunc='min')
print(pivot_table)


"""Output:
Order_Status       Delivered     Pending  Processing    Shipped
Product_Brand                                                  
Adidas             10.484693   11.558308   13.318187  13.267327
Apple              11.696255   11.288107   10.928036  13.992273
Bed Bath & Beyond  10.362214   11.892097   11.035773  11.383778
BlueStar           10.312626         NaN         NaN        NaN
Coca-Cola          10.382533   13.914545   11.927405  11.392996
HarperCollins      10.304855   12.472113   11.333472  10.288169
Home Depot         10.198830   10.573064   12.494869  10.068154
IKEA               11.044818   13.457616   12.371498  12.115942
Mitsubhisi         10.800385  110.733110   15.309442  34.552923
Nestle             10.761919   12.512199   10.056353  10.947367
Nike               10.648666   12.162504   10.578870  10.601896
Penguin Books      10.226839   10.572502   10.707279  10.133500
Pepsi              10.092966   10.231967   10.304530  10.003750
Random House       10.934673   13.717490   10.172078  10.510516
Samsung            10.566244   12.491820   10.523771  11.536797
Sony               10.063269   11.832873   11.509879  10.831884
Whirepool          10.011336         NaN         NaN        NaN
Zara               11.548863   10.295241   11.218513  10.783579"""