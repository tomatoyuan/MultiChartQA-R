import matplotlib.pyplot as plt


# 数据
labels = ['原料进货成本', '人力成本', '三项费用', '房租及物业成本', '能源成本', '税费']
sizes = [42.7, 21.9, 20.1, 8.8, 3.6, 2.9]
colors = ['#E73331', '#233B7B', '#999999', '#F5B92E', '#4BA2C8', '#892D2D']
# explode = [0.05 if i == 0 else 0 for i in range(len(labels))]  # 突出显示“原料进货成本”

# 绘制图表
fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(aspect="equal"))
wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, colors=colors, autopct='%.1f%%',
    startangle=90, wedgeprops=dict(width=1.0), textprops=dict(color="black", fontsize=12)
)

# 设置标签字体为白色并居中
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(12)
    autotext.set_fontweight('bold')

ax.set_title("2023年我国餐饮样本企业各项成本占比情况", fontsize=16)
plt.tight_layout()
plt.show()