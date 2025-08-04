import matplotlib.pyplot as plt
import numpy as np

# Data
years = ["2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", 
         "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "Jan - Nov 2023"]
retail_sales = [4.2, 4.7, 5.1, 5.8, 6.6, 7.7, 9.1, 11.1, 12.8, 15.2, 18.0, 20.6, 23.2, 25.9, 28.7, 31.6, 
                34.7, 37.8, 40.8, 39.2, 44.1, 44.0, 42.8]
growth_rate = [0, 11.6, 8.9, 13.1, 14.6, 15.5, 18.0, 22.5, 15.6, 18.5, 18.2, 14.3, 13.0, 11.7, 10.4, 10.2, 
               10.0, 8.8, 8.0, -3.9, 12.5, -0.2, -0.5]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 7))

# Draw a bar chart of total retail sales of consumer goods
ax1.bar(x, retail_sales, color='orange', label='Total Retail Sales of Consumer Goods (Trillion Yuan)')
ax1.set_ylabel('Total Retail Sales of Consumer Goods (Trillion Yuan)')
ax1.set_xlabel('Year')
ax1.set_xticks(x)
ax1.set_xticklabels(years, rotation=45, ha='right')
ax1.legend(loc='upper left')

# Create a secondary y - axis and draw a line chart of year - on - year growth
ax2 = ax1.twinx()
ax2.plot(x, growth_rate, marker='o', color='brown', label='Year - on - Year Growth (%)', linewidth=2)
ax2.set_ylabel('Year - on - Year Growth (%)')
ax2.legend(loc='center right')

# Add value labels for total retail sales of consumer goods
for i, sales in enumerate(retail_sales):
    ax1.text(i, sales + 0.5, f'{sales}', ha='center', va='bottom')

# Add value labels for year - on - year growth
for i, rate in enumerate(growth_rate):
    ax2.text(i, rate + 0.5, f'{rate}%', ha='center', va='bottom')

ax1.set_title('Total Retail Sales of Consumer Goods and Growth Rate in China from 2001 to First 11 Months of 2023')

plt.tight_layout()
plt.show()