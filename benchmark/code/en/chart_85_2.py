import matplotlib.pyplot as plt

# Data
labels = ['Industrial Sector', 'Transportation', 'Construction and Other Sectors']
sizes = [60, 31, 9]
colors = ['#A4C639', '#a8dda8', '#87CEEB']  # Match the original color tone

# Create canvas
fig, ax = plt.subplots(figsize=(6, 6))

# Draw pie chart
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',  
    startangle=90,     
    colors=colors,
    textprops={'color': 'black'}
)

# Adjust label positions (place "Industrial Sector" labels outside the pie chart to match original layout)
for text, autotext, wedge in zip(texts, autotexts, wedges):
    if text.get_text() == 'Industrial Sector':
        text.set_position((1.15, 0.5))  
        autotext.set_position((1.3, 0.5))

# Add structure description box above
structure_text = "Industrial Sector: 60%\nTransportation: 31%\nConstruction and Other: 9%"
bbox_props = dict(boxstyle="round,pad=0.5", fc="white", ec="green", lw=1)
ax.text(0.25, 0.1, structure_text, transform=ax.transAxes, fontsize=12,
        bbox=bbox_props, color='green')

# Set title
ax.set_title('Hydrogen Utilization Structure', fontsize=14, fontweight='bold', y=1.1)

plt.tight_layout()
plt.show()