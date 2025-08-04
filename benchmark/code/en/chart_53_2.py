import matplotlib.pyplot as plt

# -------------------- Data Definition --------------------
labels = ["Whey Protein", "Plant and Mixed Protein"]
sizes = [70.4, 29.6]  # Proportion data

# -------------------- Color Scheme: Warm Tones --------------------
colors = ["#ffb74d", "#e57373"]  # Orange + Red

# -------------------- Create a Canvas --------------------
fig, ax = plt.subplots(figsize=(6, 6))

# -------------------- Draw a Donut Chart --------------------
wedges, text_labels, auto_texts = ax.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",
    startangle=90,
    colors=colors,
    textprops={"fontsize": 12, "color": "#424242"},
    wedgeprops={"linewidth": 2, "edgecolor": "white"}
)

# Add a central circle to create a "hollow" effect
centre_circle = plt.Circle((0, 0), 0.4, fc="white")
fig.gca().add_artist(centre_circle)

# Beautify the percentage text
for text in auto_texts:
    text.set_color("white")
    text.set_fontweight("bold")

# -------------------- Add a Title --------------------
ax.set_title(
    "Proportion of Whey Protein in the Total Sales Volume of Protein Powders",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# -------------------- Optimize the Layout --------------------
plt.tight_layout()
plt.show()