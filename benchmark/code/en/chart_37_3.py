import matplotlib.pyplot as plt
import numpy as np

# Data preparation (rough simulation, can be fine - tuned according to actual situation)
categories = [
    ["Windbreakers and Windpants", "Sports Down Jackets"],
    ["Tang-style Clothing/Chinese-style Clothing", "Intangible Cultural Heritage/Textile and Dyeing Clothing"],
    ["Anime Shirts", "Anime Dresses"]
]
groups = ["Outdoor Sports", "Chinese Style Clothing", "Anime Clothing"]
values = [
    [27, 46],
    [123, 78],
    [200, 93]
]

# Color configuration (similar to the light color scheme of the original chart)
bar_colors = ["#C9B8A7", "#B8A090"]  # Can be fine - tuned according to actual needs

# Initialize the plot
fig, axes = plt.subplots(3, 1, figsize=(6, 10), sharex=False)  # Adjust the height to accommodate the title
plt.subplots_adjust(top=0.85, hspace=0.5)  # Adjust the top spacing

# Add the main title and subtitle
plt.suptitle("Growth Rate of Clothing Categories Related to Interest Circles", fontsize=16, fontweight="bold", y=0.95)
plt.title("Year - on - Year Growth Percentage of Sales of Each Category", fontsize=12, y=1.05)  # Subtitle

for i in range(3):
    # Draw horizontal bar charts
    axes[i].barh(categories[i], values[i], color=bar_colors)
    axes[i].set_title(groups[i], fontsize=12, fontweight="bold")  # Set the group title

    # Add data labels (growth rate in +% format)
    for j, val in enumerate(values[i]):
        axes[i].text(val + 5, categories[i][j], f"{val}%+", 
                     va="center", fontsize=9, color="black")

# Uniformly set the axes (hide the x - axis ticks to make the chart cleaner)
for ax in axes:
    ax.set_xticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

plt.show()