import matplotlib.pyplot as plt
import numpy as np

# Category names
categories = ["Outdoor functional socks", "Shark leggings", "Trail running shoes", "Soft shell clothing", "Ladies' clothing for middle - aged women", 
              "Warm cotton coats", "Sports ball uniforms", "Hanfu - Neo - Chinese style", "Down vests", "Sports polo shirts"]
# Simulated transaction amount growth rate data, roughly close to the proportion of the original chart
data = [92, 88, 65, 60, 55, 52, 48, 45, 42, 38]  

x = np.arange(len(categories))  # x-axis positions

fig, ax = plt.subplots()
# Draw a bar chart, set the color to a similar brown - like color, and adjust the bar width
bars = ax.bar(x, data, width=0.6, color='#b38878')  

# Set the y-axis range
ax.set_ylim([30, 100])  
# Set x-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=45, ha='right')  

# Add y-axis label
ax.set_ylabel('Transaction amount growth rate', fontsize=12)  
# Add title
ax.set_title('Top 10 categories with high growth in business scale of Douyin e - commerce autumn and winter clothing in 2024', fontsize=14, pad=20)  

# Add data labels
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

# Hide the top and right borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()  # Adjust the layout
plt.show()