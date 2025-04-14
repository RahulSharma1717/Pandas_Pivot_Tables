# Find the most expensive purchase amount for each product type.

import pandas as pd

df = pd.read_csv('retail_data.csv')
#pd.set_option('display.max_columns', None)

pivot_table = df.pivot_table(index='Product_Type', values='Amount', aggfunc='max')
print(pivot_table)


"""Output:
                                        Amount
Product_Type                                  
Bathroom                            499.968673
Bedding                             499.963011
BlueStar AC                         499.863784
Children's                          499.916128
Chocolate                           499.989331
Coffee                              499.894725
Decorations                         499.975680
Dress                               499.886695
Fiction                             499.993884
Fridge                              499.780098
Furniture                           499.966831
Headphones                          499.863222
Jacket                              499.934010
Jeans                               499.728422
Juice                               499.971297
Kitchen                             499.996681
Laptop                              499.989082
Lighting                            499.971256
Literature                          499.975499
Mitsubishi 1.5 Ton 3 Star Split AC  499.971872
Non-Fiction                         499.997024
Shirt                               499.988382
Shoes                               499.976353
Shorts                              499.905745
Smartphone                          499.965071
Snacks                              499.397907
Soft Drink                          499.948541
T-shirt                             499.872190
Tablet                              499.967846
Television                          499.995511
Thriller                            499.973765
Tools                               499.966177
Water                               499.997911
"""