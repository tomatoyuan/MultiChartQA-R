import matplotlib.pyplot as plt
import numpy as np

# Data
age_groups = ["Under 19", "25 - 34", "19 - 24", "35 - 49", "Over 50"]
percentages = [11, 49, 20, 15, 5]
colors = ["#1f77b4", "#8dd3c7", "#bebada", "#fb8072", "#80b1d3"]  # Custom colors, can be adjusted

# Create a donut chart
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(
    percentages,
    labels=age_groups,
    autopct="%1.1f%%",  # Display percentage format
    startangle=90,
    colors=colors,
    pctdistance=0.85,  # Distance of percentage labels from the center
    wedgeprops={"width": 0.4},  # Width of the donut
)

# Add a center circle (to make the donut more obvious)
centre_circle = plt.Circle((0, 0), 0.6, color="black", fc="white", linewidth=0)
ax.add_artist(centre_circle)

# Set the title
ax.set_title("Age Group Distribution", fontsize=16, y=1.05)

# Display the chart
plt.show()