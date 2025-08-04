import matplotlib.pyplot as plt

# Data
labels = ["Listen to parents", "Decide by oneself", "Listen to experts or others"]
sizes = [36, 58, 6]
colors = ["#99CCFF", "#FFCC99", "#CC99FF"]  # Keep the original color scheme

# Create a canvas and sub - plot
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)

# Draw a pie chart, add shadow and explosion effect to highlight the "Decide by oneself" part
explode = (0, 0.05, 0)  # Only the "Decide by oneself" part is highlighted
wedges, texts, autotexts = ax.pie(
    sizes,
    explode=explode,
    autopct='%1.1f%%',  # Only show the percentage
    startangle=90,
    colors=colors,
    shadow=True,
    wedgeprops={'edgecolor': 'w', 'linewidth': 2},  # Add a white border
    textprops={'fontsize': 12, 'weight': 'bold'}  # Bold the percentage text
)

# Set the title
ax.set_title("Regarding college application, which option do you prefer?", fontsize=18, pad=20, fontweight='bold')

# Ensure the pie chart is circular
ax.axis("equal")  

# Optimize the legend style
legend = ax.legend(
    wedges, 
    labels, 
    title="College application preference", 
    loc="center left", 
    bbox_to_anchor=(1, 0.5),
    frameon=True,
    framealpha=0.9,
    edgecolor='lightgray',
    fontsize=12,
    title_fontsize=14,
    labelspacing=1.2,
    handlelength=1.5,
    handleheight=1.5
)

# Add background color and rounded corners to the legend
frame = legend.get_frame()
frame.set_facecolor('#f8f9fa')
frame.set_boxstyle("round,pad=0.5,rounding_size=4")

# Add data label style
for text in autotexts:
    text.set_backgroundcolor('white')
    text.set_alpha(0.8)
    text.set_bbox(dict(facecolor='white', alpha=0.8, edgecolor='none', pad=2))

# Adjust the layout
plt.tight_layout(pad=2)

# Display the graph
plt.show()