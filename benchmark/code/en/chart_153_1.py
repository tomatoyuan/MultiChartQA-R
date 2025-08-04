# Chart 1: Changes in keyword search note data (Dual - axis with bar chart + line chart)
import matplotlib.pyplot as plt
import numpy as np

# Data definition
categories = ["Pore discussion questions", "Total volume of topics about large pores", "Pore care"]
old_values = [43.65, 8.7, 0.16]
new_values = [79.06, 17.95, 0.39]
growth_rates = [81.12, 106.32, 143.75]

x = np.arange(len(categories))
width = 0.35

fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar chart
bars1 = ax1.bar(x - width/2, old_values, width, label='2022/08 - 2023/07', color='#c5d9de')
bars2 = ax1.bar(x + width/2, new_values, width, label='2023/08 - 2024/07', color='#355c5c')
ax1.set_ylabel('Number of search notes (in ten thousands)')
ax1.set_xticks(x)
ax1.set_xticklabels(categories, fontsize=10)
ax1.legend(loc='best')

# Add values on top of the bars
for bar in bars1 + bars2:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, height + 1, f'{height:.2f}',
             ha='center', va='bottom', fontsize=9)

# Line chart
ax2 = ax1.twinx()
ax2.plot(x, growth_rates, color='gray', marker='o', label='Year - on - year growth rate')
for i, rate in enumerate(growth_rates):
    ax2.text(x[i], rate + 3, f'{rate:.2f}%', color='black', ha='center', fontsize=9)
ax2.set_ylabel('Year - on - year growth rate (%)')
ax2.set_ylim(0, 180)

# Title and beautification
plt.title("Figure 1.1 - 1 Xiaohongshu keyword search note data (Data source: Feigua)")
plt.tight_layout()
plt.show()