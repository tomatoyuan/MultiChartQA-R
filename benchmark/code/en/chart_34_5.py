import matplotlib.pyplot as plt
import numpy as np

# Simulated data, generally corresponding to the categories and trends in the original chart
categories = ["Fragrance", "Camellia", "Zero - feeling", "Sterile", "Skin care", "Hyaluronic acid", "Tencel", "Moisturizing", "Suspension", "Aloe vera"]
gmv_data = [71, 70, 20, 25, 20, 38, 26, 16, 32, 20]  # Simulated GMV (index) data
growth_data = [0.10, 0.1, 0.08, 0.06, 0.05, 0.04, 0.03, 0.025, 0.02, 0.015]  # Simulated year - on - year data

x = np.arange(len(categories))  # x - axis positions

# Create a canvas and subplot, set the chart size
fig, ax1 = plt.subplots(figsize=(12, 7))

# Set the background style - use the built - in style of Matplotlib instead
plt.style.use('ggplot')

# Draw a bar chart (GMV) - use gradient colors
cmap = plt.cm.Blues
norm = plt.Normalize(min(gmv_data), max(gmv_data))
colors = cmap(norm(gmv_data))

bars = ax1.bar(x, gmv_data, width=0.6, color=colors, label='GMV (Index)', edgecolor='black', linewidth=0.5)
ax1.set_ylabel('GMV (Index)', fontsize=12, fontweight='bold')
ax1.set_xlabel('Selling points', fontsize=12, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(categories, rotation=30, ha='right', fontsize=10)  # Rotate x - axis labels

# Add data labels to the bar chart
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 1,
             f'{height}', ha='center', va='bottom', fontsize=9)

# Create a second y - axis to draw a line chart (year - on - year)
ax2 = ax1.twinx()
line, = ax2.plot(x, growth_data, color='#FF7F50', marker='o', markersize=6,
                 linewidth=2, label='Year - on - year growth rate')
ax2.set_ylabel('Year - on - year growth rate', rotation=270, labelpad=18, fontsize=12, fontweight='bold')
ax2.set_ylim(0, 0.13)  # Roughly corresponding to the percentage range in the original chart

# Add data labels to the line chart
for i, txt in enumerate(growth_data):
    ax2.annotate(f'{txt:.1%}', (x[i], growth_data[i]),
                 textcoords="offset points",
                 xytext=(0, 10),
                 ha='center',
                 fontsize=9)

# Add a title and legend
plt.title('Top 10 growth rates of selling points of Douyin tech underwear since the spring new launch in 2025', fontsize=16, fontweight='bold', pad=20)

# Combine the two legends
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper right', frameon=True, shadow=True)

# Add grid lines
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax2.grid(axis='y', linestyle='--', alpha=0.3)

# Adjust the chart margins
plt.tight_layout()

# Display the chart
plt.show()