import matplotlib.pyplot as plt
# Data
labels = ["Spending a lot of energy and time in searching for healthy ingredients without clear label instructions",
          "Worried about excessive food additives",
          "Unable to judge whether instant foods or takeaways are healthy",
          "Difficulty in finding a long - term reliable purchasing channel",
          "Worrying about the calorie content of each food and afraid of gaining weight"]
percentages = [60, 55, 47, 44, 18]

# Create a plotting object
fig, ax = plt.subplots()

# Draw a horizontal bar chart
ax.barh(labels, percentages, color='green')

# Add percentage labels
for i, v in enumerate(percentages):
    ax.text(v + 1, i, f'{v}%', va='center')

# Set the title and axis labels (adjust as needed)
ax.set_title('Concerns about healthy ingredients')

# Display the chart
plt.show()