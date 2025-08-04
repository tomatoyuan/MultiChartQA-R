import matplotlib.pyplot as plt
import numpy as np

# Left: Survey data on the number of self-operated brokerage APPs owned by Chinese brokerage users
left_labels = ["3-4", "1-2", "5 or more"]
left_sizes = [54.55, 39.57, 5.88]
left_colors = ["gold", "coral", "green"]

# Right: Survey data on the number of times Chinese brokerage users open self-operated brokerage APPs per day
right_labels = ["Open several times a day on average", "Open several times a week on average", 
                "Open many times a day on average", "Open several times a month on average", 
                "Open less than once a year on average"]
right_sizes = [44.39, 32.09, 14.97, 7.49, 1.06]
right_colors = ["gold", "green", "coral", "brown", "olive"]

# Create a larger figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Left pie chart: Number of APPs owned
# Adjust percentage label position with pctdistance
wedges, texts, autotexts = ax1.pie(
    left_sizes, 
    labels=left_labels, 
    colors=left_colors, 
    autopct="%1.2f%%",
    startangle=90,
    pctdistance=0.85,  # Distance of percentage labels from center
    textprops={'fontsize': 12}  # Label font size
)

# Adjust left percentage label colors
for autotext in autotexts:
    autotext.set_color("black")

# Set left title
ax1.set_title("Survey on the number of self-operated brokerage APPs\nowned by Chinese brokerage users", fontsize=14, pad=20)

# Right pie chart: Number of daily openings
# Use explode parameter to separate slices and avoid label overlap
explode = (0.05, 0.05, 0.05, 0.05, 0.08)  # Separation for each slice
wedges, texts, autotexts = ax2.pie(
    right_sizes, 
    labels=right_labels, 
    colors=right_colors, 
    autopct="%1.2f%%",
    startangle=90,
    explode=explode,  # Separate slices to avoid label overlap
    pctdistance=0.85,  # Distance of percentage labels from center
    labeldistance=1.1,  # Distance of category labels from center
    textprops={'fontsize': 11}  # Label font size
)

# Adjust right percentage label colors
for autotext in autotexts:
    autotext.set_color("black")

# Set right title
ax2.set_title("Survey on the number of times Chinese brokerage users open self-operated brokerage APPs per day", fontsize=14, pad=20)

# Adjust layout
plt.tight_layout(pad=5.0)  # Increase spacing between subplots

plt.show()