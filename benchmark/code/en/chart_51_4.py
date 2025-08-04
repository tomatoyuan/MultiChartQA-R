import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2024e", "2025e", "2026e", "2027e", "2028e", "2029e"]

# Investment data for each technology (in billions of yuan), in the order of RPA/IPA, Others, AI, Cloud, Big Data
# Note: The last value is calculated by subtracting the previous values from the total to ensure the sum of each layer is correct
tech_investment = np.array([
    [12.2, 25.8, 61.1, 117.9 - (12.2 + 25.8 + 61.1)],  # Total in 2024e: 12.2+25.8+61.1+18.8=117.9
    [14.6, 32.3, 73.7, 144.9 - (14.6 + 32.3 + 73.7)],  # Total in 2025e: 14.6+32.3+73.7+24.3=144.9
    [17.5, 40.3, 88.5, 177.2 - (17.5 + 40.3 + 88.5)],  # Total in 2026e: 17.5+40.3+88.5+30.9=177.2
    [20.7, 49.9, 105.5, 215.3 - (20.7 + 49.9 + 105.5)],# Total in 2027e: 20.7+49.9+105.5+39.2=215.3
    [24.8, 62.3, 126.9, 263.8 - (24.8 + 62.3 + 126.9)],# Total in 2028e: 24.8+62.3+126.9+50.0=263.8
    [29.3, 54.0, 153.6, 325.4 - (29.3 + 54.0 + 153.6)] # Total in 2029e: 29.3+54.0+153.6+88.5=325.4
])

# Colors corresponding to each technology (as close as possible to the original image)
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Technology names (with units)
tech_names = ["RPA/IPA", "Others", "AI", "Cloud", "Big Data"]

x = np.arange(len(years))  # x-axis tick positions
bar_width = 0.6  # Width of the bar chart

fig, ax = plt.subplots(figsize=(12, 7))

# Draw the stacked bar chart
bottom = np.zeros(len(years))
for i in range(tech_investment.shape[1]):
    bars = ax.bar(x, tech_investment[:, i], width=bar_width, bottom=bottom, 
                  color=colors[i], label=tech_names[i])
    bottom += tech_investment[:, i]
    
    # Label the values in each stacked layer
    for j, bar in enumerate(bars):
        height = bar.get_height()
        if height > 0:  # Only label non-zero values
            ax.text(
                bar.get_x() + bar.get_width()/2, 
                bar.get_y() + height/2,
                f'{height:.1f}',
                ha='center', va='center',
                color='white', fontsize=9, fontweight='bold'
            )

# Add the title
ax.set_title('China Insurance Industry Frontier Technology Investment from 2024 to 2029', fontsize=14, pad=15)

# Set x-axis tick labels
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=11)

# Add y-axis label
ax.set_ylabel('Technology Investment (Billions of Yuan)', fontsize=12)

# Add the legend (placed on the right side of the chart)
ax.legend(loc='upper left', frameon=True, framealpha=0.9, fontsize=10)

# Calculate and label the CAGR (22.5%)
cagr = 22.5
start_value = tech_investment[0].sum()
end_value = tech_investment[-1].sum()

# Draw the CAGR line
ax.plot([x[0], x[-1]], [start_value, end_value], 'gray', linestyle='--', linewidth=1.2)

# Add the CAGR text label
ax.annotate(
    f'CAGR={cagr}%', 
    xy=(x[2], start_value + (end_value - start_value)*0.4), 
    xytext=(x[2]+0.5, start_value + (end_value - start_value)*0.6),
    arrowprops=dict(facecolor='gray', shrink=0.05, width=1.2, headwidth=8),
    fontsize=11,
    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8)
)

# Beautify the chart
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add horizontal grid lines
plt.tight_layout()  # Automatically adjust the layout

plt.show()