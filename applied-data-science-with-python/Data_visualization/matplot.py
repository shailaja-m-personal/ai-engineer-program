import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  # type: ignore[reportMissingModuleSource]

df = pd.read_csv('tips.csv')
# print(df.head(10))

data = df.groupby('day', as_index=False).agg({'total_bill': 'sum'})
# print(data)

# plt.plot(data['day'], data['total_bill']) # 'r' is the color red
# plt.xlabel('Day')
# plt.ylabel('Total Bill')
# plt.title('Total Bill by Day')
# plt.show()

# plt.plot(data['day'], data['total_bill'],
#          color = 'orange',
#          linestyle = 'dashdot',
#          linewidth = 1,
#          marker = '8',
#          markerfacecolor = 'k',
#          markersize = 10,
# )
# plt.xlabel('Days', color = 'blue', size = 20)
# plt.ylabel('Sales')
# plt.title('Sales per day', size = 30, color = 'red')
# plt.show()

#Plotting 2 lines and Customizing the graph
year = [2022, 2023, 2024, 2025, 2026]
product_1_sales = [100, 105, 102, 90, 150]
product_2_sales = [90, 95, 100, 110, 120]
#line 1
# plt.plot(year, product_1_sales,
#          color = 'greenyellow',
#          label = 'Product 1',
#          linewidth = 2,
#          marker = 'p',
#          markerfacecolor = 'black',
#          markersize = 10
#          )
# #line 2
# plt.plot(year, product_2_sales, 'b*-', # b*- is the color blue with star marker and solid line
#          label = 'Product 2',
#          markersize = 10,
#          linewidth = 1,
#          markerfacecolor = 'red',
#          markeredgecolor = 'black',
#          markeredgewidth = 2
#          )
# plt.xticks(ticks = year)
# plt.ylabel('Sales')
# plt.xlabel('Year')
# plt.title('Product Sales Over Time', size = 12)
# plt.legend()
# plt.show()

# #Scatter plot
# plt.scatter(df['total_bill'],
#             df['tip'],
#             label = 'bill vs tip',
#             marker = 'o',
#             edgecolor = 'black',
#             color = 'red',
#             s = 50,
#             alpha = 0.2)
# plt.xticks(ticks = range(1,55,3))
# plt.xlabel('Bill', color = 'blue', size = 10)
# plt.ylabel('Tip')
# plt.title('Graph title', color = 'green', size = 10)
# plt.legend()
# plt.show()

# plt.scatter(df['total_bill'],
#             df['size'],
#             label = 'bill vs family size',
#             marker = 'o',
#             edgecolor = 'black',
#             color = 'red',
#             s = 50,
#             alpha = 0.2)
# plt.xlabel('Bill', color = 'blue', size = 10)
# plt.ylabel('family size')
# plt.title('Graph title', color = 'green', size = 10)
# plt.legend()
# plt.show()

#correlation 
# df_dummy = pd.DataFrame({'savings' : [100, 500, 800, 1000],
#                          'Expend' : [8000, 6000, 2000, 100],
#                          'balance' : [200, 800, 1000, 1500]})
# print(df_dummy.corr())

# #bubble plot
# plt.scatter(df['total_bill'], df['tip'],
#             label = 'bill vs tip',
#             marker='o', edgecolors='black', color='gold',
#             alpha=0.5)
# plt.xlabel('total_bill', color = 'blue', size = 10)
# plt.ylabel('tip')
# plt.title('Bubble plot', color = 'green', size = 10)
# plt.legend()
# plt.show()

#Pie Chart
data = df.groupby('day', as_index=False).agg({'tip' : 'sum'})
# print(data)

# colors_we_want = ['#ff9999','#8ebfa4','#DBF7DA','#fcc996']
# plt.pie(data['tip'],
#         labels = data['day'],
#         colors = colors_we_want,
#         explode = (0,0,0,0.2),
#         autopct = '%1.1f%%',
#         counterclock=True,
#         startangle=90,
#         shadow=True,
#         radius=1,
#         textprops={'fontsize':10})
# plt.show()

#bar chart
data = df.groupby('day', as_index=False).agg({'size':'sum', 'tip':'sum'})
# # print(data)
# plt.bar(data['day'],
#         data['tip'],
#         label ='Sum_Tip_Amt',
#         width=0.5,
#         alpha=0.4,
#         edgecolor = 'black',
#         color = 'cyan')
# plt.xlabel('Day')
# plt.ylabel('Total No.of People')
# plt.legend()
# plt.show()

plt.figure(figsize=(7,5))

plt.bar(data['day'],
        data['tip'],
        label='Total tip ($)',
        color = 'skyblue',
        edgecolor='black')

plt.bar(data['day'],
        data['size'],
        label='No.of people',
        color = 'gold',
        edgecolor='black')

plt.xlabel('Day of the week', fontsize=12)
plt.yticks(range(1,500,20))
plt.ylabel('Value', fontsize=12)
plt.title('Stacked Bar Chart: No.of People and Tips by Day', fontsize=14)

plt.legend(title='Legend')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()
