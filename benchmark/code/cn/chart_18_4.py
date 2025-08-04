import matplotlib.pyplot as plt
import numpy as np

# 数据
countries = ["韩国", "日本", "美国", "埃及"]
costs = [31, 41, (11 + 17) / 2, 44]  # 美国取区间平均值

# 颜色方案
colors = ['#638EC6', '#7BC67B', '#FFBC52', '#FF6F6F']

# 创建画布和子图
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制横向柱状图，添加透明度和边框
bars = ax.barh(countries, costs, color=colors, alpha=0.8, edgecolor='black', linewidth=0.8)

# 添加标题和标签
ax.set_title("国外结婚成本对比", fontsize=16, pad=15)
ax.set_xlabel("结婚成本（万人民币）", fontsize=12, labelpad=10)
ax.set_ylabel("国家", fontsize=12, labelpad=10)

# 添加数值标签
for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.5, bar.get_y() + bar.get_height()/2,
            f'{width:.1f}', ha='left', va='center', fontsize=10)

# 设置坐标轴样式
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(0.5)
ax.spines['left'].set_linewidth(0.5)

# 设置刻度样式
ax.tick_params(axis='both', which='major', labelsize=10)
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# 添加背景网格
plt.grid(axis='x', linestyle='--', alpha=0.3)

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()