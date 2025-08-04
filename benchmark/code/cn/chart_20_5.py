import matplotlib.pyplot as plt

# 数据
labels = ['购买保险', '寻医挂号', '寻找偏方', '求神拜佛', '其他']  # 这里补充“其他”，因原图表各部分占比和为43%+18%+18%+21% = 100% ，实际按你的需求调整
sizes = [43, 18, 18, 21, 0]  # 各部分占比，和为100，可按需调整
colors = ['#FFA07A', '#90EE90', '#FFC0CB', '#87CEFA', '#D3D3D3']  # 各部分颜色，可自定义

# 绘制饼图
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # 保证饼图是正圆形

# 添加标题
plt.title('癌症患者后续行为')

# 显示图表
plt.show()