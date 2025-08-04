import matplotlib.pyplot as plt
import numpy as np

# 智能眼镜类型
glasses_types = ["VR智能眼镜", "AR智能眼镜", "AI显示眼镜", "AI音频眼镜", "AI摄影眼镜", "MR智能眼镜", "其他智能眼镜"]
# 对应占比（%），数据大体模拟，可根据实际调整
percentages = [79.4, 69.8, 63.9, 62.0, 55.8, 38.7, 11.9]

x = np.arange(len(glasses_types))  # x轴刻度位置

fig, ax = plt.subplots()

# 绘制条形图，颜色设置为接近的绿色
bars = ax.barh(x, percentages, color='greenyellow')

# 添加标题
ax.set_title('整体被访者听说过的智能眼镜类型')

# 设置y轴刻度标签
ax.set_yticks(x)
ax.set_yticklabels(glasses_types)

# 为每个条形添加数值标签
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(3, 0),  # 水平偏移3个点，垂直居中
                textcoords="offset points",
                ha='left', va='center')

# 隐藏x轴刻度（原图x轴无明显刻度显示，主要看条形长度和标签）
ax.xaxis.set_ticks([])

plt.show()