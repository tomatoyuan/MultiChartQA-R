import matplotlib.pyplot as plt
import numpy as np

# Stage names
stages = ["Pre - pregnancy", "Pregnancy", "Parenting"]
# Corresponding information categories of each stage (sorted according to the legend, need to correspond to the actual data)
categories = ["Pre - pregnancy preparation knowledge", "Pre - pregnancy nutrition", "Pre - pregnancy monitoring",
              "Pregnancy maintenance", "Maternity clothing", "Fetal development record",
              "Pregnancy diet recipes", "Delivery knowledge", "Infant clothing/products",
              "Baby food", "Postpartum care products/courses"]
# Simulated data (need to be replaced with actual complete data, here the sub - list of each stage corresponds to the proportion in the order of categories)
# In actual use, the proportion values of each stage and category need to be accurately filled according to the chart
data = {
    "Pre - pregnancy": [1.43, 15.89, 21.38, 23.63, 21.59, 21.18, 18.33, 16.09, 14.66, 8.76, 5.91],
    "Pregnancy": [7.33, 12.22, 21.38, 31.77, 22.00, 23.83, 23.83, 15.89, 10.79, 6.52, 2.24],
    "Parenting": [4.48, 9.57, 15.27, 20.98, 20.98, 20.98, 17.92, 13.85, 18.33, 15.48, 8.15]
}
# Corresponding colors (need to be accurately matched according to the chart legend, here is just an example, the actual is based on the chart)
colors = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63',
          '#00BFFF', '#FFD700', '#1E90FF', '#FF69B4', '#00FA9A', '#FFA07A']

x = np.arange(len(stages))  # The x - axis corresponds to three stages
bar_width = 0.8  # Bar width

fig, ax = plt.subplots(figsize=(12, 8))
bottom = np.zeros(len(stages))

for i, category in enumerate(categories):
    # Traverse each category of concerned information and draw stacked columns
    ax.bar(stages, [data[stage][i] for stage in stages], width=bar_width,
           bottom=bottom, color=colors[i], label=category)
    # Add numerical annotations (just an example, if there is a lot of data, it may overlap, and the position, font size, etc. can be adjusted as needed)
    for j in range(len(stages)):
        ax.text(j, bottom[j] + data[stages[j]][i] / 2,
                f'{data[stages[j]][i]:.2f}', ha='center', va='center', fontsize=7)
    bottom += [data[stage][i] for stage in stages]

ax.set_ylabel('Proportion (%)')
ax.set_title('Key information concerned by Chinese maternal and infant consumers in each stage in 2025')
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # Place the legend on the right to avoid occlusion
plt.xticks(x, stages)
plt.tight_layout()
plt.show()