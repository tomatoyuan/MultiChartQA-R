import matplotlib.pyplot as plt

# Budget change categories
labels = ["Significantly Decreased", "Slightly Decreased", "Basically Unchanged", "Slightly Increased", "Significantly Increased"]
# Proportion of each category (%)
sizes = [10.5, 40.8, 34.9, 12.5, 1.3]
# Colors for each part of the pie chart
colors = ["#A4D68C", "#87D3F2", "#A4C639", "#74BCEF", "#F2D387"]

# Create a figure and a subplot
fig, ax = plt.subplots(figsize=(8, 8))

# Draw a pie chart
wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, autopct='%1.1f%%', 
    startangle=140, colors=colors, 
    textprops={'color': 'black'}
)

# Beautify the annotation text (adjust the size, etc.)
for text in texts + autotexts:
    text.set_fontsize(12)

# Set the title
ax.set_title("2022 Customer Budget Changes for Corporate Training", fontsize=14, fontweight="bold", y=1.05)

plt.tight_layout()  # Automatically adjust the layout
plt.show()