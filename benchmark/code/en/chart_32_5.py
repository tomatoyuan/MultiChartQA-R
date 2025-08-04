import matplotlib.pyplot as plt
import numpy as np

# Define keywords and corresponding areas (decrease in the specified order and enlarge overall)
keywords = ["Teacher Qualification Certificate", "Online Education", "Teacher Establishment", "Teacher Holidays", "Teacher Benefits"]
sizes = [152000, 111600, 9200, 6800, 4400]  # Double the area overall
colors = ['#FFC2D1', '#BDE0FE', '#BDB2FF', '#A2D2FF', '#C8B6FF']  # Bubble colors

# Create a canvas
plt.figure(figsize=(12, 10))  # Increase the canvas size

# Generate evenly distributed positions (arranged in a circle)
theta = np.linspace(0, 2*np.pi, len(keywords), endpoint=False)
radius = 1.5  # Increase the radius of the circle to avoid bubble overlap
x = radius * np.cos(theta)
y = radius * np.sin(theta)

# Draw a bubble chart
scatter = plt.scatter(x, y, s=sizes, c=colors, alpha=0.7, edgecolors='w', linewidths=2)

# Add labels
for i, txt in enumerate(keywords):
    plt.annotate(txt, (x[i], y[i]), ha='center', va='center', 
                 fontsize=14, fontweight='bold', color='#333333')  # Increase the font size

# Set chart properties
plt.axis('equal')  # Ensure the bubbles are circular
plt.axis('off')    # Hide the axes
plt.title("Bubble Chart of Keyword Attention in the Teaching Industry", fontsize=18, pad=20)  # Increase the title font size

# Display the chart
plt.tight_layout()
plt.show()