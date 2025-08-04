import matplotlib.pyplot as plt
import numpy as np

# Construct horizontal axis date data corresponding to the dates in the original chart
dates = ["2.1", "2.3", "2.5", "2.7", "2.9", "2.11", 
         "2.13", "2.15", "2.17", "2.19", "2.21", 
         "2.23", "2.25", "2.27"]
# Construct approximate vertical axis search attention data following the trend of the original chart
values = [150000, 200000, 250000, 380000, 370000, 390000, 
          360000, 430000, 440000, 410000, 560000, 
          430000, 420000, 340000]  

# Create a canvas and set its size
fig, ax = plt.subplots(figsize=(10, 6))  

# Draw a line chart, set the line color to blue, and adjust the line width for a better visual effect
line, = ax.plot(dates, values, color="#4285F4", linewidth=2.5)  

# Set the chart title, bold the font
ax.set_title("February Milk Powder Industry Search Attention Trend", fontsize=16, fontweight="bold")  

# Set the vertical axis label, range, and ticks
ax.set_ylabel("Attention", fontsize=12)
ax.set_ylim(100000, 600000)  
ax.set_yticks([100000, 200000, 300000, 400000, 500000, 600000])  
# Format the vertical axis tick labels with comma separators
ax.set_yticklabels([f"{tick:,}" for tick in ax.get_yticks()])  

# Set the horizontal axis ticks using the constructed date data
ax.set_xticks(dates)  

# Add grid lines in dashed style to improve chart readability
ax.grid(linestyle="--", color="gray", alpha=0.3)  

# Add annotations to the data points
for x, y in zip(dates, values):
    # Format the numerical value with a thousands separator
    value_str = f"{y:,}"
    
    # Adjust the annotation position to avoid overlap
    if y > 400000:  # Annotation above the point
        ax.annotate(value_str, 
                    (x, y), 
                    textcoords="offset points",
                    xytext=(0, 10), 
                    ha='center',
                    fontsize=9,
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#4285F4", alpha=0.8))
    else:  # Annotation below the point
        ax.annotate(value_str, 
                    (x, y), 
                    textcoords="offset points",
                    xytext=(0, -15), 
                    ha='center',
                    fontsize=9,
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#4285F4", alpha=0.8))

# Highlight the maximum and minimum values
max_value = max(values)
min_value = min(values)
for x, y in zip(dates, values):
    if y == max_value or y == min_value:
        ax.scatter(x, y, color='red', s=50, zorder=5)
        ax.annotate(f"{y:,}", 
                    (x, y), 
                    textcoords="offset points",
                    xytext=(0, 15), 
                    ha='center',
                    fontsize=10,
                    fontweight='bold',
                    color='red',
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="red", alpha=0.8))

# Add a legend
ax.legend([line], ["Search Attention"], loc='upper left')

# Add a data source description
plt.figtext(0.1, 0.01, 'Data Source: Fictitious data for example only', ha="left", fontsize=9, bbox={"facecolor":"white", "alpha":0.5, "pad":5})

# Optimize the layout to avoid element overlap
plt.tight_layout()  

# Display the chart
plt.show()