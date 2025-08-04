import matplotlib.pyplot as plt
import numpy as np

# -------------------- 数据定义 --------------------
categories = ["中度用户", "重度用户", "轻度用户"]
sizes = [53.1, 43.7, 3.2]  # 占比（百分比）

# 颜色配置（贴近原图）
colors = ["#a5d6a7", "#81c784", "#4dd0e1"]

# 图例说明（需与原图一致）
legend_labels = [
    "中度用户-使用程度适中，比较喜欢用，但没有很依赖",
    "重度用户-大部分休闲时间都会使用",
    "轻度用户-只有小部分休闲时间偶尔使用"
]

# -------------------- 创建画布 --------------------
fig, ax = plt.subplots(figsize=(8, 6))

# -------------------- 绘制饼图 --------------------
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=None,  # 先不设置标签，通过图例显示
    colors=colors,
    autopct='%1.1f%%',  # 显示百分比
    startangle=90,      # 从90度开始绘制（让中度用户在右侧）
    wedgeprops={
        'edgecolor': 'white', 
        'linewidth': 1,
        # 重度用户的虚线圆弧：通过设置 wedgeprops 的 'linestyle' 实现
        'linestyle': 'dashed' if categories[1] == "重度用户" else 'solid'
    },  
    textprops={'fontsize': 10, 'color': '#424242', 'fontweight': 'bold'}  # 百分比文本设置
)

# -------------------- 绘制重度用户的虚线圆弧（补充饼图未覆盖的样式） --------------------
# 获取重度用户的 wedge
heavy_user_wedge = wedges[1]
# 绘制虚线圆弧（从起始角度到结束角度）
theta1, theta2 = heavy_user_wedge.theta1, heavy_user_wedge.theta2
center, r = heavy_user_wedge.center, heavy_user_wedge.r

# -------------------- 美化图表 --------------------
# 设置图例（调整位置和样式，与原图一致）
ax.legend(
    wedges, legend_labels,
    title="用户类型",
    loc="center left",
    bbox_to_anchor=(1, 0.5),  # 图例在右侧居中
    fontsize=9,
    title_fontsize=12,
    frameon=True,
    facecolor="white",
    edgecolor="white"
)

# 使饼图为正圆形
ax.axis('equal')  

# 添加标题
ax.set_title(
    "2022年中国美颜拍摄类APP用户社交娱乐内容平台使用情况",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# 调整布局（让图例和标题不重叠）
plt.subplots_adjust(right=0.7)

plt.show()