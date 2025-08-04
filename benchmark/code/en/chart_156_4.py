import matplotlib.pyplot as plt

# Data definition (more precise positions close to the original image)
labels = ['Skin - feel', 'Realistic', 'Invisible', 'Natural', 'Bare - skin feel']
x_sales_ratio = [0.05, 0.03, 0.04, 0.55, 0.75]  # Sales ratio
y_growth_rate = [2.8, 0.05, -0.02, 0.1, 0.12]   # Year - on - year growth rate
sizes = [500, 320, 300, 350, 360]  # Bubble sizes set manually to approximate the visual weight in the original image

# Create the chart
fig, ax = plt.subplots(figsize=(10, 6))

# Draw the bubble chart
ax.scatter(
    x_sales_ratio,
    y_growth_rate,
    s=sizes,
    c='#FF8888',
    alpha=0.75,
    edgecolors='white',
    linewidth=1.5
)

# Add text labels
for i in range(len(labels)):
    ax.text(x_sales_ratio[i] + 0.03, y_growth_rate[i] + 0.03, labels[i],
            ha='center', va='bottom', fontsize=10)

# Axis settings
ax.set_title('MAT2024 Online Taobao "Fake Skinny Leggings" Function Selling Points Segmentation\nRelated to Color Naturalness', fontsize=15, weight='bold')
ax.set_xlabel('Sales Ratio', fontsize=12)
ax.set_ylabel('Year - on - Year', fontsize=12)

# Set tick formats and ranges
ax.set_xlim(0, 0.9)
ax.set_ylim(-0.3, 3.2)
ax.set_xticks([0, 0.2, 0.4, 0.6, 0.8])
ax.set_xticklabels(['0%', '20%', '40%', '60%', '80%'])
ax.set_yticks([-1, 0, 1, 2, 3])
ax.set_yticklabels(['-100%', '0%', '100%', '200%', '300%'])

# Add grid and background
ax.grid(True, linestyle='--', alpha=0.4)
ax.set_facecolor('#fcfcfc')

# Data source description
source_text = "Data Source: Magic Mirror Market Intelligence Data; MAT2024: 2023.07 - 2024.06"
plt.figtext(0.5, -0.05, source_text, wrap=True, horizontalalignment='center', fontsize=9, color='gray')

plt.tight_layout()
plt.show()