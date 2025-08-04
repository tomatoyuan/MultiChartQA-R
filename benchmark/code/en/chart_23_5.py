import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ["It seems impossible to find a partner", "Poor communication skills make it hard to date", "Actively participate in blind dates", "Enjoy the single - culture", "Other"]
sizes = [40, 20, 19, 7.8, 13.2]  # The proportion of "Other" is calculated by 100 - 40 - 20 - 19 - 7.8, which is 13.2
colors = ["#f78199", "#a06cd5", "#ffe66d", "#ff4b5c", "#c3eaf4"]

# Create a donut chart
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90, pctdistance=0.85)

# Add a white circle in the center to form a donut chart effect
centre_circle = plt.Circle((0, 0), 0.70, fc="white")
fig.gca().add_artist(centre_circle)

# Set the title
ax.set_title("Among those who avoid getting into a relationship")

# Adjust the layout and display the chart
plt.tight_layout()
plt.show()