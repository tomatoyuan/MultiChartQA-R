import matplotlib.pyplot as plt
import numpy as np

# Data
city_levels = ["First-tier cities", "Second-tier cities", "Third-tier cities", "Fourth-tier cities"]
proportion = [38, 19, 17, 12]  # Proportion data
growth_rate = [-6, -4, -8, -9]  # Growth rate data

x = np.arange(len(city_levels))  # x-axis tick positions

# Create a chart
fig, ax1 = plt.subplots(figsize=(10, 6))  # Adjust the chart size

# Set the background style - Use a built-in Matplotlib style
plt.style.use('ggplot')  # Change to a built-in Matplotlib style

# Draw a bar chart (proportion) - Use gradient colors
bar_colors = ['#4A86E8', '#6AA1E8', '#8ABBE8', '#AAD5E8']  # Blue gradient
bars = ax1.bar(x, proportion, color=bar_colors, label='Proportion', width=0.6, edgecolor='black', linewidth=0.5)
ax1.set_ylabel('Proportion (%)', color='#4A86E8', fontsize=12)
ax1.set_xlabel('City level', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(city_levels, fontsize=11)
ax1.tick_params(axis='y', labelcolor='#4A86E8')

# Add data labels above the bar chart
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 0.5,
             f'{height}%', ha='center', va='bottom', fontsize=10)

# Create a second y-axis and draw a line chart (growth rate)
ax2 = ax1.twinx()
line_color = '#FF9900'  # Orange
ax2.plot(x, growth_rate, color=line_color, label='Growth rate', linewidth=2.5, marker='o', markersize=8)
ax2.set_ylabel('Growth rate (%)', color=line_color, fontsize=12)
ax2.tick_params(axis='y', labelcolor=line_color)
ax2.set_ylim([-10, 0])  # Set the range of the growth rate axis

# Add data labels on the line chart
for i, txt in enumerate(growth_rate):
    ax2.annotate(f'{txt}%', (x[i], growth_rate[i]), textcoords="offset points", 
                 xytext=(0,10), ha='center', fontsize=10, color=line_color)

# Add a legend - Use a more beautiful style
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper right', 
           frameon=True, framealpha=0.9, edgecolor='black', fancybox=True)

# Add a chart title
plt.title('Attention proportion of vocational training industry by city level in May', fontsize=16, fontweight='bold', pad=20)

# Add grid lines to enhance readability
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax1.grid(axis='x', visible=False)
ax2.grid(visible=False)

# Adjust the chart layout
plt.tight_layout()

# Display the chart
plt.show()