import matplotlib.pyplot as plt
import numpy as np

# Match data (match confrontation, score, popularity value)
matches = ["Russia 5:0 Saudi Arabia", 
           "Portugal 3:3 Spain", 
           "Egypt 0:1 Uruguay", 
           "Brazil 1:1 Switzerland", 
           "Tunisia 1:2 England"]
hot_values = [150, 136, 103, 78, 65]  # Popularity value (unit: ten thousand, simplified to numerical value)

# Used for display on the X-axis
x = np.arange(len(matches))  

# Create a canvas
fig, ax = plt.subplots(figsize=(10, 6))
# Draw a bar chart
rects = ax.bar(x, hot_values, width=0.6, color="#7B68EE")  

# Set X-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(matches, rotation=45, ha="right", fontsize=10)  

# Set Y-axis label
ax.set_ylabel("Popularity Value (Ten Thousand)", fontsize=12)  
# Set the title
ax.set_title("Top 5 Popularity Ranking of the First Round of the World Cup Group Stage", fontsize=14, fontweight="bold")  

# Annotate the values on the bars
for rect in rects:
    height = rect.get_height()
    ax.annotate(f"{height}K", 
                xy=(rect.get_x() + rect.get_width() / 2, height), 
                xytext=(0, 3),  # Offset upward by 3 pixels
                textcoords="offset points", 
                ha="center", va="bottom")

# Optimize the layout (avoid incomplete label display)
plt.tight_layout()  
# Display the chart
plt.show()