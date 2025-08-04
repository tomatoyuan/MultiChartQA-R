import matplotlib.pyplot as plt

# Set main category data
main_labels = ['Other Packaging', 'Sustainable Packaging']
main_sizes = [75, 25]
main_colors = ['#E0E0E0', '#8BC34A']

# Set sub - category data inside sustainable packaging
inner_labels = ['Reusable Packaging', 'Other Sustainable Packaging', 'Other Packaging (not subdivided)']
inner_sizes = [10, 15, 75]
inner_colors = ['#AED581', '#A1887F', '#FFFFFF00']  # The third item is transparent (to avoid redundant display of "Other Packaging")

# Create the chart
fig, ax = plt.subplots(figsize=(8, 6))

# Outer circle (main category)
wedges1, _ = ax.pie(
    main_sizes,
    radius=1,
    labels=[f'{v}%' for v in main_sizes],
    colors=main_colors,
    startangle=90,
    wedgeprops=dict(width=0.3, edgecolor='white')
)

# Inner circle (sub - categories of sustainable packaging)
wedges2, _ = ax.pie(
    inner_sizes,
    radius=1 - 0.3,
    labels=['10%', '15%', ''],
    colors=inner_colors,
    startangle=0,
    wedgeprops=dict(width=0.3, edgecolor='white')
)

# Add title
plt.title('Global Packaging Industry Product Structure in 2020', fontsize=16, color='green', weight='bold')

# Legend
custom_legend = [
    plt.Line2D([0], [0], marker='o', color='w', label='Other Packaging', markerfacecolor='#E0E0E0', markersize=12),
    plt.Line2D([0], [0], marker='o', color='w', label='Sustainable Packaging', markerfacecolor='#8BC34A', markersize=12),
    plt.Line2D([0], [0], marker='o', color='w', label='Reusable Packaging', markerfacecolor='#AED581', markersize=12),
    plt.Line2D([0], [0], marker='o', color='w', label='Other Sustainable Packaging', markerfacecolor='#A1887F', markersize=12)
]
plt.legend(handles=custom_legend, loc='lower center', bbox_to_anchor=(0.5, -0.15), ncol=2, fontsize=10, frameon=False)

plt.tight_layout()
plt.show()