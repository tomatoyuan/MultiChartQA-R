import matplotlib.pyplot as plt
import numpy as np

# 功能提升项
features = ["提升舒适性", "改善健康", "运动专业功能性"]
# 对应占比数据
percentages = [71, 57, 55]
# 用于在图表上显示 TOP 信息，这里根据索引对应设置
tops = ["TOP1", "TOP2", "TOP3"]

# 设置字体，确保中文显示正常（需根据自己环境调整字体路径或名称，这里以 SimHei 为例，若没有可替换为其他支持中文的字体）
plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示为方块的问题

y_pos = np.arange(len(features))  # y 轴位置

# 创建横向条形图
fig, ax = plt.subplots()
bars = ax.barh(y_pos, percentages, align='center', color=['#1f77b4', '#ff7f0e', '#2ca02c'])  # 设置颜色，尽量接近示例风格

# 在每个条形末端添加占比数值
for bar, percentage in zip(bars, percentages):
    length = bar.get_width()
    ax.text(length + 1,  # 数值显示位置的 x 坐标，可微调
            bar.get_y() + bar.get_height() / 2,  # 数值显示位置的 y 坐标，居中
            f'{percentage}%',
            va='center')

# 在每个条形右侧添加 TOP 信息
for i, (bar, top) in enumerate(zip(bars, tops)):
    length = bar.get_width()
    ax.text(length + 6,  # 可根据实际情况微调位置
            bar.get_y() + bar.get_height() / 2,
            top,
            va='center')

ax.set_yticks(y_pos)
ax.set_yticklabels(features)
ax.invert_yaxis()  # 让第一个功能项显示在最上方
ax.set_xlabel('占比（%）')
ax.set_title('消费者希望内衣实现的功能提升')

plt.show()