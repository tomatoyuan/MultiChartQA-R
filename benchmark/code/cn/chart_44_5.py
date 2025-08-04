import matplotlib.pyplot as plt
import numpy as np

# 图表数据
status = ["久坐不动，几乎一整天都坐着，很少起身", 
          "坐的太久身体不舒服的时候才会起来走一走", 
          "在工位上安置了电脑支撑架，经常站立办公", 
          "有规律地要求自己每隔一段时间就起身活动，如每一小时", 
          "经常因工作需要频繁走动，不存在久坐问题"]
percentage = [34, 44, 8, 13, 2]
tgi = [138, 108, 73, 59, 65]

# 创建画布和双Y坐标轴
fig, ax1 = plt.subplots(figsize=(14, 8))
ax2 = ax1.twinx()

# 设置柱状图位置
x = np.arange(len(status))
width = 0.35

# 绘制柱状图
bars1 = ax1.bar(x - width/2, percentage, width, label='占比', color='#5DA5DA')
bars2 = ax2.bar(x + width/2, tgi, width, label='TGI', color='#FAA43A')

# 设置坐标轴标签和标题
ax1.set_xlabel('日常办公状态', fontsize=12)
ax1.set_ylabel('占比 (%)', fontsize=12, color='#5DA5DA')
ax2.set_ylabel('TGI', fontsize=12, color='#FAA43A')
plt.title('朋克加班人群日常办公状态与TGI分布', fontsize=16)

# 设置x轴刻度和标签
ax1.set_xticks(x)
ax1.set_xticklabels(status, rotation=45, ha='right', fontsize=10)

# 添加图例
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines1 + lines2, labels1 + labels2, loc='upper right')

# 添加数据标签
def add_labels(bars, ax, is_percentage=True):
    for bar in bars:
        height = bar.get_height()
        if is_percentage:
            ax.annotate(f'{height}%',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom')
        else:
            ax.annotate(f'{height}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom')

add_labels(bars1, ax1)
add_labels(bars2, ax2, False)

# 设置网格线
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()