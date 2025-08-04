import matplotlib.pyplot as plt

# 数据
labels = ['无需每日更换', '需每日更换']
sizes = [62.6, 37.4]
colors = ['#058b83', '#abd7a6']  # 使用与图表一致的配色

# 生成饼状图
plt.figure(figsize=(6, 6))
wedges, texts, autotexts = plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    textprops={'fontsize': 14}
)

# 设置标题
plt.title('多人入住「无需每日更换一次性用品」人数占比', fontsize=16)

# 显示图表
plt.tight_layout()
plt.show()