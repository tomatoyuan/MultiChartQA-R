import matplotlib.pyplot as plt
import numpy as np

# Year data
years = np.arange(2015, 2025)  
# Total retail sales of consumer goods corresponding to each year (in billions of yuan). The data is roughly estimated based on the chart and can be replaced accurately as needed.
retail_sales = [290000, 310000, 340000, 370000, 400000, 390000, 430000, 435000, 460000, 480000]  

# Create a canvas and sub - plot
fig, ax = plt.subplots()

# Draw a bar chart
bars = ax.bar(years, retail_sales, color='cyan', label='Total Retail Sales')  

# Calculate the trend line
z = np.polyfit(years, retail_sales, 1)
p = np.poly1d(z)
ax.plot(years, p(years), 'blue', label='Trend Line')  

# Set the x - axis ticks to display years
plt.xticks(years)  

# Add data labels
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 1000,
            f'{height}',
            ha='center', va='bottom', rotation=0)

# Add a title and axis labels
ax.set_title('Trend of Total Retail Sales of Consumer Goods in China from 2015 to 2024 (in billions of yuan)')
ax.set_xlabel('Year')
ax.set_ylabel('Total Retail Sales (in billions of yuan)')

# Add a legend
ax.legend()  

# Display the chart
plt.show()