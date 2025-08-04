import matplotlib.pyplot as plt

# Data
labels = ["China", "Europe", "North America", "Japan", "Others"]
sizes = [65, 9, 8, 7, 10]
# Color settings, as close to the original image as possible
colors = ["#A4C639", "#8EBF8F", "#87CEEB", "#ADD8E6", "#FFD700"]  

# Create a canvas
fig, ax = plt.subplots(figsize=(6, 5))

# Draw a pie chart
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",  
    startangle=90,     
    colors=colors,
    textprops={"color": "black"}
)

# Set the title, simulate the top green background title (implemented with a normal title + position adjustment)
ax.set_title("Global Stainless Steel Vacuum Flask Production Share", fontsize=14, fontweight="bold", y=1.08, backgroundcolor="#8EBF8F", pad=8)

# Beautify: keep the pie chart circular
ax.axis("equal")

plt.tight_layout()
plt.show()