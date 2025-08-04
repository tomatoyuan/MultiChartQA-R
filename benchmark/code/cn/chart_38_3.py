import matplotlib.pyplot as plt
import numpy as np

# 抛期类型
categories = ['日抛', '月抛', '双周抛', '季抛', '半年抛', '年抛']
# 透明隐形眼镜占比（模拟数据，大体接近示例比例）
transparent = [25, 20, 15, 10, 5, 2]  
# 彩色隐形眼镜占比（模拟数据，用总和约为示例中对应抛期的比例，如日抛总和约41% ）
colorful = [16, 19, 12, 10, 10, 2]  

x = np.arange(len(categories))  # x轴位置
width = 0.35  # 每个分组中条形的宽度

fig, ax = plt.subplots()
# 绘制透明隐形眼镜的条形
rects1 = ax.bar(x - width/2, transparent, width, label='透明隐形眼镜', color='#5799C6')  
# 绘制彩色隐形眼镜的条形
rects2 = ax.bar(x + width/2, colorful, width, label='彩色隐形眼镜', color='#F28A2B')  

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(categories)
# 设置y轴标签
ax.set_ylabel('占比（%）')  
# 设置标题
ax.set_title('消费者在日常使用中会交替选择日抛和月抛隐形眼镜\n最近一年主要使用的抛期类型')  
ax.legend()

# 在每个条形上方标注数值
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}%'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 数值标注相对于条形的垂直偏移
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.tight_layout()
plt.show()