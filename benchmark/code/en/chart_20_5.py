import matplotlib.pyplot as plt

# Data
labels = ['Buy Insurance', 'Seek Medical Appointment', 'Look for Folk Remedies', 'Pray to Gods', 'Others']
sizes = [43, 18, 18, 21, 0]  # Proportions of each part, the sum is 100, can be adjusted as needed
colors = ['#FFA07A', '#90EE90', '#FFC0CB', '#87CEFA', '#D3D3D3']  # Colors of each part, can be customized

# Draw a pie chart
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Ensure the pie chart is a perfect circle

# Add a title
plt.title('Subsequent Behaviors of Cancer Patients')

# Display the chart
plt.show()