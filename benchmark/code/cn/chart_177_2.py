import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors

# 数据
categories = [
    "学习能力与学习习惯", "智力开发、科学类培训", "学科辅导、课内知识",
    "兴趣培养", "生活技能与行为习惯", "心理健康",
    "竞赛与竞技能力", "体育体能"
]
values = [68, 57, 54, 50, 40, 35, 26, 20]

# 颜色渐变设定
norm = mcolors.Normalize(vmin=min(values), vmax=max(values))
cmap = cm.Reds

# 画图
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(categories, values, color=cmap(norm(values)))

# 数值标注
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval + 1, f'{yval}%', ha='center', va='bottom', fontsize=10)

# 图形美化
ax.set_ylabel('关注比例 (%)')
ax.set_title('家长在家庭教育中关注和重视的方面')
ax.set_ylim(0, 80)
plt.xticks(rotation=30, ha='right')
plt.tight_layout()

plt.show()