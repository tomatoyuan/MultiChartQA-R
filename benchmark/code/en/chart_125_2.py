import matplotlib.pyplot as plt
import numpy as np

# Left pie chart data
pie_labels = ["Two years", "Three years", "Four years and above", "Within one year"]
pie_sizes = [49.0, 33.7, 9.3, 8.0]
pie_colors = ["#8B4513", "#FFA07A", "#32CD32", "#FF8C00"]

# Right bar chart data
bar_factors = ["Performance", "Screen size", "Battery life", "Brand", "RAM", "Price", "Camera function", "Storage capacity", "Other"]
bar_proportions = [57.6, 57.0, 54.2, 47.2, 41.8, 38.4, 34.3, 31.1, 0.2]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Left pie chart
wedges, texts, autotexts = ax1.pie(pie_sizes, labels=pie_labels, colors=pie_colors, autopct="%1.1f%%", startangle=90)
for autotext in autotexts:
    autotext.set_color("white")
ax1.set_title("Replacement frequency of mobile phones by Chinese consumers")

# Right bar chart
x = np.arange(len(bar_factors))
bars = ax2.bar(x, bar_proportions, color="#FF8C00")
for i, proportion in enumerate(bar_proportions):
    ax2.text(i, proportion + 1, f"{proportion}%", ha="center", va="bottom")
ax2.set_ylabel("Proportion (%)")
ax2.set_xlabel("Consideration factors")
ax2.set_xticks(x)
ax2.set_xticklabels(bar_factors, rotation=45)
ax2.set_title("Factors considered by Chinese consumers when choosing mobile phones")

plt.tight_layout()
plt.show()