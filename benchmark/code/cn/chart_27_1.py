import matplotlib.pyplot as plt
import numpy as np

# 电视剧名称
labels = ["漂洋过海来看你", "剃刀边缘", "人民的名义", "云巅之上"]
# 对应搜索指数数据
values = [16693, 75744, 243831, 60535]
# 为每组数据设置颜色（可根据需求调整）
colors = ['c', 'orange', 'r', 'm']  

x = np.arange(len(labels))  # x 轴坐标

fig, ax = plt.subplots()
# 绘制柱状图
bars = ax.bar(x, values, color=colors)  

# 在柱子上方添加数值标签
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height, str(height),
            ha='center', va='bottom')  

# 设置 x 轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(labels)
# 设置图表标题
ax.set_title('春季档电视剧搜索指数', fontsize=14, fontweight='bold')  
# 设置 y 轴标签（这里因原图表未明确，简单示例可不设或按需补充）
# ax.set_ylabel('搜索指数')  

plt.show()