import matplotlib.pyplot as plt

# Data
labels = ['Pet Food', 'Pet Supplies', 'Pet Health', 'Live Pets', 'Pet Services']
sizes = [49.7, 35.5, 8.4, 6.2, 0.2]
# Color scheme for beautification (using softer gradient colors)
colors = ['#6a89cc', '#82ccdd', '#b8e994', '#f8c291', '#d6a2e8']
# Highlight the largest part
explode = (0.1, 0, 0, 0, 0)  

# Create a canvas and sub - plot
fig, ax = plt.subplots(figsize=(10, 7), dpi=300)

# Draw a pie chart with shadow and 3D effect
wedges, texts, autotexts = ax.pie(
    sizes, 
    explode=explode,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    shadow=True,
    wedgeprops={'edgecolor': 'w', 'linewidth': 2},
    textprops={'fontsize': 12, 'weight': 'bold'}
)

# Adjust the color of percentage texts
for text in autotexts:
    text.set_color('black')

# Set the title and legend
ax.set_title('MAT2024 Sales Proportion of Pet E - commerce Sub - categories', fontsize=16, pad=20)
ax.legend(wedges, labels, title="Categories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Ensure the pie chart is circular
plt.axis('equal')
plt.tight_layout()

# Save the chart (optional)
# plt.savefig('pet_ecommerce_sales.png', bbox_inches='tight')

plt.show()