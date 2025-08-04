import matplotlib.pyplot as plt
import numpy as np

# 季度数据
quarters = ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023', 'Q1 2024', 'Q2 2024']
# App Store 内购收入（单位：亿美元，模拟数据贴近图表比例）
app_store = [20, 18, 18, 17, 16.3, 14.4]  
# Google Play 内购收入（单位：亿美元，模拟数据贴近图表比例）
google_play = [15, 12, 12, 11, 10.6, 11.7]

x = np.arange(len(quarters))  # x 轴刻度位置
width = 0.5  # 柱子宽度，让图表更紧凑美观

# 创建画布，设置尺寸
fig, ax = plt.subplots(figsize=(12, 6))

# 绘制 App Store 柱子（底部，紫色）
rects1 = ax.bar(x, app_store, width, label='App Store', color='#9b59b6')
# 绘制 Google Play 柱子（顶部，青色，底部基于 App Store 数据堆叠）
rects2 = ax.bar(x, google_play, width, bottom=app_store, label='Google Play', color='#1abc9c')

# 设置 x 轴刻度与标签，水平显示
ax.set_xticks(x)
ax.set_xticklabels(quarters, rotation=0)  

# 设置 y 轴范围与刻度，匹配图表的“0、18、36 亿美元”量级
ax.set_ylim(0, 36)
ax.set_yticks([0, 18, 36])
ax.set_yticklabels(['0亿美元', '18亿美元', '36亿美元'])

# 添加数据标签函数，显示柱子高度（保留1位小数）
def add_labels(rects, bottom_values=None):
    for i, rect in enumerate(rects):
        height = rect.get_height()
        y_pos = bottom_values[i] + height / 2 if bottom_values is not None else height / 2
        ax.text(
            rect.get_x() + rect.get_width()/2., 
            y_pos,
            f'{height:.1f}',  # 关键修改：强制保留1位小数
            ha='center', 
            va='center', 
            color='white', 
            fontweight='bold'
        )

add_labels(rects1)  # App Store 数据标签
add_labels(rects2, app_store)  # Google Play 数据标签

# 图例、标题设置
ax.legend(loc='upper right')
ax.set_title('2023 Q1 - 2024 Q2 日本市场手游内购收入趋势', fontsize=16, pad=40)

# 添加网格线，辅助观察数据
ax.grid(axis='y', linestyle='--', alpha=0.7)

# 图表上方说明文字，还原业务背景
text = ("2024年第二季度日元兑美元平均汇率相比2023年第一季度下降了18%，受汇率影响，\n"
        "2024年上半年，尽管手游下载量有所回升，内购收入同比下降17%至53亿美元。")
# 调整文字位置，避免与标题重叠
fig.text(0.5, 0.89, text, ha='center', va='center', fontsize=12, linespacing=1.5)

# 自动优化布局，确保元素不挤压
plt.tight_layout()

plt.show()