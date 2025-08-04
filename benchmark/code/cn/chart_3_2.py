import matplotlib.pyplot as plt
import numpy as np

# 新图表对应的数据
labels = ["营销传播ROI难提升", "效果难测量和验证", "媒介碎片化"]
# 各类别占比数据（因是单组数据，直接用一维数组）
values = np.array([62, 54, 50])  
# 颜色方案（贴合原图色调，可微调）
colors = ['#4C72B0', '#818181', '#A9A9A9']  

# 创建画布和子图，设置图表尺寸
fig, ax = plt.subplots(figsize=(8, 4))  

# 绘制横向条形图（单组数据，无需堆积）
for i, (label, value, color) in enumerate(zip(labels, values, colors)):
    bar = ax.barh(label, value, color=color, alpha=0.9, edgecolor='w', linewidth=0.5)
    
    # 在条形末端标注百分比
    ax.text(
        value + 1,  # 文本在条形右侧，可微调距离
        bar[0].get_y() + bar[0].get_height()/2,
        f"{value}%", 
        ha='left', 
        va='center',
        fontweight='bold',
        fontsize=10
    )

# 设置标题
ax.set_title('2021年广告主媒介选择挑战', fontsize=14, fontweight='bold', pad=20)  

# 设置标签（x轴表示百分比，y轴无额外标签需求则注释）
ax.set_xlabel('百分比 (%)', fontsize=12, labelpad=10)  
# ax.set_ylabel('类别', fontsize=12, labelpad=10)  # 若需y轴标签可取消注释

# 设置x轴范围，让数据显示更合理
ax.set_xlim(0, 70)  

# 设置网格线（x轴方向，虚线、半透明）
ax.grid(axis='x', linestyle='--', alpha=0.7)  

# 隐藏边框（可增强简洁感）
for spine in ax.spines.values():
    spine.set_visible(False)

# 调整布局，优化显示
plt.tight_layout()  

# 显示图表
plt.show()