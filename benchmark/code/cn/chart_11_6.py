import matplotlib.pyplot as plt
import numpy as np

# 数据（已按降序排列）
universities = [
    "哈佛大学", "麻省理工学院", "斯坦福大学", 
    "约翰斯霍普金斯大学", "加州大学伯克利分校", 
    "华盛顿大学西雅图分校", "多伦多大学", 
    "牛津大学", "加州大学洛杉矶分校", "伦敦大学学院"
]

# 搜索指数（降序排列）
search_proportion = [1.0, 0.9, 0.85, 0.7, 0.65, 0.6, 0.5, 0.45, 0.4, 0.3]

# 配色方案（增强对比度）
colors = [
    "#FF5252", "#FF9800", "#FFEB3B", 
    "#42A5F5", "#42A5F5", "#42A5F5", 
    "#5C6BC0", "#5C6BC0", "#5C6BC0", "#5C6BC0"
]

# 创建画布（增加清晰度）
plt.rcParams['figure.dpi'] = 300
fig, ax = plt.subplots(figsize=(10, 7), facecolor="#E8F5E9")

# 逆序排列数据
universities = universities[::-1]
search_proportion = search_proportion[::-1]
colors = colors[::-1]  # 如果需要保持颜色对应关系也需反转

# 绘制横向条形图（添加阴影效果）
bars = ax.barh(universities, search_proportion, color=colors, height=0.7, 
               edgecolor='black', linewidth=0.5, alpha=0.9)

# 添加标题（改进设计）
title_bg = plt.Rectangle((0, 1.02), 1, 0.1, color="#D32F2F", transform=ax.transAxes, 
                        clip_on=False, zorder=3)
ax.add_patch(title_bg)
ax.text(0.5, 1.06, "最被关注的Top名校（海外）", 
        fontsize=18, fontweight="bold", color="white", 
        transform=ax.transAxes, va="center", ha="center")

# 添加“搜索指数”标注（改进位置）
ax.text(-0.15, 0.98, "搜索指数", 
        fontsize=14, fontweight="bold", color="#D32F2F", 
        transform=ax.transAxes, va="center", rotation=0)

# 美化y轴标签（添加填充和边框）
for i, txt in enumerate(ax.get_yticklabels()):
    txt.set_bbox(dict(facecolor='white', alpha=0.7, edgecolor='gray', boxstyle='round,pad=0.3'))

# 隐藏边框与刻度
ax.spines[:].set_visible(False)
ax.set_xticks([])
ax.tick_params(axis='y', labelsize=12, pad=15)

# 添加网格线（水平方向）
ax.set_axisbelow(True)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# 添加底部装饰线
footer_line = plt.Line2D([0, 1], [-0.03, -0.03], color='#D32F2F', 
                        transform=ax.transAxes, linewidth=3, clip_on=False)
ax.add_artist(footer_line)

plt.tight_layout()
plt.show()