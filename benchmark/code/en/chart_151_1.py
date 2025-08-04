import matplotlib.pyplot as plt
import numpy as np

# Chart 1: MAT2406 Online FMCG and Growth Rates of Each Category (Using Bar Chart)
categories = ['Online Retail', 'Online FMCG', 'Food', 'Beauty', 'Maternity & Baby']
growth = [4.9, 7.8, 8.1, 5.8, 10.2]
colors = ['black', '#0056d6', 'white', 'white', 'white']
edgecolors = ['black', '#0056d6', '#0056d6', '#0056d6', '#0056d6']

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(categories, growth, color=colors, edgecolor=edgecolors, linewidth=2)

# Add numerical labels
for bar, value in zip(bars, growth):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 0.3, f'{value}%', ha='center', va='bottom', fontsize=12)

# Set the title and Y - axis label
ax.set_title('MAT2406 Online FMCG and Growth Rates of Each Category', fontsize=16)
ax.set_ylabel('Year - on - Year Growth Rate (%)')
ax.set_ylim(0, 12)
ax.set_facecolor('#f8f9fa')

plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()