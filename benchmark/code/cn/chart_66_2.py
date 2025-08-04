import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

age_groups = ["95后", "90后", "85后", "85前"]
categories = ["需要日常定期补充", "在宠物有相关症状或处于特殊时期时补充即可"]
data = [[46, 52, 56, 54], [33, 35, 28, 30]]
colors = [["#C0C0C0", "#A4C639", "#8DB328", "#7EA11E"], 
          ["#A4C639", "#8DB328", "#C0C0C0", "#D3D3D3"]]

x = np.arange(len(age_groups))  
width = 0.35  

fig, ax = plt.subplots(figsize=(8, 5))
for i in range(len(categories)):
    rects = ax.bar(x + i * width, data[i], width, color=colors[i], edgecolor="white", label=categories[i])
    for rect, label in zip(rects, data[i]):
        height = rect.get_height()
        ax.annotate(f'{label}%',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  
                    textcoords="offset points",
                    ha='center', va='bottom')

ax.set_xticks(x + width / 2)
ax.set_xticklabels(age_groups)
ax.set_ylim(0, 60)
ax.set_title("各年龄段人群对宠物保健品的接受度", fontsize=14, fontweight="bold")

# 调整图例位置，比如放在左上角
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))  

plt.show()