import matplotlib.pyplot as plt
import numpy as np

# Data
price_bands = ['Below 50 yuan', '50 - 100 yuan', '100 - 300 yuan', 'Over 300 yuan']
volume_2022 = [0.38, 0.25, 0.22, 0.15]
volume_2023 = [v + d for v, d in zip(volume_2022, [0.12, -0.06, -0.05, -0.01])]
volume_change = ['+12%', '-6%', '-5%', '-1%']

# Plotting
fig, ax = plt.subplots(figsize=(7, 5))
y = np.arange(len(price_bands))
bar_height = 0.35

# Bar chart
ax.barh(y - bar_height / 2, volume_2022, height=bar_height, color='#e55322', label='2022H2')
ax.barh(y + bar_height / 2, volume_2023, height=bar_height, color='black', label='2023H2')

# Value annotation
for i in range(len(price_bands)):
    ax.text(volume_2022[i] + 0.005, y[i] - bar_height / 2,
            f'{int(volume_2022[i]*100)}%', va='center', ha='left', fontsize=9,
            color='white' if volume_2022[i] > 0.3 else 'black')
    ax.text(volume_2023[i] + 0.005, y[i] + bar_height / 2,
            f'{int(volume_2023[i]*100)}%', va='center', ha='left', fontsize=9,
            color='white' if volume_2023[i] > 0.3 else 'black')
    ax.text(max(volume_2022[i], volume_2023[i]) + 0.03, y[i],
            volume_change[i], va='center', fontsize=10)

# Style
ax.set_title('Change in sales volume share by price band\n (H2 2023 YoY / Douyin apparel, shoes and bags)', fontsize=12)
ax.set_yticks(y)
ax.set_yticklabels(price_bands, fontsize=11)
ax.set_xlim(0, max(volume_2023) + 0.2)
ax.invert_yaxis()
ax.legend(loc='lower right', fontsize=9)
ax.xaxis.grid(True, linestyle='--', alpha=0.3)

# Data source
fig.text(0.01, -0.01,
         'Data source: Youmi Youshu New E - commerce Marketing Big Data Analysis Platform.\n Statistics time: 2022.6.1–12.31, 2023.6.1–12.31',
         ha='left', va='bottom', fontsize=9)

plt.tight_layout(rect=[0, 0.03, 1, 1])
plt.show()