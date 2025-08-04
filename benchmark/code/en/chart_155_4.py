# Re-import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm



# Data
months = [f'{i}月, 2022' for i in range(1, 13)] + [f'{i}月, 2023' for i in range(1, 13)]
douyin_scale = [1.2, 1.7, 1.5, 2.5, 1.8, 1.7, 1.5, 2.1, 2.4, 2.6, 2.9, 3.1, 2.0, 2.3, 2.8, 2.7, 2.6, 2.5, 2.9, 3.2, 3.3, 3.1, 3.5, 3.4]
kuaishou_scale = [1.0, 1.2, 2.1, 1.6, 1.3, 1.1, 1.4, 1.8, 2.0, 2.3, 2.6, 3.0, 2.5, 2.7, 3.1, 3.5, 3.0, 3.2, 3.6, 3.9, 4.1, 4.0, 4.3, 4.5]
douyin_growth = [500, 800, 400, 600, 350, 300, 200, 150, 100, 90, 80, 75, 50, 40, 30, 25, 20, 10, 15, 5, 8, 6, 4, 3]
kuaishou_growth = [200, 250, 300, 220, 180, 160, 140, 100, 80, 60, 50, 40, 30, 25, 20, 18, 15, 10, 8, 6, 5, 3, 2, 1]

x = np.arange(len(months))
width = 0.35

fig, ax1 = plt.subplots(figsize=(14, 6))

# Industry scale bar chart
bar1 = ax1.bar(x - width/2, douyin_scale, width=width, label='Douyin Industry Scale (Billion)', color='#b6d957')
bar2 = ax1.bar(x + width/2, kuaishou_scale, width=width, label='Kuaishou Industry Scale (Billion)', color='#f6c7b6')
ax1.set_ylabel('Industry Scale (Billion)')
ax1.set_ylim(0, 7)

# Label bar chart data
for rect in bar1:
    height = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width()/2, height + 0.1, f'{height:.1f}', ha='center', va='bottom', fontsize=7, color='#4b830d', fontweight='bold')

for rect in bar2:
    height = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width()/2, height + 0.1, f'{height:.1f}', ha='center', va='bottom', fontsize=7, color='#a8431b', fontweight='bold')

# Year-on-year growth line chart
ax2 = ax1.twinx()
douyin_line = ax2.plot(x, douyin_growth, color='red', label='Douyin Year-on-Year Growth', linewidth=2, marker='o')
kuaishou_line = ax2.plot(x, kuaishou_growth, color='steelblue', label='Kuaishou Year-on-Year Growth', linewidth=2, marker='s')
ax2.set_ylabel('Year-on-Year Growth (%)')
ax2.set_ylim(-100, 850)

# Label line chart data
for i, val in enumerate(douyin_growth):
    ax2.text(x[i], val + 20, f'{val}', color='red', fontsize=7, ha='center')

for i, val in enumerate(kuaishou_growth):
    ax2.text(x[i], val + 20, f'{val}', color='steelblue', fontsize=7, ha='center')

# X-axis labels
ax1.set_xticks(x)
ax1.set_xticklabels(months, rotation=45, ha='right', fontsize=8)

# Combine legends
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='best', fontsize=9)

# Title
plt.title('Overview of Douyin and Kuaishou Big Health Market Sales from 2022 to 2023', fontsize=14, weight='bold')

plt.tight_layout()
plt.show()