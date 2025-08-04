import matplotlib.pyplot as plt
import numpy as np

# Data
years = ['2022', '2028E']
values = [449.25, 607.95]
x = np.arange(len(years))

# Create a chart
fig, ax = plt.subplots(figsize=(7, 6))

# Bar chart
bars = ax.bar(x, values, color='#00d2c8', width=0.5, label='Market Size (Billion Yuan)')

# Add top value labels
for i, v in enumerate(values):
    ax.text(x[i] - 0.1, v + 15, f'{v}', ha='center', va='bottom', fontsize=10)

# Add CAGR annotation
ax.annotate('CAGR = 5.17%',
            xy=(x[0], values[0] + 25), xytext=(x[1], values[1] + 25),
            textcoords='data',
            arrowprops=dict(arrowstyle='-', linestyle='dotted', color='#00d2c8', linewidth=2),
            fontsize=13, color='#00d2c8', fontweight='bold')

# Axis settings
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=11)
ax.set_ylim(0, 700)
ax.set_ylabel('Unit: Billion Yuan', fontsize=12)
ax.set_title('Global Sweetener Market Size', fontsize=14, fontweight='bold', pad=20)

# Legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.08), frameon=False, fontsize=10)

# Beautify
ax.yaxis.grid(True, linestyle='--', alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout(rect=[0, 0.05, 1, 1])  # Leave space for the legend
plt.show()