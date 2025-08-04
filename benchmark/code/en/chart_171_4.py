import matplotlib.pyplot as plt
import numpy as np

# Data
price_bands = ['Below 50 yuan', '50 - 100 yuan', '100 - 300 yuan', 'Above 300 yuan']
value_2022 = [0.30, 0.28, 0.27, 0.15]
value_2023 = [v + d for v, d in zip(value_2022, [0.09, -0.01, -0.03, -0.04])]
value_change = ['+9%', '-1%', '-3%', '-4%']

# Plotting
fig, ax = plt.subplots(figsize=(7, 5))
y = np.arange(len(price_bands))
bar_height = 0.35

# Bar chart
ax.barh(y - bar_height / 2, value_2022, height=bar_height, color='#e55322', label='2022H2')
ax.barh(y + bar_height / 2, value_2023, height=bar_height, color='black', label='2023H2')

# Value annotation
for i in range(len(price_bands)):
    ax.text(value_2022[i] + 0.005, y[i] - bar_height / 2,
            f'{int(value_2022[i]*100)}%', va='center', ha='left', fontsize=9,
            color='white' if value_2022[i] > 0.3 else 'black')
    ax.text(value_2023[i] + 0.005, y[i] + bar_height / 2,
            f'{int(value_2023[i]*100)}%', va='center', ha='left', fontsize=9,
            color='white' if value_2023[i] > 0.3 else 'black')
    ax.text(max(value_2022[i], value_2023[i]) + 0.03, y[i],
            value_change[i], va='center', fontsize=10)

# Style
ax.set_title('Sales revenue proportion change in each price band\n(2023H2 YoY / Douyin Fashion and Footwear)', fontsize=12)
ax.set_yticks(y)
ax.set_yticklabels(price_bands, fontsize=11)
ax.set_xlim(0, max(value_2022) + 0.2)
ax.invert_yaxis()
ax.legend(loc='lower right', fontsize=9)
ax.xaxis.grid(True, linestyle='--', alpha=0.3)

# Data source
fig.text(0.01, 0.01,
         'Data source: Youmi Youshu New E - commerce Marketing Big Data Analysis Platform. Statistics time: 2022.6.1–12.31, 2023.6.1–12.31',
         ha='left', va='bottom', fontsize=9)

plt.tight_layout(rect=[0, 0.03, 1, 1])
plt.show()