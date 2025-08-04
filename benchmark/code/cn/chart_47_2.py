import matplotlib.pyplot as plt

# 数据
labels = ['生物科技原料', '美妆护肤品牌', '医疗科技', '其他']
sizes = [42, 25, 20, 13]  # 这里的数值为模拟，你可根据实际数据替换，保证总和为100
colors = ['#d9b3b3', '#f2d9a6', '#c7e0c3', '#d9d9d9']  # 自定义颜色

# 绘制饼图
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
ax.set_title('2024国内美妆投融资企业分布')

plt.show()