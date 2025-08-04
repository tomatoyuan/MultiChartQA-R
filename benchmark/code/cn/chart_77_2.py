import matplotlib.pyplot as plt
import numpy as np

# 业绩变化类别
categories = ["增长20%以上", "增长20%以内", "下降20%以内", "下降20%以上"]
# 在线学习机构数据（%），数据大体一致即可
online = [51, 31, 16, 2]
# 培训供应商数据（%），数据大体一致即可
supplier = [16, 31, 43, 11]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制分组柱状图
x = np.arange(len(categories))
bar_width = 0.35
online_bars = ax.bar(x - bar_width/2, online, width=bar_width, color="#C68439", label="在线学习机构")
supplier_bars = ax.bar(x + bar_width/2, supplier, width=bar_width, color="#64B5F6", label="培训供应商")

# 添加在线学习机构数据标注
for bar in online_bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom')

# 添加培训供应商数据标注
for bar in supplier_bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom')

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(categories)
# 设置y轴标签
ax.set_ylabel("占比（%）")
# 设置标题
ax.set_title("2021年在线学习机构与培训供应商的业绩情况", fontsize=14, fontweight="bold")

# 添加图例
ax.legend()

# 美化图表，隐藏顶部和右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()