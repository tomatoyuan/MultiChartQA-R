import matplotlib.pyplot as plt
import numpy as np

# 类别
categories = ["花胶", "海参", "猪蹄", "燕窝"]
# 胶原蛋白含量（%），数据大体一致即可
collagen_content = [84.0, 54.2, 11.1, 1.5]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(6, 5))

# 绘制柱状图
x = np.arange(len(categories))
bar_width = 0.6
bars = ax.bar(x, collagen_content, width=bar_width, color="#A4C639", label="胶原蛋白含量（%）")

# 添加数据标注
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom')

# 添加底部说明文本
ax.text(0.5, -0.25, "● 胶原蛋白含量是猪蹄的7倍+", 
        ha='center', va='bottom', fontsize=10, color='green')

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(categories)
# 设置y轴标签
ax.set_ylabel("胶原蛋白含量（%）")
# 设置标题
ax.set_title("花胶的胶原蛋白含量", fontsize=14, fontweight="bold")

# 添加图例
ax.legend()

# 美化图表，隐藏顶部和右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()