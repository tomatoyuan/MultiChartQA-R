import matplotlib.pyplot as plt

# 数据
labels = ['心脑血管疾病', '癌症', '慢性呼吸系统疾病', '其他']
sizes = [53, 27, 10, 10]  # 其他部分占比，使总和为100，数据大体接近即可
colors = ['#008060', '#80e0a0', '#c0ffe0', '#d9d9d9']  # 颜色尽量接近原图表

# 绘制饼图
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
ax.set_title('慢性病死因构成')

# 调整图例位置（模拟原图表的标注样式，可根据实际需求微调）
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right', bbox_to_anchor=(1.3, 1.1))

plt.show()