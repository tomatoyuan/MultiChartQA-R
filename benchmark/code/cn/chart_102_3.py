import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 构建数据
data = {
    '平台': ['抖音', '快手', '小红书', 'B站', '微博', '秒拍', '皮皮虾', '西瓜视频', '微信视频号'],
    '1分': [2.1, 2.37, 3.22, 4.56, 2.08, 3.54, 3.03, 4.17, 3.03],
    '2分': [5.01, 8.91, 7.07, 6.46, 8.33, 13.27, 14.39, 13.33, 7.74],
    '3分': [13.67, 20.77, 11.58, 16.35, 26.39, 23.01, 22.73, 15.83, 19.19],
    '4分': [40.09, 35.01, 40.83, 32.71, 29.17, 31.86, 33.33, 36.67, 36.36],
    '5分': [38.50, 32.94, 37.30, 39.92, 34.03, 28.32, 26.52, 30.00, 33.68]
}

df = pd.DataFrame(data)
# 将“平台”列设为索引，方便后续绘图按平台展示
df.set_index('平台', inplace=True)

# 定义颜色，与图表中的颜色对应
colors = ['#FF5733', '#3498DB', '#2ECC71', '#9B59B6', '#E74C3C']
columns = df.columns

fig, ax = plt.subplots(figsize=(10, 6))
bottom = np.zeros(len(df))

for i, col in enumerate(columns):
    ax.bar(df.index, df[col], bottom=bottom, color=colors[i], label=col)
    bottom += df[col]
    # 标注数值
    for x, y in zip(df.index, bottom - df[col] / 2):
        ax.text(x, y, f'{df[col][x]}', ha='center', va='center')

ax.set_ylabel('百分比（%）')
ax.set_title('2025年中国用户对短视频平台总体使用满意度评分')
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()