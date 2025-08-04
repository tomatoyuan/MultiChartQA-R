import matplotlib.pyplot as plt

# 数据定义
labels = ["追求学术创新", "积极参与科研项目，积累学术经验", "能够独立产出个人的研究成果", "不会主动投入，学校有要求才会去做"]
sizes = [33.8, 31.0, 27.3, 7.8]  # 数据大体模拟，可根据实际调整
# 颜色设置，尽量贴近原图
colors = ["greenyellow", "green", "limegreen", "lightgray"]

# 创建饼图
fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors,
                                  textprops={'fontsize': 12}, wedgeprops={'linewidth': 1, 'edgecolor': 'white'})

# 美化标注文本颜色
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')

# 设置标题
ax.set_title("大学生在学术方面的自我要求", fontsize=16, fontweight='bold', y=1.05)

# 调整图例位置（可选，若需要可调整）
ax.legend(loc='upper right', bbox_to_anchor=(1.5, 0.8), fontsize=12)

# 调整布局
plt.tight_layout()

plt.show()