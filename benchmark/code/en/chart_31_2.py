import matplotlib.pyplot as plt

# Gender ratio data
labels = ["Female", "Male", "Other (e.g., crawlers)"]
sizes = [57, 40, 3]  # Adjusted the ratio of "Other" to ensure the total is 100%
colors = ["#FFC0CB", "#87CEEB", "#D3D3D3"]  # Pink (Female), Light blue (Male), Light gray (Other)

# Create a canvas
plt.figure(figsize=(8, 8))

# Draw a pie chart
plt.pie(sizes, 
        labels=labels, 
        autopct='%1.1f%%',  # Display percentage
        startangle=140,  # Starting angle
        colors=colors,
        explode=(0, 0, 0.1),  # Highlight the "Other" category
        shadow=True,  # Add shadow
        textprops={'fontsize': 12}  # Set text size
       )

# Set the title and display in equal proportion
plt.title("Gender Ratio of Campus Loan Search Users", fontsize=16)
plt.axis('equal')  # Ensure the pie chart is a perfect circle

# Display the graph
plt.tight_layout()
plt.show()