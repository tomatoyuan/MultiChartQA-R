import matplotlib.pyplot as plt
import numpy as np

# 阶段名称
stages = ["备孕期", "怀孕期", "育儿期"]
# 各阶段对应的关注信息类别（根据图例整理，需与实际数据对应）
categories = ["备孕准备知识", "备孕营养", "备孕监测", "孕期保养", "孕妇服饰", 
              "胎儿发育记录", "孕期食谱", "分娩知识", "婴幼儿服饰/产品", 
              "婴儿食品", "产后护理产品/课程"]
# 模拟数据（需替换为实际完整数据，这里每个阶段的子列表对应categories顺序的占比）
# 实际使用时，需根据图表准确填充各阶段、各类别的占比数值
data = {
    "备孕期": [1.43, 15.89, 21.38, 23.63, 21.59, 21.18, 18.33, 16.09, 14.66, 8.76, 5.91],
    "怀孕期": [7.33, 12.22, 21.38, 31.77, 22.00, 23.83, 23.83, 15.89, 10.79, 6.52, 2.24],
    "育儿期": [4.48, 9.57, 15.27, 20.98, 20.98, 20.98, 17.92, 13.85, 18.33, 15.48, 8.15]
}
# 对应颜色（需根据图表图例准确匹配，这里仅示例，实际以图表为准）
colors = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63', 
          '#00BFFF', '#FFD700', '#1E90FF', '#FF69B4', '#00FA9A', '#FFA07A']

x = np.arange(len(stages))  # x轴对应三个阶段
bar_width = 0.8  # 柱子宽度

fig, ax = plt.subplots(figsize=(12, 8))
bottom = np.zeros(len(stages))

for i, category in enumerate(categories):
    # 遍历每个关注信息类别，绘制堆积柱形
    ax.bar(stages, [data[stage][i] for stage in stages], width=bar_width, 
           bottom=bottom, color=colors[i], label=category)
    # 添加数值标注（仅示例，若数据多可能重叠，可按需调整位置、字体大小等）
    for j in range(len(stages)):
        ax.text(j, bottom[j] + data[stages[j]][i] / 2, 
                f'{data[stages[j]][i]:.2f}', ha='center', va='center', fontsize=7)
    bottom += [data[stage][i] for stage in stages]

ax.set_ylabel('占比（%）')
ax.set_title('2025年中国母婴消费者各阶段重点关注的信息')
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # 图例放右侧，避免遮挡
plt.xticks(x, stages)
plt.tight_layout()
plt.show()