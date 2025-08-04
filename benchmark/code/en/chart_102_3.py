import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Build data
data = {
    'Platform': ['Douyin', 'Kuaishou', 'Xiaohongshu', 'Bilibili', 'Weibo', 'Miaopai', 'Pipixia', 'Xigua Video', 'WeChat Video Account'],
    '1 Score': [2.1, 2.37, 3.22, 4.56, 2.08, 3.54, 3.03, 4.17, 3.03],
    '2 Score': [5.01, 8.91, 7.07, 6.46, 8.33, 13.27, 14.39, 13.33, 7.74],
    '3 Score': [13.67, 20.77, 11.58, 16.35, 26.39, 23.01, 22.73, 15.83, 19.19],
    '4 Score': [40.09, 35.01, 40.83, 32.71, 29.17, 31.86, 33.33, 36.67, 36.36],
    '5 Score': [38.50, 32.94, 37.30, 39.92, 34.03, 28.32, 26.52, 30.00, 33.68]
}

df = pd.DataFrame(data)
# Set the 'Platform' column as the index for subsequent plotting by platform
df.set_index('Platform', inplace=True)

# Define colors corresponding to those in the chart
colors = ['#FF5733', '#3498DB', '#2ECC71', '#9B59B6', '#E74C3C']
columns = df.columns

fig, ax = plt.subplots(figsize=(12, 6))  # 调整图形宽度以适应外侧图例
bottom = np.zeros(len(df))

for i, col in enumerate(columns):
    ax.bar(df.index, df[col], bottom=bottom, color=colors[i], label=col)
    bottom += df[col]
    # Annotate the values
    for x, y in zip(df.index, bottom - df[col] / 2):
        ax.text(x, y, f'{df[col][x]}', ha='center', va='center')

ax.set_ylabel('Percentage (%)')
ax.set_title('Overall Satisfaction Ratings of Chinese Users for Short - Video Platforms in 2025')

# 将图例移至图表右侧外侧
ax.legend(bbox_to_anchor=(1.01, 1), loc='upper left')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()