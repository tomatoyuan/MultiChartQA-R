import matplotlib.pyplot as plt
import numpy as np

# 购买考虑因素
factors = [
    "口感", "麦芽汁浓度", "口碑评价", "酒精度数", "酿造原料",
    "香气/色泽", "品牌知名度", "酿造工艺", "性价比", "泡沫丰富度",
    "新口味/新品尝类", "购买便捷度", "保质期", "酒瓶/包装颜值",
    "广告代言人等", "限定产品/联名产品", "KOL推荐"
]
# 各因素占比（%），数据与图表一致
percentages = [
    38.4, 31.3, 29.4, 28.1, 27.3,
    27.0, 26.5, 25.8, 24.8, 22.7,
    20.5, 20.0, 17.9, 16.5,
    12.3, 11.4, 11.1
]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(12, 6))

# 绘制柱状图
x = np.arange(len(factors))
bar_width = 0.6
bars = ax.bar(x, percentages, width=bar_width, color="#A4C639")

# 给“口感”“麦芽汁浓度”添加蓝色边框
for i in range(2):
    bars[i].set_edgecolor('blue')
    bars[i].set_linewidth(2)

# 添加数据标注
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom',
                color="#A4C639")

# 设置x轴刻度和标签，旋转标签方便显示
ax.set_xticks(x)
ax.set_xticklabels(factors, rotation=45, ha='right')
# 设置y轴标签
ax.set_ylabel("占比（%）")
# 设置标题
ax.set_title("啤酒购买考虑因素", fontsize=14, fontweight="bold")

# 美化图表，隐藏顶部和右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()