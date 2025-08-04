import matplotlib.pyplot as plt
import numpy as np

# 数据
labels = ['一次成功率', '二次成功率', '三次以上成功率']
values = [8, 27, 65]

# 创建图形
fig, ax = plt.subplots()

# 绘制柱状图
ax.bar(labels, values, color=['lightblue', 'lightgreen', 'lightcoral'])

# 添加数值标签
for i, v in enumerate(values):
    ax.text(i, v + 1, f'{v}%', ha='center')

# 设置标题和坐标轴标签（可根据需求调整）
ax.set_ylabel('百分比')
# 添加标题
ax.set_title('2016年春运期间12306验证码录入成功率分布')

# 显示图形
plt.show()