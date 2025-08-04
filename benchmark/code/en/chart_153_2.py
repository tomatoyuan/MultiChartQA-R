import matplotlib.pyplot as plt

labels = ["Skin Care", "Methods", "Lifestyle", "Medical Aesthetics", "Oral Administration"]
sizes_2023 = [69.36, 17.76, 7.52, 4.70, 0.66]
sizes_2024 = [71.33, 12.58, 6.45, 9.07, 0.57]
colors = ['#224b4a', '#628a89', '#a9c0bf', '#cededc', '#e7f0ef']

fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# 饼图 1
wedges1, texts1, autotexts1 = axs[0].pie(
    sizes_2023, labels=labels, autopct='%1.2f%%', startangle=140, colors=colors,
    textprops={'fontsize': 9}
)
axs[0].set_title("Aug 2022 – Jul 2023")

# 饼图 2
wedges2, texts2, autotexts2 = axs[1].pie(
    sizes_2024, labels=labels, autopct='%1.2f%%', startangle=140, colors=colors,
    textprops={'fontsize': 9}
)
axs[1].set_title("Aug 2023 – Jul 2024")

# 调整数字颜色（深色扇区用白色，浅色用黑色）
def adjust_autotext_color(autotexts, wedges):
    for autotext, wedge in zip(autotexts, wedges):
        # 获取 wedge 的颜色
        face_color = wedge.get_facecolor()
        # 判断亮度（简单方式：RGB平均值）
        avg_brightness = sum(face_color[:3]) / 3
        if avg_brightness < 0.5:  # 深色底用白字
            autotext.set_color('white')
        else:  # 浅色底用黑字
            autotext.set_color('black')

adjust_autotext_color(autotexts1, wedges1)
adjust_autotext_color(autotexts2, wedges2)

# 总标题
fig.suptitle("Fig 1.1-3 Proportion of Pore - Enlargement Improvement Plans (Data Source: Feigua)", fontsize=13)
plt.tight_layout()
plt.show()