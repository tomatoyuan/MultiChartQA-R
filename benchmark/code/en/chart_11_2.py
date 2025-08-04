import matplotlib.pyplot as plt

# Data
labels = ["Yes", "No"]
sizes = [39, 61]
# Colors for each part of the pie chart, can be adjusted as needed
colors = ["#87E8DE", "#FF6B6B"]  

# Create a pie chart
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90, colors=colors)
# Set the title
ax.set_title("Will you check exam scores with your parents?")
# Ensure the pie chart is a perfect circle
ax.axis("equal")  

# Display the chart
plt.show()