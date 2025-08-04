import matplotlib.pyplot as plt
import numpy as np

# 数据
years = [2015, 2016, 2017, 2018]
# 各季度关注度（第1-4季度）
q1 = [1000, 1200, 5000, 4000]  
q2 = [800, 1300, 4800, 5000]
q3 = [600, 1100, 4600, 4500]
q4 = [1200, 1500, 8000, 1500]
# 新发现感染人数
new_infections = [115465, 124555, 134512, 160000]  

# 用于在同一X轴上绘制多组柱状图的偏移量
x = np.arange(len(years))  
width = 0.2  

# 创建画布和子图
fig, ax1 = plt.subplots(figsize=(8, 5))

# 绘制各季度关注度的柱状图
ax1.bar(x - 1.5*width, q1, width, label='第1季度', color='#f78b9b')
ax1.bar(x - 0.5*width, q2, width, label='第2季度', color='#ff5e2d')
ax1.bar(x + 0.5*width, q3, width, label='第3季度', color='#d4b17c')
ax1.bar(x + 1.5*width, q4, width, label='第4季度', color='#3b3b3b')

# 设置左侧Y轴（关注度）的标题
ax1.set_ylabel('关注度', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# 创建右侧Y轴，用于绘制新发现感染人数的折线图
ax2 = ax1.twinx()
line, = ax2.plot(x, new_infections, marker='o', color='#8bc34a', label='新发现感染人数')

# 添加折线数据标注
for i, (x_val, y_val) in enumerate(zip(x, new_infections)):
    # 将感染人数转换为带千位分隔符的字符串
    y_text = f"{y_val:,}"
    ax2.annotate(y_text,  # 标注文本
                 (x_val, y_val),  # 数据点位置
                 textcoords="offset points",  # 文本坐标相对于数据点的偏移
                 xytext=(0,10),  # X和Y方向的偏移量
                 ha='center',  # 水平对齐方式
                 fontsize=9)  # 字体大小

ax2.set_ylabel('新发现感染人数', fontsize=12)
ax2.legend(loc='upper right')

# 图表标题
plt.title('“艾滋病”相关信息关注度与新发现感染人数（2015-2018）', fontsize=14, pad=20)

# 调整布局
plt.tight_layout()
# 显示图表
plt.show()