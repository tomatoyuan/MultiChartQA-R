import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['MAT TY', 'YTD TY', 'Jan', 'Feb']
values_2023 = [-3.3, 2.1, 16.0, -10.4]
values_2024 = [-3.5, -5.6, -22.5, 14.2]

x = np.arange(len(labels))  # X-axis positions
width = 0.35  # Bar width

# Create figure and axes
fig, ax = plt.subplots(figsize=(8, 6))

# Draw bar chart
bars1 = ax.bar(x - width / 2, values_2023, width, label='2023', color='#A9C6FB')  # Light blue
bars2 = ax.bar(x + width / 2, values_2024, width, label='2024', color='#1346D3')  # Dark blue

# Add percentage text
for i in range(len(labels)):
    ax.text(x[i] - width / 2, values_2023[i] + (0.8 if values_2023[i] >= 0 else -2),
            f'{values_2023[i]}%', ha='center', va='bottom' if values_2023[i] >= 0 else 'top',
            fontsize=10, color='red' if values_2023[i] < 0 else 'black')
    ax.text(x[i] + width / 2, values_2024[i] + (0.8 if values_2024[i] >= 0 else -2),
            f'{values_2024[i]}%', ha='center', va='bottom' if values_2024[i] >= 0 else 'top',
            fontsize=10, color='red' if values_2024[i] < 0 else 'black')

# Add dividing line
ax.axvline(x=1.5, color='gray', linestyle='--', linewidth=1)

# Beautify the chart
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_title('YoY Growth Rate of FMCG Offline Sales %', fontsize=14, weight='bold')
ax.legend(loc='upper left')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add data source description
plt.figtext(0.5, -0.05, 'Note: The scope is 79 Offline categories (baby store excluded), Feb\'24',
            wrap=True, horizontalalignment='center', fontsize=9, color='gray')
plt.ylim(-27.5,20)
plt.tight_layout()
plt.show()