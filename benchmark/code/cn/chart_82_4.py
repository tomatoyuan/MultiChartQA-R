import matplotlib.pyplot as plt
import numpy as np

# 原因类别
reasons = [
    "年卡模式时间长，较难坚持",
    "对教练教学态度和能力不满意",
    "门店风格过时，吸引力不足",
    "年卡模式风险大，担心商家跑路",
    "经常发传单或推销，印象不好",
    "价格贵，对性价比不满意",
    "课程较同质化，不能满足需求",
    "关店跑路新闻常有，印象不好",
    "地理位置不方便"
]
# 对应占比（%），数据大体一致即可
percentages = [47.5, 43.0, 42.4, 41.1, 39.9, 38.0, 30.4, 21.5, 12.0]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制条形图（水平条形图，调整为与原图方向一致）
y = np.arange(len(reasons))
bar_width = 0.6
bars = ax.barh(y, percentages, height=bar_width, color="#A4C639")

# 添加数据标注
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # 标注位置调整
                textcoords="offset points",
                ha='left', va='center')

# 绘制Top5虚线边框（前5个条目）
for i in range(5):
    special_bar = bars[i]
    x0, y0 = special_bar.get_xy()
    width, height = special_bar.get_width(), special_bar.get_height()
    rect = plt.Rectangle((x0, y0), width, height, fill=False, edgecolor='green', linestyle='--')
    ax.add_patch(rect)

# 设置y轴刻度和标签（调整顺序，让第一个原因在最上方）
ax.set_yticks(y)
ax.set_yticklabels(reasons)
# 隐藏x轴刻度
ax.set_xticks([])
# 设置标题
ax.set_title("2022年中国健身房用户未选择传统健身房的原因", fontsize=14, fontweight="bold")

# 美化图表，隐藏顶部、右侧和底部边框
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()