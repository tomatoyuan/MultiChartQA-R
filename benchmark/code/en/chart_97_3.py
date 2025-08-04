import matplotlib.pyplot as plt

# Classification and proportion of years of watching games (simulated data, similar to the original image)
labels = ["Over 5 years", "2 - 5 years", "Within 2 years"]
sizes = [89.9, 7.6, 2.5]
# Free color matching (adjustable)
colors = ["#A4C639", "#87CEEB", "#FFD700"]

# Create a canvas
fig, ax = plt.subplots(figsize=(6, 6))

# Draw a pie chart
wedges, texts, autotexts = ax.pie(
    sizes, 
    labels=labels, 
    colors=colors, 
    autopct='%1.1f%%', 
    startangle=90,
    wedgeprops=dict(width=0.3, edgecolor='white')  # Ring - shaped pie chart effect (optional, can be deleted for a solid pie chart)
)

# Set the title
ax.set_title("Years of watching football games of Chinese football fans in 2022", fontsize=14, fontweight="bold", y=1.05)

# Beautify the annotations (color, size)
for text, autotext in zip(texts, autotexts):
    text.set_color('black')
    autotext.set_color('black')
    autotext.set_fontsize(10)

# Hide the border (the pie chart has no actual border, just for layout standardization)
for spine in ax.spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()