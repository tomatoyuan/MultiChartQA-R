import matplotlib.pyplot as plt

# 性别比例数据
labels = ["女", "男", "其他（爬虫等）"]
sizes = [57, 40, 3]  # 调整了"其他"比例以保证总和为100%
colors = ["#FFC0CB", "#87CEEB", "#D3D3D3"]  # 粉色(女)、浅蓝色(男)、浅灰色(其他)

# 创建画布
plt.figure(figsize=(8, 8))

# 绘制饼图
plt.pie(sizes, 
        labels=labels, 
        autopct='%1.1f%%',  # 显示百分比
        startangle=140,  # 起始角度
        colors=colors,
        explode=(0, 0, 0.1),  # 突出显示"其他"类别
        shadow=True,  # 添加阴影
        textprops={'fontsize': 12}  # 设置文本大小
       )

# 设置标题和等比例显示
plt.title("校园贷搜索用户性别比例", fontsize=16)
plt.axis('equal')  # 保证饼图是正圆形

# 显示图形
plt.tight_layout()
plt.show()