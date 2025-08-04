import matplotlib.pyplot as plt
import numpy as np

# 数据（专业名称 + 搜索指数）
majors = [
    "生物工程", "国际经济与贸易", "通信工程", 
    "金融学", "工商管理", "经济学", 
    "计算机应用", "电气自动化"
]
search_index = [323, 712, 1060, 1374, 1241, 945, 581, 447]

# 反转数据顺序（让“生物工程”在最上方，与原图一致）
majors = majors[::-1]
search_index = search_index[::-1]

# 创建画布
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制横向条形图
colors = ["#99D8C9", "#4ECDC4", "#239B56", "#E74C3C", "#F39C12", "#F1C40F", "#3498DB", "#9B59B6"]
ax.barh(majors, search_index, color=colors, height=0.7)

# 添加搜索指数标签
for i, idx in enumerate(search_index):
    ax.text(idx + 20, i, str(idx), va="center", fontsize=10, fontweight="bold")

# 设置标题
ax.set_title("曾经的热门专业今何在", fontsize=14, fontweight="bold", pad=20, loc="left")

# 隐藏顶部、右侧边框和 x 轴刻度
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xticks([])

# 调整 y 轴刻度字体大小
ax.tick_params(axis='y', labelsize=11)

# 设置 x 轴范围，留出标签空间
ax.set_xlim(0, max(search_index) + 200)

plt.tight_layout()
plt.show()