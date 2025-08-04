import matplotlib.pyplot as plt

# Data
countries = ["USA", "Japan", "Europe"]
percentages = [48, 45, 7]  
colors = ["pink", "lightgreen", "lightblue"]  

# Create a pie chart
plt.pie(
    percentages, 
    labels=countries, 
    colors=colors, 
    autopct="%1.1f%%",  # Display percentages
    startangle=90,      # Starting angle
    textprops={"fontsize": 12}
)

# Add a title
plt.title("Where to seek medical treatment overseas?", fontsize=16, fontweight="bold")

# Adjust the layout (to avoid label crowding)
plt.tight_layout()

# Display the chart
plt.show()