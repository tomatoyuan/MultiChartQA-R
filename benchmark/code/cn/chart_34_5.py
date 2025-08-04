import matplotlib.pyplot as plt
import numpy as np

# 模拟数据，大体对应原图表的类别和趋势
categories = ["香氛", "山茶花", "0感", "无菌", "护肤", "玻尿酸", "天丝", "润肤", "悬浮", "芦荟"]
gmv_data = [71, 70, 20, 25, 20, 38, 26, 16, 32, 20]  # GMV（指数）模拟数据
growth_data = [0.10, 0.1, 0.08, 0.06, 0.05, 0.04, 0.03, 0.025, 0.02, 0.015]  # 同比模拟数据

x = np.arange(len(categories))  # x轴位置

# 创建画布和子图，设置图表大小
fig, ax1 = plt.subplots(figsize=(12, 7))

# 设置背景风格 - 使用Matplotlib内置样式替代
plt.style.use('ggplot')

# 绘制柱状图（GMV） - 使用渐变色
cmap = plt.cm.Blues
norm = plt.Normalize(min(gmv_data), max(gmv_data))
colors = cmap(norm(gmv_data))

bars = ax1.bar(x, gmv_data, width=0.6, color=colors, label='GMV（指数）', edgecolor='black', linewidth=0.5)
ax1.set_ylabel('GMV（指数）', fontsize=12, fontweight='bold')
ax1.set_xlabel('卖点', fontsize=12, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(categories, rotation=30, ha='right', fontsize=10)  # 旋转x轴标签

# 添加柱状图数据标签
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 1,
            f'{height}', ha='center', va='bottom', fontsize=9)

# 创建第二个y轴绘制折线图（同比）
ax2 = ax1.twinx()
line, = ax2.plot(x, growth_data, color='#FF7F50', marker='o', markersize=6, 
                linewidth=2, label='同比增长率')
ax2.set_ylabel('同比增长率', rotation=270, labelpad=18, fontsize=12, fontweight='bold')
ax2.set_ylim(0, 0.13)  # 大致对应原图表百分比范围

# 添加折线图数据标签
for i, txt in enumerate(growth_data):
    ax2.annotate(f'{txt:.1%}', (x[i], growth_data[i]), 
                textcoords="offset points", 
                xytext=(0,10), 
                ha='center',
                fontsize=9)

# 添加标题和图例
plt.title('2025年春上新至今抖音科技内衣卖点增速TOP10', fontsize=16, fontweight='bold', pad=20)

# 合并两个图例
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper right', frameon=True, shadow=True)

# 添加网格线
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax2.grid(axis='y', linestyle='--', alpha=0.3)

# 调整图表边距
plt.tight_layout()

# 显示图表
plt.show()