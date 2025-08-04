import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['2302', '2303', '2304', '2305', '2306', '2307', '2308', '2309',
          '2310', '2311', '2312', '2402', '2403']
x = np.arange(len(months))

social_retail_yoy = [3.5, 10.6, 18.4, 12.7, 3.1, 2.5, 4.6, 5.5, 7.6, 10.1, 7.4, 5.5, 3.1]
network_retail_yoy = [5.3, 7.3, 10.4, 11.8, 10.8, 10.0, 9.5, 8.9, 8.4, 8.3, 8.4, 14.4, 11.6]

# Canvas
plt.figure(figsize=(12, 6))

# Line chart
plt.plot(x, social_retail_yoy, marker='o', label='Social Retail YoY', color='#1976d2', linewidth=2)
plt.plot(x, network_retail_yoy, marker='s', label='Accumulated YoY of Physical Goods Online Retail', color='#26a69a', linewidth=2)

# Add data labels
for i, (y1, y2) in enumerate(zip(social_retail_yoy, network_retail_yoy)):
    plt.text(x[i], y1 + 0.7, f'{y1:.1f}%', ha='center', fontsize=9, color='#1976d2')
    plt.text(x[i], y2 - 1.2, f'{y2:.1f}%', ha='center', fontsize=9, color='#26a69a')

# Set axes and title
plt.xticks(x, months)
plt.ylabel('Year-on-Year Growth Rate (%)')
plt.title('Social Retail and Online Retail Trends, 202301 - 202403')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()

# Add data source and description
plt.figtext(0.01, 0, "Data Source: Magic Mirror Insights; Sina Finance\nData Description: Online retail YoY is the year-on-year growth of the accumulated value up to the current month;",
            ha='left', fontsize=9, linespacing=1.5)

plt.tight_layout()
plt.subplots_adjust(bottom=0.2)
plt.ylim(2, 20)
plt.show()