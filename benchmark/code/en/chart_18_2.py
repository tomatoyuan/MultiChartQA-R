import matplotlib.pyplot as plt
import numpy as np

# Data definition
labels = ["Banquet", "Motorcade", "Master of Ceremonies", "Wedding Supplies", "Others", "Honeymoon", "Jewelry", "Wedding Photos"]
sizes = [6, 0.8, 0.2, 1.5, 5, 4, 3, 1]
total_cost = sum(sizes)  # Total cost

# Optimized color scheme (using more harmonious gradient colors)
colors = plt.cm.YlOrRd(np.linspace(0.2, 0.9, len(labels)))

# Create a canvas and sub - plot
fig, ax = plt.subplots(figsize=(10, 8))

# Draw a donut chart
wedges, texts, autotexts = ax.pie(
    sizes, 
    labels=None,  # Do not display labels directly on the chart
    colors=colors,
    autopct='',  # Do not display values for now
    startangle=90,
    wedgeprops=dict(width=0.4, edgecolor='w', linewidth=2)  # Increase the ring width and add a white border
)

# Customize labels: display both the name and the amount, and intelligently adjust the position and color
for i, (wedge, label, size) in enumerate(zip(wedges, labels, sizes)):
    # Calculate the text position
    theta = (wedge.theta2 + wedge.theta1) / 2
    x = 0.65 * np.cos(np.radians(theta))  # 0.65 controls the radial position
    y = 0.65 * np.sin(np.radians(theta))
    
    # Adjust the text style according to the sector size
    text_size = 10 if size / total_cost > 0.05 else 8  # Use a smaller font for small sectors
    
    # Text content
    text = f"{label}\n{size} million yuan"
    
    # Adjust the text color (use white text for dark sectors and black text for light sectors)
    color = 'white' if i in [0, 4, 5, 6] else 'black'
    
    # Add text
    ax.text(x, y, text, ha='center', va='center', fontsize=text_size, 
            fontweight='bold', color=color, bbox=dict(
                boxstyle="round,pad=0.2", 
                fc=colors[i], 
                ec='none', 
                alpha=0.7
            ))

# Set the title
ax.set_title("Wedding Expense Distribution of Miss Liu in Shanghai", fontsize=18, fontweight='bold', pad=20)
subtitle = f"Total cost: {total_cost} million yuan"
plt.figtext(0.5, 0.92, subtitle, ha='center', fontsize=12, color='gray')

# Add center text
centre_circle = plt.Circle((0, 0), 0.2, fc='white')
ax.add_patch(centre_circle)
ax.text(0, 0, "Wedding Expenses", ha='center', va='center', fontsize=14, fontweight='bold')

# Adjust the layout
plt.tight_layout()

# Add the data source
plt.figtext(0.5, 0.01, "Data source: Hypothetical example", ha='center', fontsize=8, color='gray')

plt.show()