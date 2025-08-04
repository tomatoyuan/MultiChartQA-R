import matplotlib.pyplot as plt
import numpy as np

# Information acquisition channels
channels = ["Content community platforms (e.g., Xiaohongshu)", "E-commerce platforms (e.g., Taobao, JD.com)",
            "Social media platforms (e.g., WeChat)", "Maternal and infant vertical platforms (e.g., Mama.cn)",
            "Short - video platforms (e.g., Douyin)", "Video - sharing platforms (e.g., Bilibili)"]
# Reasons for each choice (legend order)
reasons = ["High professionalism (experts/Q&A)", "Reliable maternal and infant information",
           "Frequent user interaction", "Following recommendations from people around", "Personal habit",
           "Preference for convenience"]
# Corresponding colors
colors = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63', '#1E90FF']
# Proportion data for each reason under each channel (in the order of channels and reasons)
data = np.array([
    [7.74, 14.26, 15.48, 12.83, 8.15, 4.07],
    [5.91, 17.52, 11.41, 13.65, 7.74, 4.68],
    [8.35, 12.83, 13.65, 9.98, 7.94, 2.24],
    [11.20, 14.87, 14.26, 10.59, 9.16, 3.46],
    [5.30, 11.00, 13.65, 9.57, 9.98, 4.48],
    [6.52, 13.24, 12.63, 12.42, 8.96, 3.87]
])

x = np.arange(len(channels))  # x-axis corresponds to different channels
bar_width = 0.8  # Bar width

fig, ax = plt.subplots(figsize=(14, 8))
bottom = np.zeros(len(channels))

for i, reason in enumerate(reasons):
    # Traverse each reason and draw a stacked bar chart
    ax.bar(channels, data[:, i], width=bar_width, bottom=bottom, color=colors[i], label=reason)
    # Add numerical annotations
    for j in range(len(channels)):
        ax.text(j, bottom[j] + data[j, i] / 2, f'{data[j, i]:.2f}', ha='center', va='center', fontsize=8)
    bottom += data[:, i]

ax.set_ylabel('Proportion (%)')
ax.set_title('Reasons for Chinese maternal and infant consumers to choose information acquisition channels in 2025')
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # Place the legend on the right
plt.xticks(x, channels, rotation=45, ha='right')
plt.tight_layout()
plt.show()