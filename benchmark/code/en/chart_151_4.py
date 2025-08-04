import numpy as np
import matplotlib.pyplot as plt

# Data
periods = ['MAT2206', 'MAT2306', 'MAT2406']
sales = [100, 110, 115]
avg_price = [150, 145, 155]

x = np.arange(len(periods))

fig, ax1 = plt.subplots(figsize=(8, 5))

# Bar chart: Sales
bars = ax1.bar(x, sales, width=0.4, color='lightgray', label='Sales')
ax1.set_ylabel('Sales (Million Yuan)', fontsize=11)
ax1.set_ylim(0, 160)

# Add value labels on top of the bars
for i, bar in enumerate(bars):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, height + 3, f'{sales[i]}',
             ha='center', va='bottom', fontsize=9)

# Line chart: Average price
ax2 = ax1.twinx()
line, = ax2.plot(x, avg_price, color='blue', marker='o', linewidth=2, label='Average Price')
ax2.set_ylabel('Average Price (Yuan)', fontsize=11)
ax2.set_ylim(60, 160)

# Label values on the line
for i, price in enumerate(avg_price):
    ax2.text(x[i], price + 3, f'{price}', ha='center', va='bottom', fontsize=9, color='blue')

# Annotation arrow (trend)
ax2.annotate('', xy=(2, avg_price[2]), xytext=(1, avg_price[1]),
             arrowprops=dict(arrowstyle='->', color='green', lw=2))

# Set X-axis
ax1.set_xticks(x)
ax1.set_xticklabels(periods, fontsize=11)

# Title
plt.title("Overall Online | Probiotic Sales (Million Yuan) and Average Price (Yuan)", fontsize=13)

# Combine legends
lines = [bars, line]
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', fontsize=10)

plt.ylim(0, 190)

plt.tight_layout()
plt.show()