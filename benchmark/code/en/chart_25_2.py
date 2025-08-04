import matplotlib.pyplot as plt

# Data
labels = ['25 - 34 years old', 'Under 19 years old', '19 - 24 years old', 'Over 35 years old']
sizes = [37, 28, 18, 17]

# Draw a pie chart
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Ensure the pie chart is a perfect circle

# Add a title
ax.set_title('Age ratio of people concerned about "Spring Festival Ritual Sense"')

# Display the chart
plt.show()