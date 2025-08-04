import matplotlib.pyplot as plt
import numpy as np

# 数据准备
channels = [
    ("线下零售", 50.2, "#FF6347"),
    ("熟人推荐", 36.4, "#FFD700"),
    ("传统广告", 40.6, "#FFDAB9"),
    ("内容分享类平台", 24.0, "#F4A460"),
    ("短视频平台", 42.3, "#FFB6C1"),
    ("电商平台", 49.6, "#FFA07A"),
]

# 六边形布局坐标（手动调整让布局近似原图）
hex_coords = [
    (0, 1),   # 线下零售
    (1, 0),   # 熟人推荐
    (1, -1),  # 传统广告
    (0, -2),  # 内容分享类平台
    (-1, -1), # 短视频平台
    (-1, 0),  # 电商平台
]

fig, ax = plt.subplots(figsize=(8, 7))
ax.set_xlim(-2, 2)
ax.set_ylim(-3, 2)
ax.axis('off')  # 隐藏坐标轴

# 绘制六边形并添加文本
for (channel, perc, color), (x, y) in zip(channels, hex_coords):
    # 绘制六边形（用多边形模拟）
    hexagon = plt.Circle((x, y), 0.4, color=color, alpha=0.8)
    ax.add_artist(hexagon)
    # 添加渠道名称和百分比
    ax.text(x, y + 0.1, channel, ha='center', va='bottom', fontsize=10)
    ax.text(x, y - 0.1, f'{perc}%', ha='center', va='top', fontsize=9, color='white')

# 标题
ax.text(0, 1.8, '2023年中国消费者化妆品信息渠道调查', ha='center', fontsize=12, fontweight='bold')
ax.text(0, 1.5, 'Survey on the Information Channels of Cosmetics of Consumers in China in 2023', 
        ha='center', fontsize=10, color='gray')

plt.tight_layout()
plt.show()