import matplotlib.pyplot as plt
import numpy as np

# Pie chart data on the left
pie_labels = ["Focused on", "Seen but not deeply understood", "Not concerned"]
pie_sizes = [53.4, 42.2, 4.4]
pie_colors = ["#FF9933", "#B34D4D", "#4D88B3"]

# Bar chart data on the right
bar_channels = ["E - commerce platforms", "Social platforms", "Short - video platforms", 
                "Content sharing platforms", "Offline specialty stores", 
                "Smart product exhibitions", "Informed by friends/relatives/classmates", "Others"]
bar_proportions = [60.2, 53.4, 41.4, 41.2, 32.5, 17.1, 9.6, 0.4]

fig = plt.figure(figsize=(16, 6))
# Left sub - plot
ax1 = fig.add_subplot(121)
wedges, texts, autotexts = ax1.pie(pie_sizes, labels=pie_labels, colors=pie_colors, autopct="%1.1f%%", 
                                   startangle=90, hatch="////")
for autotext in autotexts:
    autotext.set_color("black")
ax1.set_title("Chinese consumers' understanding of small - screen mobile phones")

# Right sub - plot
ax2 = fig.add_subplot(122)
x = np.arange(len(bar_channels))
bars = ax2.bar(x, bar_proportions, color="#FF9933", hatch="////")
for i, proportion in enumerate(bar_proportions):
    ax2.text(i, proportion + 1, f"{proportion}%", ha="center", va="bottom")
ax2.set_ylabel("Proportion (%)")
ax2.set_xlabel("Understanding channels")
ax2.set_xticks(x)
ax2.set_xticklabels(bar_channels, rotation=45, ha="right")
ax2.set_title("Channels through which Chinese consumers understand small - screen mobile phones")

plt.tight_layout()
plt.show()