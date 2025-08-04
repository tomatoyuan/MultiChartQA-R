import numpy as np
import matplotlib.pyplot as plt

# Labels for marketing methods
labels_mkt = ['SEO Marketing', 'SEM Marketing', 'Social Media Marketing\n(Including Account Self-Operation \nand Advertising)', 'Influencer Marketing', 'Email Marketing', 'Other Methods']
# Values representing the proportion of each marketing method
values_mkt = [23.5, 45.6, 65.0, 47.5, 20.4, 5.3]
# Add the first value to the end to close the radar chart
values_mkt += values_mkt[:1]
# Generate angles for each label
angles = np.linspace(0, 2 * np.pi, len(labels_mkt), endpoint=False).tolist()
# Add the first angle to the end to close the radar chart
angles += angles[:1]

# Create a figure and a polar subplot
fig2, ax2 = plt.subplots(figsize=(6, 6), subplot_kw={'polar': True})
# Plot the radar chart
ax2.plot(angles, values_mkt, color='darkorange', linewidth=2)
# Fill the area inside the radar chart
ax2.fill(angles, values_mkt, color='darkorange', alpha=0.6)
# Set the labels for each angle
ax2.set_thetagrids(np.degrees(angles[:-1]), labels_mkt, fontsize=10)
# Set the title of the chart
ax2.set_title("Main Marketing Promotion Methods for Independent Websites", fontsize=14, fontweight='bold', pad=20)

# Add the percentage values to each point on the radar chart
for angle, value in zip(angles, values_mkt):
    ax2.text(angle, value - 2, f'{value:.1f}%', color='darkred', ha='center', va='center', fontsize=12)

# Add the source information at the bottom of the chart
plt.figtext(0.5, 0.02, "Source: GoodsFox Research Data, Statistics Time: January - December 2023", ha='center', fontsize=10)
# Adjust the layout to make the chart look better
plt.tight_layout()
# Show the chart
plt.show()