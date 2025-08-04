import matplotlib.pyplot as plt
import numpy as np

# 数据准备
constellations = [
    "金牛座", "水瓶座", "摩羯座", "狮子座", "双鱼座", "白羊座", "射手座", "巨蟹座",
    "天秤座", "双子座", "处女座", "天蝎座"
]
percentages = [4, 4, 7, 10, 5, 9, 6, 6, 6, 10, 18, 15]
# 为方便布局，手动设置各星座坐标（可根据设计微调）
coords = [
    (0.2, 0.8), (0.1, 0.6), (0.3, 0.4), (0.2, 0.2), (0.4, 0.1), (0.6, 0.2),
    (0.7, 0.3), (0.8, 0.5), (0.7, 0.7), (0.5, 0.8), (0.6, 0.6), (0.4, 0.7)
]
# 对应气泡颜色（示例配色，可自行调整）
colors = [
    "#D4AF37", "#ADD8E6", "#C0C0C0", "#87CEFA", "#F0E68C", "#90EE90",
    "#FFD700", "#FF6347", "#FFC0CB", "#BA55D3", "#FF69B4", "#1E90FF"
]
# 处女座特殊标注文本
virgo_text = "处女座虽高贵冷艳，\n最拿手的却是隐藏焦虑。"

# 创建画布
fig, ax = plt.subplots(figsize=(8, 8), facecolor='black')
ax.set_facecolor('black')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
# 隐藏坐标轴
ax.set_xticks([])
ax.set_yticks([])

# 绘制气泡 + 标注
for constellation, p, (x, y), color in zip(constellations, percentages, coords, colors):
    # 绘制气泡（散点图模拟）
    ax.scatter(
        x, y, 
        s=p * 120,  # 气泡大小与焦虑占比关联
        c=color, 
        alpha=0.8,
        edgecolors='white', 
        linewidths=1
    )
    # 绘制百分比文本
    text_color = 'white' if p != 18 else 'black'  # 处女座文本反色
    ax.text(
        x, y, 
        f"{p}%", 
        ha='center', 
        va='center', 
        fontsize=10, 
        color=text_color, 
        fontweight='bold'
    )
    # 绘制星座名称
    ax.text(
        x, y - 0.05, 
        constellation, 
        ha='center', 
        va='top', 
        fontsize=9, 
        color='white'
    )

# 处女座特殊说明文本
virgo_x, virgo_y = coords[constellations.index("处女座")]
ax.text(
    virgo_x, virgo_y - 0.18, 
    virgo_text, 
    ha='center', 
    va='bottom', 
    fontsize=10, 
    color='white', 
    linespacing=1.2,
    # 修复：将CSS颜色格式改为RGBA元组格式
    bbox=dict(facecolor=(1, 1, 1, 0.1), edgecolor='white', pad=5)
)

# 添加标题
ax.text(
    0.5, 0.95, 
    "十二星座最焦虑榜", 
    ha='center', 
    va='center', 
    fontsize=20, 
    color='white', 
    fontweight='bold'
)

plt.tight_layout()
plt.show()