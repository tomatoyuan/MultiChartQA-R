import matplotlib.pyplot as plt

# 设置问题与百分比（按原图顺序，从高到低）
labels = [
    '水分流失、皮肤干燥',
    '皮肤暗沉',
    '皮肤粗糙暗黄',
    '毛孔粗大',
    '皱纹、细纹',
    '皮肤松弛、下垂',
    '黑色素沉淀、色斑',
    '肌肤屏障脆弱',
    '代谢能力差',
    '其他衰老问题',
    '以上都没有'
]
percentages = [65, 61, 59, 57, 53, 53, 51, 47, 30, 18, 2]

# 颜色定义（前3个高亮金黄，其余统一紫色）
colors = ['#FFCC00', '#FBC02D', '#F9A825'] + ['#673AB7'] * (len(labels) - 3)

# 反转顺序：从上到下显示最高到最低
labels = labels[::-1]
percentages = percentages[::-1]
colors = colors[::-1]
y_pos = range(len(labels))

# 创建图形
fig, ax = plt.subplots(figsize=(10, 7))
bars = ax.barh(y_pos, percentages, color=colors)

# 添加百分比标签
for bar, pct in zip(bars, percentages):
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2,
            f'{pct}%', va='center', fontsize=11)

# 图表样式设置
ax.set_yticks(y_pos)
ax.set_yticklabels(labels, fontsize=11)
ax.invert_yaxis()  # 最大值在上
ax.set_xlim(0, 70)
ax.set_title("水分流失、暗沉、粗糙暗黄是人们遇到最多的肌肤衰老问题", fontsize=14, weight='bold')

# 去除边框和多余坐标
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_color('#cccccc')
ax.xaxis.set_visible(False)

# 数据来源标注
source_text = (
    "数据来源：2024年7月CBNData问卷调研\n"
    "Q4. 请问您在日常生活中是否面临以下肌肤问题？"
)
plt.figtext(0.5, -0.05, source_text, wrap=True, ha='center', fontsize=9, color='gray')

plt.tight_layout()
plt.show()