import matplotlib.pyplot as plt
import numpy as np

# 学历分类
education = ["高中及以下", "大学专科", "大学本科", "硕士/MBA及以上"]
# 模拟占比数据（贴近原图）
percentages = [15.0, 19.0, 54.3, 11.7]
# 自由配色（可调整）
bar_color = "#C6BF39"  # 基础绿色，也可换其他颜色如 "#FF8C00"

# 创建画布
fig, ax = plt.subplots(figsize=(6, 4))

# 绘制横向柱状图
y = np.arange(len(education))
bar_height = 0.6  # 定义 bar_height 变量
bars = ax.barh(y, percentages, color=bar_color, height=bar_height)

# 添加数据标注
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar_height/2),
                xytext=(5, 0),  # 标注位置：右侧偏移 5
                textcoords="offset points",
                ha='left', va='center',
                color='black')

# 设置y轴刻度和标签
ax.set_yticks(y)
ax.set_yticklabels(education)
# 设置x轴刻度（0-60%）
ax.set_xlim(0, 60)
# 设置标题
ax.set_title("2022年中国足球球迷学历情况", fontsize=14, fontweight="bold")

# 美化：隐藏顶部、右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()