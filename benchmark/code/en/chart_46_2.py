import matplotlib.pyplot as plt

# Data - In the order of the chart: Ergonomic chairs, Eye - protecting lamps, Standing desks; Generational order: Post - 05s → Post - 00s → Post - 95s → Post - 90s → Post - 85s → Post - 80s
categories = ["Ergonomic chairs", "Eye - protecting lamps", "Standing desks"]
generations = ["Post - 05s", "Post - 00s", "Post - 95s", "Post - 90s", "Post - 85s", "Post - 80s"]
# 1 means the square is filled, 0 means not, corresponding to the chart
data = {
    "Ergonomic chairs": [0, 0, 1, 1, 1, 1],  
    "Eye - protecting lamps": [1, 0, 0, 0, 1, 1],     
    "Standing desks": [1, 0, 1, 0, 1, 0]      
}

# Total percentages (consistent with the chart)
total_percentages = {
    "Ergonomic chairs": 66,
    "Eye - protecting lamps": 55,
    "Standing desks": 53
}

# Custom colors (similar to the original orange color scheme)
colors = {
    "Ergonomic chairs": "#F8C4B4",  # Light orange, similar to the color of ergonomic chairs in the original chart
    "Eye - protecting lamps": "#F8C4B4",    # Light orange, color for eye - protecting lamps
    "Standing desks": "#F8C4B4"     # Light orange, color for standing desks
}

# Create a canvas
fig, ax = plt.subplots(figsize=(10, 5))  # Adjust the canvas size

# Set grid parameters
grid_size = 0.8   # Square size
spacing = 0.2     # Spacing between squares
label_width = 2   # Width of the left - hand label area

# Draw the content
for i, cat in enumerate(categories):
    # Background of the left - hand label (semi - transparent light orange)
    rect_bg = plt.Rectangle(
        (0, i * (grid_size + spacing)),
        label_width, grid_size,
        facecolor=colors[cat],
        alpha=0.3,
        edgecolor='none'
    )
    ax.add_patch(rect_bg)
    
    # Item name
    ax.text(
        label_width * -0.1,  
        i * (grid_size + spacing) + grid_size/2,
        cat,
        ha='left',
        va='center',
        color='black',
        fontweight='bold',
        fontsize=12
    )
    
    # Percentage label
    ax.text(
        label_width * 1.0,  
        i * (grid_size + spacing) + grid_size/2,
        f'{total_percentages[cat]}%',
        ha='right',
        va='center',
        color='black',
        fontweight='bold',
        fontsize=12
    )
    
    # Draw data squares
    for j, value in enumerate(data[cat]):
        if value == 1:  # Draw a square if there is a value
            rect = plt.Rectangle(
                (label_width + j * (grid_size + spacing), i * (grid_size + spacing)),
                grid_size, grid_size,
                facecolor=colors[cat],
                edgecolor='white',
                alpha=1
            )
            ax.add_patch(rect)

# Set the axis range
ax.set_xlim(0, label_width + len(generations) * (grid_size + spacing))
ax.set_ylim(0, len(categories) * (grid_size + spacing))

# X - axis labels (generations)
x_ticks = [label_width + j * (grid_size + spacing) + grid_size/2 for j in range(len(generations))]
ax.set_xticks(x_ticks)
ax.set_xticklabels(generations, fontsize=11, rotation=0)

# Title
ax.set_title('Furniture consumers most want to equip in their study (Highlighted parts with TGI>100 indicate high preference)', fontsize=14, pad=20)

# Hide unnecessary borders, keep X - axis labels
ax.yaxis.set_visible(False)  # Hide the Y - axis
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# Adjust the layout to avoid truncation
plt.tight_layout()
plt.show()