import matplotlib.pyplot as plt
import numpy as np

# 使用您提供的精确数据
dates = [f"5/{i}" for i in range(1, 32)]
values = [
    7200000, 7000000, 7800000, 6800000, 6500000, 6800000, 7000000, 6200000, 
    6500000, 5800000, 7000000, 500000, 7200000, 3500000, 4000000, 3000000, 
    3500000, 4500000, 5200000, 4800000, 4500000, 4300000, 5000000, 5500000, 
    6000000, 6200000, 6800000, 6000000, 6500000, 7000000, 7500000
]

# 创建画布
fig, ax = plt.subplots(figsize=(10, 5))  # 稍微加宽画布以容纳更多数据点

# 绘制折线图，颜色和线宽匹配原图
ax.plot(dates, values, color="#4285f4", linewidth=2.5)

# 设置标题
ax.set_title("5月医疗美容行业资讯关注度趋势", fontsize=14, fontweight="bold")

# 设置纵轴（关注度）
ax.set_ylabel("关注度", fontsize=12)
ax.set_ylim(0, 9000000)  # 匹配原图纵轴范围
ax.set_yticks(np.arange(0, 10000000, 1000000))  # 纵轴刻度间隔100万

# 设置横轴（日期）- 每3天显示一个刻度
ax.set_xticks(np.arange(0, len(dates), 3))  # 每隔3天显示一个刻度
ax.set_xticklabels([dates[i] for i in range(0, len(dates), 3)], rotation=45, ha="right")  # 旋转45度避免重叠

# 添加网格线
ax.grid(linestyle="--", color="gray", alpha=0.5)

# 优化布局
plt.tight_layout()

# 显示图表
plt.show()