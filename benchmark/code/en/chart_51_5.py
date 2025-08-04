import matplotlib.pyplot as plt
import numpy as np

# Data definition, project quantity distribution and project amount distribution
labels = ["Banks", "Insurance", "Securities", "Others"]
sizes_quantity = [53, 12, 15, 20]  # Project quantity distribution, roughly simulated
sizes_amount = [56, 8, 17, 19]  # Project amount distribution, roughly simulated
# Color settings, as close to the original image as possible
colors = ["greenyellow", "green", "limegreen", "lightseagreen"]

# Create a canvas and sub - plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Draw a pie chart of project quantity distribution
ax1.pie(sizes_quantity, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
ax1.set_title('Project Quantity Distribution')

# Draw a pie chart of project amount distribution
ax2.pie(sizes_amount, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
ax2.set_title('Project Amount Distribution')

# Add a main title
fig.suptitle('Distribution of Winning Bids for Large - scale Financial Industry Models in 2024', fontsize=14)

plt.tight_layout()
plt.show()