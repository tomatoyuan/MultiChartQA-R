import matplotlib.pyplot as plt
import numpy as np

# 设置季度数据
quarters = ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023', 'Q1 2024', 'Q2 2024']
# App Store 下载量数据（单位：亿次），调整后Q1 2024 + Q2 2024 ≈ 1.76
app_store = [0.77, 0.8, 0.95, 0.85, 0.95, 0.81]  
# Google Play 下载量数据（单位：亿次），调整后Q1 2024 + Q2 2024 ≈ 1.44
google_play = [0.8, 0.75, 0.75, 0.8, 0.8, 0.64]  

x = np.arange(len(quarters))  # x轴刻度位置
width = 0.5  # 增加柱子宽度

# 创建更宽的图表（宽度12，高度6）
fig, ax = plt.subplots(figsize=(12, 6))

# 绘制 App Store 柱子（底部）
rects1 = ax.bar(x, app_store, width, label='App Store', color='#9b59b6')
# 绘制 Google Play 柱子（顶部）
rects2 = ax.bar(x, google_play, width, bottom=app_store, label='Google Play', color='#1abc9c')

# 设置x轴刻度标签和旋转角度
ax.set_xticks(x)
ax.set_xticklabels(quarters, rotation=0)  # 水平显示季度标签

# 设置y轴范围和刻度
ax.set_ylim(0, 2.0)
ax.set_yticks([0, 0.5, 1.0, 1.5, 2.0])
ax.set_yticklabels(['0亿', '0.5亿', '1.0亿', '1.5亿', '2.0亿'])

# 添加数据标签（修改为保留两位小数）
def add_labels(rects, bottom_values=None):
    for i, rect in enumerate(rects):
        height = rect.get_height()
        if bottom_values is not None:
            y_pos = bottom_values[i] + height / 2
        else:
            y_pos = height / 2
        # 格式化显示为两位小数
        ax.text(rect.get_x() + rect.get_width()/2., y_pos,
                f'{height:.2f}', ha='center', va='center', color='white', fontweight='bold')

add_labels(rects1)  # App Store 标签
add_labels(rects2, app_store)  # Google Play 标签

# 添加图例和标题
ax.legend(loc='upper right')
ax.set_title('2023 Q1 - 2024 Q2 日本市场手游下载量趋势', fontsize=16, pad=20)

# 添加网格线
ax.grid(axis='y', linestyle='--', alpha=0.7)

# 在标题下方添加指定文字（调整y坐标为0.92）
text = "2024年上半年，日本市场手游下载量同比提升2.5%，达到3.2亿次，其中App Store平台下载量占比为55%。"
fig.text(0.5, 0.92, text, ha='center', va='center', fontsize=12)

# 调整布局
plt.tight_layout()

plt.show()