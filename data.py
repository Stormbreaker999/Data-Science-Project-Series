#Required Modules
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

stock_data=pd.read_csv("infolimpioavanzadoTarget.csv")
#print(stock_data.head())
# for col in stock_data.columns:
#     print(stock_data[col].value_counts())
#print(stock_data['TARGET'].head(50))
#print(stock_data.isnull().sum())
column_set=[]
for i in stock_data.columns:
    if stock_data[i].isnull().sum()<100:
        column_set.append(i)
my_data=stock_data[[col for col in column_set]]
print(my_data.shape)
print(my_data.head())
#print(my_data.isnull().sum())
#checking still null columns
# for i in my_data.columns:
#     if my_data[i].isnull().sum():
#         print(i, my_data[i].isnull().sum())

plt.scatter(y=my_data["close"][:1000], x=my_data["open"][:1000])
plt.show()

cnt=0
for i in my_data['open']:
    if(i<100):
        cnt+=1
print(cnt)


