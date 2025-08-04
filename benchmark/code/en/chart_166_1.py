import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Skin Care', 'Makeup', 'Personal Care', 'Perfume']
market_scale = [4823.5, 1700.9, 1193.5, 254]
growth_rate = [0.1, 13.5, 15.8, 11.4]

x = np.arange(len(categories))
width = 0.4

fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar chart: Market scale
bars = ax1.bar(x, market_scale, width, color='#FFB6C1', label='Market Scale (Billion Yuan)')
ax1.set_ylabel('Market Scale (Billion Yuan)')
ax1.set_xticks(x)
ax1.set_xticklabels(categories)
ax1.bar_label(bars, fmt='%.1f', label_type='edge', fontsize=10, color='crimson')
ax1.set_ylim(0, 5500)

# Line chart: Year - on - year growth rate
ax2 = ax1.twinx()
line = ax2.plot(x, growth_rate, color='gray', marker='o', label='YoY Market Scale Growth', linewidth=2)
ax2.set_ylabel('Year - on - year Growth Rate (%)')
ax2.set_ylim(0, 18)
for i, val in enumerate(growth_rate):
    ax2.text(x[i], val + 0.8, f'{val:.1f}%', ha='center', fontsize=10, weight='bold')

# Set the title and add spacing to prevent overlap
plt.title('Market Scale of Each Primary Category in 2023', fontsize=14, pad=20)

# Combine legends
handles = list(bars)[:1] + line  # Take only one bar as a representative + line
labels = ['Market Scale (Billion Yuan)', 'YoY Market Scale Growth']
ax1.legend(handles, labels, loc='upper right', fontsize=10)

# Add data source
plt.figtext(0.01, -0.05, 'Data Source: CBNData', fontsize=10, ha='left')

plt.tight_layout()
plt.show()