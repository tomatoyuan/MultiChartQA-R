import matplotlib.pyplot as plt

# -------------------- Data Definition --------------------
labels = ['1 - 500,000 yuan (units)', '500,001 - 999,999 yuan (units)', '1,000,000 yuan and above (units)']
sizes = [95, 3, 2]  # Proportion
absolute_values = [950, 30, 20]  # Assumed real quantities (optional)

# New color scheme (enhanced readability and aesthetics)
colors = ['#ff6f91', '#845ec2', '#88ccf1']

# -------------------- Create Canvas --------------------
fig, ax = plt.subplots(figsize=(7, 6))

# -------------------- Draw Donut Chart (Pie Chart + Central Hole) --------------------
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops=dict(width=0.6, edgecolor='white')  # Donut shape + White border
)

# -------------------- Adjust Text Style --------------------
for i, autotext in enumerate(autotexts):
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(10)

# -------------------- Add Central Annotation --------------------
total = sum(absolute_values)
ax.text(
    0, 0,
    f"Total\n{total} units",
    ha='center', va='center',
    fontsize=12,
    fontweight='bold',
    color="#424242"
)

# -------------------- Add Title --------------------
ax.set_title(
    "Distribution of Equipment Units Worth Over 10,000 Yuan in Chinese Rehabilitation Hospitals in 2020 (Donut Chart)",
    fontsize=14,
    fontweight='bold',
    pad=20
)

# -------------------- Layout Optimization and Display --------------------
plt.tight_layout()
plt.show()