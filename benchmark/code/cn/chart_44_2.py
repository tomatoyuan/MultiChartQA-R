import matplotlib.pyplot as plt
# 数据
labels = ["在寻找健康食材上消耗很多精力和时间，没有明确的标签指示",
          "担心食品添加剂过多",
          "无法判断速成食品或外卖是否健康",
          "难以找到可以长期信赖的购买渠道",
          "纠结每一种食物的热量高低，怕长胖"]
percentages = [60, 55, 47, 44, 18]

# 创建绘图对象
fig, ax = plt.subplots()

# 绘制横向条形图
ax.barh(labels, percentages, color='green')

# 添加百分比标签
for i, v in enumerate(percentages):
    ax.text(v + 1, i, f'{v}%', va='center')

# 设置标题和坐标轴标签（可根据需求调整）
ax.set_title('健康食材相关担忧情况')

# 显示图表
plt.show()