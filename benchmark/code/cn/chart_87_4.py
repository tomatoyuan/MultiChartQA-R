import matplotlib.pyplot as plt
import numpy as np

# 功能期待项
functions = [
    "准确率高",
    "检查结果分析全面",
    "快速了解眼健康情况",
    "为眼健康问题提出预警",
    "提供后续眼健康解决方案",
    "有健康跟踪档案",
    "记录每次筛查结果",
    "检查方式便捷",
    "检查速度快",
    "提供线上报告解读服务",
    "检查项目多"
]
# 对应占比（%），数据与图表一致
percentages = [40.9, 40.3, 37.1, 36.4, 35.8, 34.4, 33.9, 27.6, 27.0, 26.9, 22.1]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(8, 7))

# 绘制水平条形图
y = np.arange(len(functions))
bar_width = 0.6
bars = ax.barh(y, percentages, height=bar_width, color="#395AC6")

# 添加数据标注
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # 标注位置调整
                textcoords="offset points",
                ha='left', va='center')

# 设置y轴刻度和标签（调整顺序，让第一个功能在最上方）
ax.set_yticks(y)
ax.set_yticklabels(functions)
# 隐藏x轴刻度
ax.set_xticks([])
# 设置标题
ax.set_title("家长对儿童青少年视觉健康类产品功能的期待", fontsize=14, fontweight="bold")

# 美化图表，隐藏顶部、右侧和底部边框
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()