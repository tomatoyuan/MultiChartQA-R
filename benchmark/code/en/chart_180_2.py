import matplotlib.pyplot as plt
import numpy as np

# Data
years = ['2022H1', '2023H1']
register_total = [883, 670]
register_new = [134, 358]
register_others = [register_total[i] - register_new[i] for i in range(2)]
record_total = [1481, 1937]

x = np.arange(len(years))  # x-axis positions
width = 0.35

fig, ax = plt.subplots(figsize=(8, 6))

# Registration part: Stacked bar chart
bar_others = ax.bar(x - width/2, register_others, width, label='Other Approvals', color='lightgray')
bar_new = ax.bar(x - width/2, register_new, width, bottom=register_others, label='New Product Approvals', color='blue')

# Label the total registration numbers (at the top)
for i in range(len(years)):
    ax.text(x[i] - width/2, register_total[i] + 30, str(register_total[i]),
            ha='center', va='bottom', fontsize=10)

for i in range(len(years)):
    ax.text(x[i] - width/2, register_others[i] + register_new[i] / 2,
            str(register_new[i]), ha='center', va='center', fontsize=9, color='white')

# Record part: Independent bar chart
bar_record = ax.bar(x + width/2, record_total, width, label='Records', color='skyblue')

# Label the record numbers
for i in range(len(years)):
    ax.text(x[i] + width/2, record_total[i] + 30, str(record_total[i]),
            ha='center', va='bottom', fontsize=10)

# Set axis labels and title
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.set_ylabel('Number of Approvals', fontsize=12)
ax.set_title('Comparison of Chinese Health Food Registration and Record in 2022H1 and 2023H1', fontsize=14, fontweight='bold')
ax.legend(loc='upper left')

# Data source description
plt.figtext(0.5, 0.01, 'Note: Import record products are not included in the record data.\nData Source: State Administration for Market Regulation',
            wrap=True, horizontalalignment='center', fontsize=9)

plt.tight_layout()
plt.show()