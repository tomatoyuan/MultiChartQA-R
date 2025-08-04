import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2019", "2020", "2021", "2022", "2023", "2024", "2025e", "2026e"]
# Premium income of each insurance type (in billions of yuan), the data is roughly simulated and can be adjusted according to actual situations
premium_data = np.array([
    [22754, 11649, 7066, 1000],    # 2019
    [23982, 11929, 8173, 1100],    # 2020
    [23572, 11671, 8447, 1200],    # 2021
    [24519, 12712, 8653, 1300],    # 2022
    [27646, 13607, 9035, 1400],    # 2023
    [31917, 14331, 9773, 1500],    # 2024
    [33736, 14918, 10174, 1600],   # 2025e
    [35659, 15530, 10591, 1700]    # 2026e
])

# Colors corresponding to each insurance type
colors = ['green', 'limegreen', 'mediumseagreen', 'lightseagreen']
# Insurance type names
insurance_types = ["Life Insurance (Billion Yuan)", "Property Insurance (Billion Yuan)", "Health Insurance (Billion Yuan)", "Accident Insurance (Billion Yuan)"]

x = np.arange(len(years))  # x-axis tick positions
bar_width = 0.6  # Bar width

fig, ax = plt.subplots(figsize=(14, 9))  # Further increase the chart size

# Draw a stacked bar chart
bottom = np.zeros(len(years))
for i in range(premium_data.shape[1]):
    bars = ax.bar(x, premium_data[:, i], width=bar_width, bottom=bottom, color=colors[i], label=insurance_types[i])
    bottom += premium_data[:, i]
    
    # Add data labels above each bar
    for j, bar in enumerate(bars):
        height = bar.get_height()
        if height > 500:  # Only show labels with sufficient height to avoid overcrowding
            ax.text(
                bar.get_x() + bar.get_width()/2., 
                bar.get_y() + height/2,
                f'{int(height)}',
                ha='center', va='center',
                color='black', fontsize=8, fontweight='bold'
            )

# Add a title
ax.set_title('Original Premium Income and Growth Rate of the Chinese Insurance Industry from 2019 to 2026', fontsize=16, pad=15)

# Set x-axis tick labels
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=11)

# Add a y-axis label
ax.set_ylabel('Premium Income (Billion Yuan)', fontsize=13)

# Add a legend
ax.legend(loc='upper left', frameon=True, framealpha=0.9, fontsize=11)

# Calculate the total premium for each year
total_premiums = premium_data.sum(axis=1)

# Add total premium annotations
for i, total in enumerate(total_premiums):
    ax.text(x[i], total + 1000,  # Adjust the vertical position to avoid overlapping with the bars
            f'{int(total)}', 
            ha='center', va='bottom', 
            fontsize=9, fontweight='bold',
            bbox=dict(facecolor='white', alpha=0.7, pad=2.0))

# CAGR annotation function
def add_cagr_annotation(start_idx, end_idx, cagr_value, ax, x, total_premiums):
    """Add CAGR polyline annotation"""
    start_x = x[start_idx]
    end_x = x[end_idx]
    start_y = total_premiums[start_idx]
    end_y = total_premiums[end_idx]
    
    # Calculate the position of the midpoint
    mid_x = (start_x + end_x) / 2
    mid_y1 = start_y + (end_y - start_y) * 0.3
    mid_y2 = start_y + (end_y - start_y) * 0.7
    
    # Draw a polyline
    ax.plot([start_x, end_x], [start_y, end_y], 
            'gray', linestyle='--', linewidth=1.2)
    
    # Add CAGR text
    text_x = mid_x
    text_y = mid_y2 + (end_y - start_y) * 0.25
    ax.text(text_x, text_y, f'CAGR = {cagr_value}%', 
            ha='center', va='bottom', fontsize=12, fontweight='bold',
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray', pad=3.0))

# Add CAGR annotation from 2019 to 2024
add_cagr_annotation(0, 5, 6, ax, x, total_premiums)

# Add CAGR annotation from 2024 to 2026
add_cagr_annotation(5, 7, 5, ax, x, total_premiums)

# Beautify the chart
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add horizontal grid lines
plt.tight_layout()  # Automatically adjust the layout

plt.show()