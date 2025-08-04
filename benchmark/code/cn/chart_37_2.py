import matplotlib.pyplot as plt
import numpy as np

# 分类名称
categories = ["户外功能袜", "鲨鱼裤", "越野跑鞋", "软壳衣裤", "大妈女装", 
              "保暖棉服", "运动球服", "汉服-新中式", "羽绒马甲", "运动POLO衫"]
# 模拟的成交金额增速数据，大体接近原图表比例
data = [92, 88, 65, 60, 55, 52, 48, 45, 42, 38]  

x = np.arange(len(categories))  # x轴位置

fig, ax = plt.subplots()
# 绘制柱状图，设置颜色为类似的棕色系，调整柱子宽度
bars = ax.bar(x, data, width=0.6, color='#b38878')  

# 设置y轴范围
ax.set_ylim([30, 100])  
# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=45, ha='right')  

# 添加y轴标签
ax.set_ylabel('成交金额增速', fontsize=12)  
# 添加标题
ax.set_title('抖音电商24秋冬服饰细分类目生意规模高增TOP10', fontsize=14, pad=20)  

# 添加数据标签
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

# 隐藏顶部和右侧边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()  # 调整布局
plt.show()