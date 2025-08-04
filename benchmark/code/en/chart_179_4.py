import matplotlib.pyplot as plt
import numpy as np

# Labels for different cost categories
labels_cost = ['Website Building Cost', 'Product Development', 'Traffic Cost', 'Warehousing and Logistics', 'Labor Cost', 'Other Costs']
# Corresponding cost values
values_cost = [6.1, 25.5, 32.6, 13.0, 18.5, 4.3]
# Make the data cyclic for a closed radar chart
values_cost += values_cost[:1]
# Generate angles for each label
angles = np.linspace(0, 2 * np.pi, len(labels_cost), endpoint=False).tolist()
# Make the angles cyclic
angles += angles[:1]

# Create a figure and a polar sub - plot
fig1, ax1 = plt.subplots(figsize=(6, 6), subplot_kw={'polar': True})
# Plot the radar chart
ax1.plot(angles, values_cost, color='darkorange', linewidth=2)
# Fill the area inside the radar chart
ax1.fill(angles, values_cost, color='darkorange', alpha=0.6)
# Set the labels for each angle
ax1.set_thetagrids(np.degrees(angles[:-1]), labels_cost, fontsize=10)
# Set the title of the chart
ax1.set_title("Main Cost Expenditure of Independent Website", fontsize=14, fontweight='bold', pad=20)

# Add data labels to the chart
for angle, value in zip(angles, values_cost):
    ax1.text(angle, value + 2, f'{value:.1f}%', color='darkred', ha='center', va='center', fontsize=12)

# Add source information at the bottom of the chart
plt.figtext(0.5, 0.02, "Source: GoodsFox Research Data, Statistical Time: January - December 2023", ha='center', fontsize=10)
# Adjust the layout to make it look better
plt.tight_layout()
# Display the chart
plt.show()