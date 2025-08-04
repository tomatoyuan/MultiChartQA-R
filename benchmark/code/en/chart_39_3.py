import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ["Often visit, the Shanghai-style culture is very distinctive", "Have visited, experienced the old Shanghai coffee culture", "Haven't visited, but quite interested", "Don't want to visit, not very interested"]
sizes = [31, 50, 16, 3]  # The data can be approximately the same
# Colors, try to be close to the original image and can be fine - tuned according to the actual situation
colors = ["#E67E22", "#F1C40F", "#BDC3C7", "#95A5A6"]

# Draw a pie chart
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140, colors=colors)

# Set the title
ax.set_title("Consumers' willingness to experience Shanghai-style cafes")

# Display the chart
plt.show()