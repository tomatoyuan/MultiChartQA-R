import matplotlib.pyplot as plt
import numpy as np

# Data definition
provinces = ["Guangdong", "Jiangsu", "Shandong", "Beijing", "Henan"]
fraud_attention = [11, 9, 6.5, 5.2, 4]
gdp_2015 = [9.5, 7.5, 4, 1.2, 2.2]

# Create a canvas and sub - plots
fig, ax = plt.subplots(figsize=(10, 6))
x = np.arange(len(provinces))
width = 0.35

# Set gradient colors
colors1 = plt.cm.Oranges(np.linspace(0.6, 0.9, len(provinces)))
colors2 = plt.cm.Greens(np.linspace(0.6, 0.9, len(provinces)))

# Draw a bar chart with gradient colors
rects1 = ax.bar(x - width/2, fraud_attention, width, 
                label='Telecom fraud attention in each province', color=colors1, 
                edgecolor='black', linewidth=0.5)

rects2 = ax.bar(x + width/2, gdp_2015, width, 
                label='GDP of each province in 2015', color=colors2, 
                edgecolor='black', linewidth=0.5)

# Add numerical labels (optimize position and style)
def add_labels(rects, ax, is_top=False):
    for rect in rects:
        height = rect.get_height()
        y_pos = height + 0.3 if not is_top else height - 0.3
        va = 'bottom' if not is_top else 'top'
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, y_pos),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va=va,
                    fontsize=10, fontweight='bold')

add_labels(rects1, ax)
add_labels(rects2, ax, is_top=True)

# Set the chart title and axis labels
ax.set_title("Comparison of telecom fraud attention and GDP of each province in 2015", 
             fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel("Value (Unit: 100 million yuan/Attention index)", fontsize=12, labelpad=10)

# Set the x - axis and y - axis styles
ax.set_xticks(x)
ax.set_xticklabels(provinces, fontsize=12, fontweight='bold')
ax.set_ylim(0, 13)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Beautify the legend
legend = ax.legend(fontsize=10, frameon=True, loc='upper right')
frame = legend.get_frame()
frame.set_facecolor('white')
frame.set_edgecolor('gray')
frame.set_alpha(0.8)

# Add bottom text description (optimize typesetting)
plt.figtext(0.5, 0.01, 
            "Top five in fraud prevention attention: Guangdong, Shandong, Jiangsu, Beijing, Henan\n"
            "Top five in GDP ranking of each province in 2015: Guangdong, Jiangsu, Shandong, Zhejiang, Henan", 
            ha="center", fontsize=10, color='dimgray')

# Add background color to distinguish areas
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#ffffff')

# Adjust the layout
plt.tight_layout(pad=3)
plt.show()