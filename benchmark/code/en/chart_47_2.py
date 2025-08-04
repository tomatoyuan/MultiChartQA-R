import matplotlib.pyplot as plt

# Data
labels = ['Biotech Raw Materials', 'Beauty and Skincare Brands', 'Medical Technology', 'Others']
sizes = [42, 25, 20, 13]  # The values here are simulated. You can replace them with actual data, ensuring the sum is 100.
colors = ['#d9b3b3', '#f2d9a6', '#c7e0c3', '#d9d9d9']  # Custom colors

# Draw a pie chart
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
ax.set_title('Distribution of Domestic Beauty Investment and Financing Enterprises in 2024')

plt.show()