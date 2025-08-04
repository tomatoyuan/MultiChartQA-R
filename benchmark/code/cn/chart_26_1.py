import matplotlib.pyplot as plt

# 数据
labels = ['女性', '男性']
sizes = [35, 65]
colors = ['#FF69B4', '#4169E1']  # 对应粉色、蓝色
explode = (0.05, 0)  # 突出显示女性部分

# 创建画布和子图
fig, ax = plt.subplots(figsize=(8, 6), facecolor='#666666')

# 绘制环形图
wedges, texts, autotexts = ax.pie(
    sizes,
    explode=explode,
    colors=colors,
    autopct=lambda p: f'{p:.1f}%\n({int(p*sum(sizes)/100)})',  # 显示百分比和实际数量
    startangle=90,
    wedgeprops=dict(width=0.4, edgecolor='w', linewidth=2),
    textprops=dict(fontsize=12)
)

# 设置标题和副标题
ax.set_title('情人节礼物搜索性别比例分析', fontsize=18, fontweight='bold', pad=20)

# 美化文本样式 - 修复版本（使用饼图返回的texts和autotexts）
for text in texts:
    text.set_color('#666666')  # 深灰色文本
    text.set_fontsize(14)
    text.set_fontweight('bold')
    
for autotext in autotexts:
    autotext.set_color('white')  # 百分比文本保持白色（与深色背景对比）
    autotext.set_fontsize(12)
    autotext.set_fontweight('bold')

# 添加图例和注释
ax.legend(wedges, labels, title="性别", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.annotate(
    '男性搜索占比更高',
    xy=(0.5, 0.5),
    xytext=(0.7, 0.7),
    arrowprops=dict(arrowstyle='->', color='#333333'),
    fontsize=12,
    ha='center'
)

# 设置背景和布局
plt.tight_layout()
plt.subplots_adjust(right=0.8)  # 为图例留出空间
plt.axis('equal')  # 确保饼图是圆形

# 保存图表（可选）
# plt.savefig('valentines_gift_gender_pie.png', dpi=300, bbox_inches='tight')

# 显示图表
plt.show()