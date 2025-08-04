import matplotlib.pyplot as plt
import numpy as np

# 电视剧名称
labels = ["人民的名义", "我主沉浮", "国家干部", "国家公诉", "绝对权力"]
# 男性占比
male_percents = [64, 70, 70, 74, 75]
# 女性占比
female_percents = [36, 30, 30, 26, 25]

x = np.arange(len(labels))  # x轴位置
width = 0.35  # 条形宽度

fig, ax = plt.subplots(figsize=(8, 5))
# 绘制男性占比条形
rects_male = ax.barh(x - width/2, male_percents, width, label='男性', color='#8B4513')  
# 绘制女性占比条形
rects_female = ax.barh(x + width/2, female_percents, width, label='女性', color='red')  

# 添加标签、标题
ax.set_yticks(x)
ax.set_yticklabels(labels)
ax.set_xlabel('占比 (%)')
ax.set_title('热门电视剧用户性别分析')
ax.legend()

# 给条形添加数值标签
def label_bars(rects):
    for rect in rects:
        length = rect.get_width()
        ax.text(length + 1, rect.get_y() + rect.get_height()/2,
                f'{length}%', va='center')

label_bars(rects_male)
label_bars(rects_female)

plt.tight_layout()
plt.show()