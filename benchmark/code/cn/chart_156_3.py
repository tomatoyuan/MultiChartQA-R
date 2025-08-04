import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 数据
labels = ['肉色/肤色款', '黑色款', '两种颜色都会买']
sizes = [61, 32, 7]
colors = ['#ffd6d6', '#ff8080', '#ffeaea']  # 贴近原图的渐变粉调配色
explode = (0, 0.05, 0.1)  # 突出显示后两项

# 创建图形
fig, ax = plt.subplots(figsize=(6, 6))
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=sizes,
    explode=explode,
    colors=colors,
    startangle=90,
    counterclock=False,
    autopct='%1.0f%%',
    textprops={'fontsize': 12, 'color': 'white'},
    wedgeprops=dict(width=0.9, edgecolor='white')
)

# 设置标题
ax.set_title("消费者光腿袜选购颜色偏好调研", fontsize=14, weight='bold')

# 添加图例
ax.legend(wedges, labels, loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=3, frameon=False, fontsize=10)

# 添加数据来源
source_text = "数据来源：CBNData2024年7月调研数据"
plt.figtext(0.5, -0.12, source_text, wrap=True, horizontalalignment='center', fontsize=9, color='gray')

plt.tight_layout()
plt.show()