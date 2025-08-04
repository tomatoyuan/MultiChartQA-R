import matplotlib.pyplot as plt

# 数据
labels = [
    "电子商务", "教育", "交通运输", "传媒", "金融", "影视", 
    "房产服务", "游戏", "卫生、社会保障和社会福利业", "文旅", "其他"
]
sizes = [16.49, 11.97, 8.24, 8.24, 10.51, 7.31, 7.85, 6.78, 12.91, 8.64, 1.06]
# 对应颜色（尽量匹配原图，可根据实际微调）
colors = [
    '#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63',
    '#1E90FF', '#FFD700', '#00FA9A', '#FF69B4', '#00BFFF', '#BA55D3'
]

fig, ax = plt.subplots(figsize=(12, 8))
# 绘制环形图，wedgeprops 设置环形宽度
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# 调整标注文字大小和颜色等（可选），让标注更清晰
for text in texts:
    text.set_fontsize(10)
for autotext in autotexts:
    autotext.set_fontsize(9)
    autotext.set_color('black')  # 让数值在彩色块上更清晰

ax.set_title('2025年中国使用AI数字人企业的行业分布')

plt.tight_layout()
plt.show()