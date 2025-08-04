import matplotlib.pyplot as plt
import numpy as np

# Data
years = ['2020', '2021', '2022', '2023']
total_retail = [390000, 440000, 440000, 470000]  # Total retail sales of consumer goods (100 million yuan)
online_retail = [110000, 120000, 120000, 130000]  # Online retail sales of physical goods (100 million yuan)
total_growth = [-0.04, 0.12, 0.00, 0.07]  # Year - on - year growth rate
online_growth = [0.14, 0.11, 0.11, 0.08]

x = np.arange(len(years))
width = 0.35

# Create a figure
fig, ax1 = plt.subplots(figsize=(10, 6))
ax2 = ax1.twinx()

# Bar chart
bar1 = ax1.bar(x - width/2, total_retail, width, label='Total retail sales of consumer goods (100 million yuan)', color='#e55322')
bar2 = ax1.bar(x + width/2, online_retail, width, label='Online retail sales of physical goods (100 million yuan)', color='lightgray')

# Data labels for bar chart
for i, rect in enumerate(bar1):
    height = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width()/2, height + 1000, f'{height}', ha='center', va='bottom', fontsize=9)

for i, rect in enumerate(bar2):
    height = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width()/2, height + 1000, f'{height}', ha='center', va='bottom', fontsize=9)

# Line chart
line1 = ax2.plot(x, total_growth, label='Year - on - year growth rate of total retail sales of consumer goods', color='black', marker='o', linewidth=2)
line2 = ax2.plot(x, online_growth, label='Year - on - year growth rate of online retail sales of physical goods', color='#7f3f1d', marker='o', linewidth=2)

# Growth rate labels
for i, v in enumerate(total_growth):
    ax2.text(x[i] + 0.1, v, f'{int(v * 100)}%', ha='center', va='bottom', fontsize=10)

for i, v in enumerate(online_growth):
    ax2.text(x[i] - 0.1, v - 0.01, f'{int(v * 100)}%', ha='center', va='bottom', fontsize=10)

# Axes and legend
ax1.set_ylabel('Amount (100 million yuan)', fontsize=12)
ax2.set_ylabel('Year - on - year growth rate', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(years, fontsize=11)
plt.title('Current value of total retail sales of consumer goods \n& current value of online retail sales of physical goods (million yuan)', fontsize=16, pad=20)
fig.legend(loc='upper center', bbox_to_anchor=(0.5, -0.08), ncol=2, frameon=False, fontsize=10)

# Grid and background
ax1.yaxis.grid(True, linestyle='--', alpha=0.4)
ax2.set_ylim(-0.05, 0.20)
ax1.set_facecolor('white')

# Data source (placed outside at the bottom using fig.text)
fig.text(0.01, 0.01, 'Data source: National Bureau of Statistics. Plotted by Youmiyun Content Center', ha='left', va='bottom', fontsize=9)

plt.tight_layout(rect=[0, 0.03, 1, 1])  # Make space for the bottom text
plt.show()