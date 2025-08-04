import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 场景与对应比例
scenarios = ['约会', '通勤上班', '聚餐', '拍照打卡', '旅游', '居家保暖', '上课']
percentages = [55, 52, 50, 44, 43, 18, 12]

# 倒序排列（为了从上到下显示）
scenarios = scenarios[::-1]
percentages = percentages[::-1]
y_pos = np.arange(len(scenarios))

# 创建渐变色映射
cmap = LinearSegmentedColormap.from_list("softpink", ["#ffe6e6", "#ffb3b3"])

# 绘图
fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.barh(y_pos, percentages, color=cmap(percentages / np.max(percentages)))

# 添加文字标签
for i, (p, label) in enumerate(zip(percentages, scenarios)):
    ax.text(p + 1, i, f"{p}%", va='center', fontsize=11)

# 设置标题和标签
ax.set_yticks(y_pos)
ax.set_yticklabels(scenarios, fontsize=12)
ax.invert_yaxis()  # 最受欢迎的场景显示在最上面
ax.set_xlim(0, 60)
ax.set_title("消费者光腿袜穿着场景调研", fontsize=15, weight='bold')

# 去除边框和多余刻度
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_color('#cccccc')
ax.spines['bottom'].set_color('#cccccc')
ax.xaxis.set_visible(False)

# 添加数据来源
source_text = "数据来源：CBNData2024年7月调研数据\n大数据：全洞察"
plt.figtext(0.5, -0.05, source_text, wrap=True, horizontalalignment='center', fontsize=9, color='gray')

plt.tight_layout()
plt.show()