import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['Proportion of vocational training searches on PC', 'Proportion of vocational training searches on mobile']
sizes = [19.30, 80.70]
# A more modern color scheme
colors = ['#3498db', '#e74c3c']  
# Highlight the mobile part
explode = (0, 0.05)  

# Create a figure and axes, set the figure size
fig, ax = plt.subplots(figsize=(8, 6))

# Draw a donut chart, add shadow effect and optimize the percentage text format
wedges, texts, autotexts = ax.pie(sizes, 
                                explode=explode,
                                labels=labels,
                                autopct=lambda p: f'{p:.2f}%\n({p*sum(sizes)/100:.1f})',
                                startangle=90,
                                colors=colors,
                                wedgeprops={'width': 0.4, 'edgecolor': 'w', 'linewidth': 2},
                                shadow=True,
                                textprops={'fontsize': 12})

# Set the title and legend
ax.set_title('Analysis of the proportion of vocational training search terminals', fontsize=16, pad=20)
ax.legend(wedges, labels, title="Terminal type", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Optimize the percentage text style - change the color to dark
plt.setp(autotexts, size=12, weight="bold", color='black')  # Change the color to black
plt.setp(texts, size=12)

# Set the figure background and layout
plt.tight_layout()
plt.axis('equal')  # Ensure the pie chart is circular
plt.subplots_adjust(right=0.8)  # Make room for the legend

# Save the figure (optional)
# plt.savefig('Proportion of vocational training search terminals.png', dpi=300, bbox_inches='tight')

# Show the figure
plt.show()