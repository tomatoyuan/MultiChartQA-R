import matplotlib.pyplot as plt
import numpy as np

# Data
years = ['As of Dec 2022', 'As of Dec 2023']
population = [52000, 54800]  # Unit: 10,000
penetration_rate = [48.8, 49.9]  # Unit: %

# Set the canvas
fig, ax1 = plt.subplots(figsize=(7, 4))

# Draw the bar chart: Population (left - axis)
bar_width = 0.4
x = np.arange(len(years))
bars = ax1.bar(x, population, bar_width, color='#4CAF50', label='Population (10,000)')
ax1.set_ylabel('Population (10,000)', fontsize=12)
ax1.set_ylim(50000, 56000)
ax1.set_xticks(x)
ax1.set_xticklabels(years, fontsize=11)
ax1.tick_params(axis='y', labelsize=10)

# Add value labels to the bar chart
for i, v in enumerate(population):
    ax1.text(i, v + 200, f"{v}", ha='center', va='bottom', fontsize=10)

# Set the second axis: Penetration rate (right - axis)
ax2 = ax1.twinx()
ax2.plot(x, penetration_rate, color='blue', marker='o', linewidth=2.5, label='Penetration rate (%)')
ax2.set_ylabel('Penetration rate among all Internet users (%)', fontsize=12)
ax2.set_ylim(48.25, 50.50)
ax2.tick_params(axis='y', labelsize=10)

# Add penetration rate value labels
for i, v in enumerate(penetration_rate):
    ax2.text(i, v - 0.2, f"{v}%", color='blue', ha='center', va='bottom', fontsize=15, fontweight='bold')

# Title and legend
plt.title('Statistics of the scale and penetration rate of online food delivery users', fontsize=14, pad=40)
fig.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=2, fontsize=10)

# Data source annotation

plt.tight_layout()
plt.show()