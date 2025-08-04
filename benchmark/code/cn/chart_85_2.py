import matplotlib.pyplot as plt

# 数据
labels = ['工业领域', '交通运输', '建筑及其他领域']
sizes = [60, 31, 9]
colors = ['#A4C639', '#a8dda8', '#87CEEB']  # 匹配原图色调

# 创建画布
fig, ax = plt.subplots(figsize=(6, 6))

# 绘制饼图
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',  
    startangle=90,     
    colors=colors,
    textprops={'color': 'black'}
)

# 调整标注位置（让“工业领域”的标注在饼图外，匹配原图布局）
for text, autotext, wedge in zip(texts, autotexts, wedges):
    if text.get_text() == '工业领域':
        text.set_position((1.15, 0.5))  
        autotext.set_position((1.3, 0.5))

# 添加上方的结构说明框
structure_text = "工业领域：60%\n交通运输：31%\n建筑及其他：9%"
bbox_props = dict(boxstyle="round,pad=0.5", fc="white", ec="green", lw=1)
ax.text(0.25, 0.9, structure_text, transform=ax.transAxes, fontsize=12,
        bbox=bbox_props, color='green')

# 设置标题
ax.set_title('氢气利用结构', fontsize=14, fontweight='bold', y=1.1)

plt.tight_layout()
plt.show()