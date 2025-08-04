# Chart 4 (Re - optimization): Add English labels and percentage values next to each sector to improve readability

labels = [
    "Sophisticated Moms", "Small Town Youths", "Senior Middle - Class", "New - Generation White - Collars",
    "Small Town Seniors", "Gen Z", "Urban Seniors", "Urban Blue - Collars", "Senior Blue - Collars"
]
sizes = [22, 20, 19, 16, 9, 8, 3, 2, 1]
import matplotlib.pyplot as plt
import numpy as np
colors = plt.cm.PuRd(np.linspace(0.2, 0.9, len(labels)))

fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops=dict(width=0.7),
    textprops=dict(color="black", fontsize=9)
)

# Beautify the title
ax.set_title("Shark Pants Population Preference Distribution (Descending by Proportion)", fontsize=13)

plt.tight_layout()
plt.show()