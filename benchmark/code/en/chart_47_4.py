import matplotlib.pyplot as plt
import numpy as np

# Data (example, need to be replaced with actual data)
labels = ['MAT2022', 'MAT2023', 'MAT2024']
taobao = [60, 55, 45]  # Taotian proportion (example)
jingdong = [10, 10, 10]  # JD proportion (example)
douyin = [30, 35, 45]  # Douyin proportion (example)

x = np.arange(len(labels))  # x-axis positions
width = 0.35  # Bar width

fig, ax = plt.subplots()
# Draw bar charts for each channel, note the bottom parameter for stacking effect
rects_taobao = ax.bar(x, taobao, width, label='Taotian', color='#E67E22')
rects_jingdong = ax.bar(x, jingdong, width, bottom=taobao, label='JD', color='#E74C3C')
rects_douyin = ax.bar(x, douyin, width, bottom=np.add(taobao, jingdong), label='Douyin', color='#6DD9E0')

# Annotate the growth rate
ax.annotate('+28%', 
            xy=(2, 100),  # Adjust the xy position to the top of the third bar
            xytext=(0, 10),  # Add an offset to place the text above the bar
            textcoords="offset points",
            ha='center', 
            va='bottom',
            fontsize=12,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", linestyle="--", alpha=0.8))

# Add value labels to each bar
def add_labels(rects, bottom_values=None):
    for i, rect in enumerate(rects):
        height = rect.get_height()
        if bottom_values is not None:
            bottom = bottom_values[i]
        else:
            bottom = 0
        # Calculate the text position (middle of the bar)
        y_position = bottom + height / 2
        # Add value label
        ax.text(
            rect.get_x() + rect.get_width() / 2,  # x-coordinate: center of the bar
            y_position,                          # y-coordinate: middle of the bar
            f'{height}%',                        # Value to display
            ha='center', va='center',            # Horizontally and vertically centered
            color='white', fontweight='bold',    # White text, bold
            fontsize=9                           # Font size
        )

# Add labels for each channel
add_labels(rects_taobao)
add_labels(rects_jingdong, taobao)
add_labels(rects_douyin, np.add(taobao, jingdong))

# Set x-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(labels)
# Set y-axis range
ax.set_ylim(0, 110)  # Increase the upper limit of the y-axis to avoid text being obscured
# Add percentage ticks to the y-axis
ax.set_yticks(np.arange(0, 101, 20))
ax.set_yticklabels([f'{i}%' for i in range(0, 101, 20)])
# Add legend and title
ax.legend()
ax.set_title('Proportion and Growth Rate of Core Online Channels in Skincare Business')

plt.tight_layout()  # Optimize the layout
plt.show()