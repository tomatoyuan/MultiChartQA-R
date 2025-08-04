import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 数据
labels = ["总投资", "商业、转会、门票", "引进外援支出"]
values = [41, 30.9, 34.3]
colors = ["#2E7D32", "#2E7D32", "#B71C1C"]  # 绿色和红色
highlight_color = "#FFC107"  # 黄色高亮

# 创建画布
fig, ax = plt.subplots(figsize=(8, 5), facecolor='#f8f9fa')
ax.set_ylim(0, 1)
ax.set_xlim(0, len(values) * 2.5)  # 增加x轴空间
ax.axis('off')

# 绘制背景网格
for i in range(1, 10):
    ax.axhline(y=i*0.1, color='#e9ecef', linestyle='-', alpha=0.5)

# 绘制数据块
for i in range(len(values)):
    # 添加阴影效果
    shadow = patches.FancyBboxPatch(
        (i * 2.5 + 0.1, 0.15), 1.5, 0.6, 
        boxstyle=patches.BoxStyle("Round", pad=0.02),
        facecolor='black', alpha=0.2
    )
    ax.add_patch(shadow)
    
    # 绘制主方块
    rect = patches.FancyBboxPatch(
        (i * 2.5, 0.2), 1.5, 0.6, 
        boxstyle=patches.BoxStyle("Round", pad=0.02),
        facecolor=colors[i], edgecolor="none", alpha=0.9
    )
    ax.add_patch(rect)
    
    # 添加边框高亮
    highlight = patches.FancyBboxPatch(
        (i * 2.5, 0.2), 1.5, 0.6, 
        boxstyle=patches.BoxStyle("Round", pad=0.02),
        facecolor='none', edgecolor=highlight_color, 
        linewidth=2, alpha=0.8
    )
    ax.add_patch(highlight)
    
    # 绘制数值文字
    ax.text(
        i * 2.5 + 0.75, 0.5, f"{values[i]}", 
        ha="center", va="center", fontsize=28, 
        color="white", fontweight='bold',
        bbox=dict(facecolor='none', edgecolor='none')
    )
    
    # 绘制标签文字
    ax.text(
        i * 2.5 + 0.75, 0.15, labels[i], 
        ha="center", va="center", fontsize=14, 
        color="#333333", fontweight='bold'
    )

# 添加标题
ax.text(
    (len(values) * 2.5) / 2, 0.95, "中超俱乐部财务数据概览", 
    ha="center", va="center", fontsize=22, 
    color="#212529", fontweight='bold'
)

# 添加副标题
ax.text(
    (len(values) * 2.5) / 2, 0.88, "单位：亿元人民币", 
    ha="center", va="center", fontsize=14, 
    color="#6c757d"
)

# 添加图例
ax.text(
    1.25, 0.05, "■ 收入项", 
    ha="center", va="center", fontsize=12, 
    color="#2E7D32"
)
ax.text(
    3.75, 0.05, "■ 支出项", 
    ha="center", va="center", fontsize=12, 
    color="#B71C1C"
)

# 添加数据来源
ax.text(
    (len(values) * 2.5) - 1.5, 0.05, "数据来源：虚构示例", 
    ha="right", va="center", fontsize=10, 
    color="#6c757d"
)

# 微调布局
plt.tight_layout()

# 显示图表
plt.show()