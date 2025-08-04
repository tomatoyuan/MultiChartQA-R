import matplotlib.pyplot as plt
import numpy as np

# Data
years = ['2021', '2022', '2026E']
values = [64416, 69700.8, 93311.9]
x = np.arange(len(years))

# Create the chart
fig, ax = plt.subplots(figsize=(8, 6))

# Bar chart
bars = ax.bar(x, values, color='#00d2c8', width=0.5, label='Market Size (Billion Yuan)')

# Add value labels
for i, v in enumerate(values):
    ax.text(x[i], v + 2000, f'{v}', ha='center', va='bottom', fontsize=10)

# Add CAGR annotation
ax.annotate('CAGR = 7.6%',
            xy=(0, values[0] + 10000), xytext=(0.6, values[2] + 8000),
            textcoords='data',
            fontsize=13, color='#00d2c8', fontweight='bold')

# Axes settings
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=11)
ax.set_ylim(0, 105000)
ax.set_ylabel('Unit: Billion Yuan', fontsize=12)
ax.set_title('Global Immunity - Boosting Food Market', fontsize=14, fontweight='bold', pad=20)

# Legend
ax.legend(loc='upper left', fontsize=10)

# Grid lines
ax.yaxis.grid(True, linestyle='--', alpha=0.3)

# Beautify the border
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.tight_layout()
plt.show()