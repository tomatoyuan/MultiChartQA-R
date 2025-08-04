import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2010", "2014", "2018", "2020"]
# 各学段近视人数（万人），数据与图表对应层级一致，可按需微调
data = {
    "小学生": [3107.13, 4458.78, 3722.13, 3818.24],
    "中学生": [3061.82, 3262.66, 3331.25, 3493.92],
    "高中生": [3554.52, 3616.31, 3187.08, 3351.23]
}
# 颜色设置，匹配图表色调
colors = ["#A4C639", "#a8dda8", "#87CEEB"]  

# 创建画布
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制堆叠柱状图
bottom = np.zeros(len(years))
for i, (category, values) in enumerate(data.items()):
    ax.bar(years, values, bottom=bottom, color=colors[i], label=category)
    # 添加数据标注
    for x, y in zip(np.arange(len(years)), values):
        ax.text(x, bottom[x] + y / 2, f'{y}', ha='center', va='center', color='black')
    bottom += np.array(values)

# 设置y轴标签
ax.set_ylabel("近视人数（万人）")
# 设置标题
ax.set_title('2010-2020年全国小学、初中、高中学生近视总人数', fontsize=14, fontweight='bold')

# 添加图例
ax.legend()

# 美化：隐藏顶部、右侧边框
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()