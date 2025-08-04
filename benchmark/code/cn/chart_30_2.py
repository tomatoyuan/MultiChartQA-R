import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 数据
labels = ['19-24岁', '25-34岁', '18岁及以下', '35-49岁', '50岁']
sizes = [41, 33, 15, 10, 1]
# 自定义颜色，使用更专业的配色方案
colors = ['#3498db', '#2ecc71', '#f39c12', '#e74c3c', '#9b59b6']
# 突出显示最大的扇形
explode = (0.1, 0, 0, 0, 0)  

# 创建画布和子图
fig, ax = plt.subplots(figsize=(10, 7))

# 绘制饼图，添加阴影和自定义百分比样式
wedges, texts, autotexts = ax.pie(
    sizes, 
    explode=explode,
    labels=labels,
    colors=colors,
    autopct=lambda p: f'{p:.1f}%\n({int(p*sum(sizes)/100)})',  # 同时显示百分比和实际人数
    shadow=True,
    startangle=90,
    textprops={'fontsize': 12}
)

# 设置标题
ax.set_title('艾滋病相关人群画像趋向年轻人', fontsize=16, pad=20)

# 使饼图为正圆形
ax.axis('equal')  

# 添加图例
plt.legend(wedges, labels, title="年龄分组", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# 添加注释
plt.figtext(0.5, 0.01, f"数据总计: {sum(sizes)}人", ha="center", fontsize=12)

# 调整布局
plt.tight_layout()

# 显示图形
plt.show()