import matplotlib.pyplot as plt

# 企业类型及占比数据
labels = [
    "制造业", "信息传输、计算机服务和软件业", "采矿业", "文化、体育和娱乐业",
    "农林牧渔业", "批发和零售业", "教育", "建筑业", "房地产业",
    "电力、燃气与水的生产和供应业", "交通运输、仓储和邮政业", "金融业",
    "卫生、社会保障和社会福利业", "其他"
]
sizes = [14.74, 14.32, 2.14, 8.55, 4.27, 8.55, 3.85, 5.34, 7.26, 9.40, 8.97, 4.49, 7.91, 0.21]
# 对应颜色（尽量匹配原图，可根据实际微调）
colors = [
    '#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63',
    '#1E90FF', '#FFD700', '#00FA9A', '#FF69B4', '#00BFFF',
    '#FFA07A', '#9370DB', '#7FFF00', '#BA55D3'
]

fig, ax = plt.subplots(figsize=(12, 8))
# 绘制环形图，wedgeprops 设置环形宽度
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# 调整标注文字大小和颜色等（可选），让标注位置更合理
for text in texts:
    text.set_fontsize(10)
for autotext in autotexts:
    autotext.set_fontsize(9)
    autotext.set_color('black')  # 让数值在彩色块上更清晰

ax.set_title('2025年中国数字化转型企业的类型')

plt.tight_layout()
plt.show()