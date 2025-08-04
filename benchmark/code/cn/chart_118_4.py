import matplotlib.pyplot as plt

# 数据
labels = [
    "效率提升50%以上", "效率提升40-50%", "效率提升30-40%", 
    "效率提升20-30%", "效率提升10-20%", "效率提升10%以下"
]
sizes = [12.53, 27.52, 31.61, 18.53, 6.54, 3.27]
# 对应颜色（尽量匹配原图，可根据实际微调）
colors = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63', '#1E90FF']

fig, ax = plt.subplots(figsize=(10, 7))
# 绘制环形图，wedgeprops 设置环形宽度
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# 调整标注文字大小和颜色等（可选），让标注更清晰
for text in texts:
    text.set_fontsize(10)
for autotext in autotexts:
    autotext.set_fontsize(9)
    autotext.set_color('black')  # 让数值在彩色块上更清晰

ax.set_title('2025年AI数字人对中国企业工作效率或质量提升情况')

plt.tight_layout()
plt.show()