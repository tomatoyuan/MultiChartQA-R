import matplotlib.pyplot as plt
import numpy as np

# 数据准备
labels = ["赛程表", "欧洲杯事件花絮", "直播网址", "上一场比分", "夺冠赔率", "其它"]
percents = [30, 24, 17, 14, 8, 7]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(10, 6), facecolor='#8BC34A')  # 绿色背景

# 绘制横向柱状图（使用黄色渐变）
y_pos = np.arange(len(labels))
colors = plt.cm.YlOrBr(np.linspace(0.6, 1, len(labels)))  # 黄色到橙色渐变
bars = ax.barh(y_pos, percents, color=colors, edgecolor='black', height=0.6)

# 添加标题和副标题
ax.set_title('八强之战前夕\n搜索关键词分布表', fontsize=18, fontweight='bold', pad=20)

# 设置y轴标签（关键词）
ax.set_yticks(y_pos)
ax.set_yticklabels(labels, fontsize=12)
ax.tick_params(axis='y', which='both', length=0)  # 隐藏y轴刻度线

# 设置x轴标签（百分比）
ax.set_xlabel('搜索占比（%）', fontsize=12, labelpad=15)
ax.set_xlim(0, 35)  # 留出右侧空间
ax.set_xticks(np.arange(0, 36, 5))
ax.set_xticklabels([f'{x}%' for x in np.arange(0, 36, 5)], fontsize=10)

# 为每个柱子添加数值标签
for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.8, bar.get_y() + bar.get_height()/2,
            f'{width}%', ha='left', va='center', fontsize=10, fontweight='bold')

# 添加"人物图标"（使用matplotlib原生形状替代）
for i, (label, percent) in enumerate(zip(labels, percents)):
    # 绘制简化的"人物"（圆形头部+矩形身体）
    head = plt.Circle((-2.5, y_pos[i]), 0.3, color='yellow', ec='black')
    body = plt.Rectangle((-2.8, y_pos[i]-0.3), 0.6, 0.6, color='yellow', ec='black')
    ax.add_patch(head)
    ax.add_patch(body)
    
    # 添加"爱心"标记（使用三角形替代）
    heart_x = [-2.6, -2.4, -2.5]
    heart_y = [y_pos[i]+0.15, y_pos[i]+0.15, y_pos[i]+0.3]
    ax.fill(heart_x, heart_y, color='red')

# 添加"放大镜"标记（使用matplotlib原生形状）
for i, p in enumerate(percents):
    num_magnifiers = p // 5
    for j in range(num_magnifiers):
        # 绘制简化的放大镜
        magnifier_x = [-5 - j*0.8, -4.5 - j*0.8, -4.7 - j*0.8, -5 - j*0.8]
        magnifier_y = [y_pos[i]+0.1, y_pos[i]+0.1, y_pos[i]-0.1, y_pos[i]-0.1]
        ax.fill(magnifier_x, magnifier_y, color='black')
        # 放大镜手柄
        ax.plot([-4.5 - j*0.8, -4.3 - j*0.8], [y_pos[i], y_pos[i]-0.2], 'k-', linewidth=1.5)

# 隐藏顶部和右侧边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(1)
ax.spines['left'].set_linewidth(1)

# 调整布局
plt.tight_layout(pad=3)
plt.show()