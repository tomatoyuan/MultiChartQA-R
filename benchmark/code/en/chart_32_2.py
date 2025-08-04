import matplotlib.pyplot as plt

# Data
labels = ['19-34 years old', '≤18 years old', 'Others']
sizes = [83, 13, 4]  # Assume the proportion of "Others" is 4%, which can be adjusted according to the actual accurate data
colors = ['pink', 'blue', 'lightcoral']

# Draw a pie chart
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Ensure the pie chart is a perfect circle

# Add a title
plt.title('Proportion of different age groups searching for "Teacher Qualification Certificate"')

# Display the chart
plt.show()