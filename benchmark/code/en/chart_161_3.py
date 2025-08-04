import matplotlib.pyplot as plt

# Data
quarters = ['23Q1', '24Q1']
categories = ['Average', 'Domestic Brands', 'International Brands']
data = {
    'Average': [39, 39],
    'Domestic Brands': [37, 43],
    'International Brands': [38, 37]
}
colors = ['#A0522D', '#FF8C00', '#FFA07A']  # Use color scheme similar to the original image

# Plotting
fig, ax = plt.subplots(figsize=(7, 5))
for idx, cat in enumerate(categories):
    ax.plot(quarters, data[cat], marker='^', label=cat, color=colors[idx], linewidth=2)

# Add text labels
for idx, cat in enumerate(categories):
    for i, quarter in enumerate(quarters):
        ax.text(quarter, data[cat][i] + 0.5, f"{data[cat][i]}%", color=colors[idx], ha='center', fontsize=12)

# Style settings
ax.set_ylim(35, 46)
ax.set_title("[Facial Cream] Gift Promotion Depth of TOP15 Brands in 24Q1 vs 23Q1 (Major E - commerce Platforms)", fontsize=14, weight='bold')
ax.legend(loc='best')
ax.set_ylabel("Gift Promotion Depth (%)")
ax.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
plt.show()