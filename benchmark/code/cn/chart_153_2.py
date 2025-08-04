# 图表 1.1-3：毛孔粗大改善方案占比（两个饼图对比）

labels = ["护肤", "方法", "生活", "医美", "口服"]
sizes_2023 = [69.36, 17.76, 7.52, 4.70, 0.66]
sizes_2024 = [71.33, 12.58, 6.45, 9.07, 0.57]
colors = ['#224b4a', '#628a89', '#a9c0bf', '#cededc', '#e7f0ef']

fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# 饼图1 - 2022/08-2023/07
wedges1, texts1, autotexts1 = axs[0].pie(
    sizes_2023, labels=labels, autopct='%1.2f%%', startangle=140, colors=colors,
    textprops={'fontsize': 9}
)
axs[0].set_title("2022/08–2023/07")

# 饼图2 - 2023/08-2024/07
wedges2, texts2, autotexts2 = axs[1].pie(
    sizes_2024, labels=labels, autopct='%1.2f%%', startangle=140, colors=colors,
    textprops={'fontsize': 9}
)
axs[1].set_title("2023/08–2024/07")

fig.suptitle("图 1.1-3 毛孔粗大改善方案占比（数据来源：飞瓜）", fontsize=13)
plt.tight_layout()
plt.show()