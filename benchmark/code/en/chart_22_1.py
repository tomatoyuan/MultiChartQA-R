import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Data
labels = ["Total Investment", "Business, Transfers, Tickets", "Foreign Player Signing Expenses"]
values = [41, 30.9, 34.3]
colors = ["#2E7D32", "#2E7D32", "#B71C1C"]  # Green and Red
highlight_color = "#FFC107"  # Yellow highlight

# Create the canvas with increased height to avoid overlap
fig, ax = plt.subplots(figsize=(10, 6), facecolor='#f8f9fa')  # 增加画布宽度
ax.set_ylim(0, 1.2)  # 扩展y轴范围
ax.set_xlim(0, len(values) * 3)  # 扩展x轴范围，为倾斜标签提供更多空间
ax.axis('off')

# Draw the background grid
for i in range(1, 10):
    ax.axhline(y=i*0.1, color='#e9ecef', linestyle='-', alpha=0.5)

# Draw the data blocks with more spacing
for i in range(len(values)):
    # Add shadow effect
    shadow = patches.FancyBboxPatch(
        (i * 3 + 0.1, 0.3), 1.8, 0.6,  # 增加方块宽度和位置间隔
        boxstyle=patches.BoxStyle("Round", pad=0.02),
        facecolor='black', alpha=0.2
    )
    ax.add_patch(shadow)
    
    # Draw the main block
    rect = patches.FancyBboxPatch(
        (i * 3, 0.35), 1.8, 0.6,  # 增加方块宽度
        boxstyle=patches.BoxStyle("Round", pad=0.02),
        facecolor=colors[i], edgecolor="none", alpha=0.9
    )
    ax.add_patch(rect)
    
    # Add border highlight
    highlight = patches.FancyBboxPatch(
        (i * 3, 0.35), 1.8, 0.6,  # 增加方块宽度
        boxstyle=patches.BoxStyle("Round", pad=0.02),
        facecolor='none', edgecolor=highlight_color, 
        linewidth=2, alpha=0.8
    )
    ax.add_patch(highlight)
    
    # Draw the value text
    ax.text(
        i * 3 + 0.9, 0.65, f"{values[i]}",  # 调整数值位置
        ha="center", va="center", fontsize=28, 
        color="white", fontweight='bold',
        bbox=dict(facecolor='none', edgecolor='none')
    )

# Add the title
ax.text(
    (len(values) * 3) / 2, 1.1, "Overview of Chinese Super League Club Financial Data", 
    ha="center", va="center", fontsize=20, 
    color="#212529", fontweight='bold'
)

# Add the subtitle
ax.text(
    (len(values) * 3) / 2, 1.0, "Unit: Billion RMB", 
    ha="center", va="center", fontsize=14, 
    color="#6c757d"
)

# Draw the labels with 30-degree rotation
for i, label in enumerate(labels):
    ax.text(
        i * 3 + 0.9, 0.25, label,  # 调整标签位置
        ha="center", va="center", fontsize=12, 
        color="#333333", fontweight='bold',
        rotation=30  # 设置倾斜角度
    )

# Adjust legend position
ax.text(
    1.5, 0.1, "■ Revenue Items",  # 调整图例位置
    ha="center", va="center", fontsize=12, 
    color="#2E7D32"
)
ax.text(
    4.5, 0.1, "■ Expense Items",  # 调整图例位置
    ha="center", va="center", fontsize=12, 
    color="#B71C1C"
)

# Adjust data source position
ax.text(
    (len(values) * 3) - 1.5, 0.1, "Data Source: Fictitious Example", 
    ha="right", va="center", fontsize=10, 
    color="#6c757d"
)

# Fine-tune the layout
plt.tight_layout()

# Display the chart
plt.show()