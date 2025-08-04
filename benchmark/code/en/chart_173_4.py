import matplotlib.pyplot as plt

# Data
labels = ['Every day', '4 - 6 days a week', '1 - 3 days a week', 'Less than once a week', 'Irregular']
sizes = [18, 36, 39, 6, 2]
colors = ['#ff6384', '#ff8fa3', '#ff2d55', '#ffb6c1', '#ffe5eb']  # Red - based colors to distinguish different frequencies

# Construct label content
labels_with_pct = [f'{label}\n {size}%' for label, size in zip(labels, sizes)]

# Create a chart
fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts = ax.pie(sizes,
                       labels=labels_with_pct,
                       colors=colors,
                       startangle=90,
                       labeldistance=1.1,
                       textprops={'fontsize': 10},
                       wedgeprops=dict(width=0.6))

# Add a title
plt.title('Distribution of viewing frequency among mini - drama audiences', fontsize=14, fontweight='bold', pad=20)

# Ensure the chart is circular
ax.axis('equal')

# Add data source description
fig.text(0.01, 0.01,
         'Data source: Online quantitative survey of mini - drama users by Millward Brown, January 2024, N = 1,000\n'
         'B1. How often do you watch mini - dramas in your daily life? [Single choice]\n',
         fontsize=9, ha='left')

plt.tight_layout(rect=[0, 0.1, 1, 1])
plt.show()