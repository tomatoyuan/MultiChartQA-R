import matplotlib.pyplot as plt
import numpy as np

# Short video platform names
platforms = ["Douyin", "Kuaishou", "Xiaohongshu", "WeChat Video Account", "Bilibili", "Xigua Video", "Weibo", "Pipixia", "Miaopai"]
# User usage percentages (%) of each platform
percentages = [46.80, 35.93, 33.16, 31.66, 28.04, 25.59, 15.35, 14.07, 12.05]

x = np.arange(len(platforms))  # Used to set the x-axis position of the bar chart

fig, ax = plt.subplots()
bars = ax.bar(x, percentages, color='orange')

# Label the value on each bar
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2., height,
            f'{height}',
            ha='center', va='bottom')

# Set the x-axis tick labels to platform names with even spacing
plt.xticks(x, platforms, rotation=45, ha='right')  # 使用 plt.xticks 确保均匀分布
# Set the chart title and axis labels
ax.set_title('Short video platforms used by Chinese users in 2025')
ax.set_ylabel('Percentage (%)')

plt.tight_layout()  # 确保布局紧凑，避免标签被截断
plt.show()