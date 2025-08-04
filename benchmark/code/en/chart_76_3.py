import matplotlib.pyplot as plt

# Application categories
labels = [
    "Video Services", "Communication and Chat", "Comprehensive Information", 
    "Game Services", "Social Networks", "E-commerce", 
    "Utility Tools", "Others"
]
# Proportion of usage time for each application (%)
sizes = [43.9, 19.7, 7.3, 5.8, 4.1, 3.7, 3.6, 11.9]
# Colors for each part of the pie chart
colors = [
    "#A4C639", "#A4D68C", "#BCE1A3", 
    "#87D3F2", "#74BCEF", "#F2D387", 
    "#F2B987", "#ECECEC"
]

# Create a canvas and a sub - plot
fig, ax = plt.subplots(figsize=(8, 8))

# Draw a pie chart
wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, autopct='%1.1f%%', 
    startangle=140, colors=colors, 
    textprops={'color': 'black'}
)

# Beautify the annotation text (adjust size, color, etc.)
for text in texts + autotexts:
    text.set_fontsize(12)

# Simulate a green outer border
for spine in ax.spines.values():
    spine.set_color('#A4C639')
    spine.set_linewidth(2)

# Set the title
ax.set_title("mUserTracker - Q1 2022 User Application Usage Time Distribution", fontsize=14, fontweight="bold", y=1.05)

plt.tight_layout()  # Automatically adjust the layout
plt.show()