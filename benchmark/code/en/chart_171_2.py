import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# Data
months = ['Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
data_2022 = [87, 100, 96, 88, 92, 91, 98]  # Constructed numerical values
growth = [0.13, 0.0, 0.04, 0.32, 0.30, 0.26, 0.02]
data_2023 = [data_2022[i] * (1 + growth[i]) for i in range(len(data_2022))]

x = np.arange(len(months))
width = 0.35

# Create the chart
fig, ax = plt.subplots(figsize=(10, 6))

# Draw the bar chart
bars_2022 = ax.bar(x - width/2, data_2022, width, label='H2 2022', color='#e55322')
bars_2023 = ax.bar(x + width/2, data_2023, width, label='H2 2023', color='black')

# Add numerical annotations (2022 and 2023)
for i in range(len(x)):
    # Inside annotation for 2022 bars
    ax.text(x[i] - width/2, data_2022[i] - 3,
            f'{int(data_2022[i])}', ha='center', va='top', fontsize=10, color='white')

    # Outside annotation on top of 2023 bars
    ax.text(x[i] + width/2, data_2023[i] + 4,
            f'{int(data_2023[i])}', ha='center', va='bottom', fontsize=10, color='black')

# Add growth rate annotations (slightly shifted up)
for i, (x_pos, val) in enumerate(zip(x, data_2023)):
    ax.text(x_pos + width/2, val + 8,
            f'+{int(growth[i]*100)}%', ha='center', va='bottom', fontsize=9, color='gray')

# Axes and labels
ax.set_xticks(x)
ax.set_xticklabels(months, fontsize=11)
ax.set_ylabel('Monthly sales (relative value)', fontsize=12)
ax.set_ylim(0, 140)
plt.title('Monthly sales & year - on - year growth rate (H2 2023 yoy / Douyin clothing, shoes and bags)', fontsize=14, pad=20)

# Legend
ax.legend(loc='upper left', fontsize=10)

# Dashed box to highlight Sep - Nov
highlight_start = x[3] - width*1.5
highlight_width = (x[5] - x[3]) + width*3
rect = patches.Rectangle(
    (highlight_start, 0), highlight_width, max(data_2023)*1.1,
    linewidth=1.5, edgecolor='#e55322', linestyle='--', facecolor='none'
)
ax.add_patch(rect)

# Data source annotation
fig.text(0.01, 0.01,
         'Data source: Youmi YouShu New E - commerce Marketing Big Data Analysis Platform. Statistical time: Jun 1, 2022 - Dec 31, 2022; Jun 1, 2023 - Dec 31, 2023',
         ha='left', va='bottom', fontsize=9)

# Grid
ax.yaxis.grid(True, linestyle='--', alpha=0.3)
ax.set_axisbelow(True)

plt.tight_layout(rect=[0, 0.03, 1, 1])

plt.show()