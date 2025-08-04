import matplotlib.pyplot as plt
import numpy as np

# 类别
categories = ['货架', '内容']
# 国货品牌数据
domestic_data = [22, 27]
# 国际品牌数据
international_data = [8, 3]

x = np.arange(len(categories))  # x轴位置
width = 0.35  # 柱子宽度

fig, ax = plt.subplots()
# 绘制国货品牌柱子
rects1 = ax.bar(x - width/2, domestic_data, width, label='国货品牌', color='#4B72C2')  
# 绘制国际品牌柱子
rects2 = ax.bar(x + width/2, international_data, width, label='国际品牌', color='#F08C2E')  

# 为柱子添加数据标签
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

add_labels(rects1)
add_labels(rects2)

# 设置x轴刻度标签
ax.set_xticks(x)
ax.set_xticklabels(categories)
# 设置y轴标签（原图表未明确显示，可根据需求添加）
# ax.set_ylabel('数量')
# 设置图表标题
ax.set_title('MAT2024TOP30品牌国货&国际品牌占比')
# 添加图例
ax.legend()

plt.tight_layout()  # 调整布局，确保标签显示完整
plt.show()