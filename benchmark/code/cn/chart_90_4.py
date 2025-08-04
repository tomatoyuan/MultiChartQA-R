import matplotlib.pyplot as plt
import numpy as np

# 啤酒卖点
selling_points = [
    "口感更丰富", "高浓度麦芽汁", "传统工艺酿造", 
    "纯净的配料表", "成分天然", "酒精度数低，不上头", 
    "轻负担，如低卡、低脂、低糖", "保质期更短、更新鲜", 
    "高科技工艺酿造", "高颜值的酒体"
]
# 各卖点占比（%），数据与图表一致
percentages = [32.0, 26.0, 24.4, 23.0, 22.9, 22.4, 19.6, 19.2, 18.4, 16.0]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制水平柱状图
y = np.arange(len(selling_points))
bar_width = 0.6
bars = ax.barh(y, percentages, height=bar_width, color="#C6AE39")

# 添加数据标注
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # 标注位置调整
                textcoords="offset points",
                ha='left', va='center')

# 设置y轴刻度和标签
ax.set_yticks(y)
ax.set_yticklabels(selling_points)
# 设置x轴标签
ax.set_xlabel("愿意支付更高价格的啤酒卖点（%）")
# 设置标题
ax.set_title("愿意支付更高价格的啤酒卖点-TOP 10", fontsize=14, fontweight="bold")

# 美化图表，隐藏顶部和右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()