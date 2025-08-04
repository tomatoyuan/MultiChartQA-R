import matplotlib.pyplot as plt
import numpy as np

# 电视剧名称
labels = ["国家公诉", "绝对权力", "我主沉浮", "国家干部"]
# 搜索指数数据
values = [526.24, 183.28, 128.79, 111.05]
# 用于在 x 轴上定位每个温度计
x_positions = np.arange(len(labels))  

# 创建画布和子图
fig, axes = plt.subplots(1, len(labels), figsize=(12, 5), sharey=True)

# 温度计的最大刻度（可根据数据调整，这里设为 600 方便展示）
max_temp = 600  
for i in range(len(labels)):
    ax = axes[i]
    # 绘制温度计外框（矩形模拟，这里简化处理，用竖线等也可，更复杂的可自定义形状）
    # 先画温度计的“玻璃管”，用白色填充背景模拟
    ax.bar(0, max_temp, width=0.5, color='white', edgecolor='black')
    # 绘制红色的“水银”部分，高度为对应的数据值
    ax.bar(0, values[i], width=0.5, color='red')
    # 设置 y 轴范围
    ax.set_ylim(0, max_temp)
    # 隐藏 x 轴刻度
    ax.set_xticks([])  
    # 添加电视剧名称作为标题
    ax.set_title(labels[i], y=-0.2)  
    # 在温度计上方显示百分比数值
    ax.text(0, values[i] + 10, f"{values[i]}", ha='center')  

# 整体标题
fig.suptitle("《人民的名义》播放后热门电视剧搜索指数对比", fontsize=16, y=1.05)
# 调整布局
plt.tight_layout()
# 显示图表
plt.show()