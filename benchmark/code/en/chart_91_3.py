import matplotlib.pyplot as plt

# Outer pie chart data
outer_sizes = [25, 17, 75]
outer_labels = ['Market share of top 10 revenue - generating enterprises (%)', 'Market share of top 5 revenue - generating enterprises (%)', 'Market share of other enterprises (%)']
outer_colors = ['#A4C639', '#87CEEB', '#D3D3D3']

# Inner pie chart data
inner_sizes = [25 + 17, 75]  # Top 10 (including top 5), others
inner_labels = ['', '']
inner_colors = ['white', 'white']  # Inner blank circle

# Create a canvas
fig, ax = plt.subplots(figsize=(6, 6))

# Draw the outer pie chart
outer_wedges, outer_texts, outer_autotexts = ax.pie(outer_sizes, labels=outer_labels, autopct='%1.1f%%',
                                                    colors=outer_colors, startangle=90,
                                                    textprops={'color': 'black'})
# Set the title
ax.set_title('Market concentration of Chinese cup and kettle industry in 2021', fontsize=14, fontweight='bold', y=1.05)

# Keep the pie chart circular
ax.axis('equal')

plt.tight_layout()
plt.show()