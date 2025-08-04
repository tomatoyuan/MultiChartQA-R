import matplotlib.pyplot as plt
import numpy as np

# 数据
labels = ['书店咖啡', '花园咖啡', '露营咖啡', '博物馆咖啡', '剧院咖啡', '健身房咖啡', '菜市场咖啡', '寺庙咖啡']
values = [62, 58, 50, 47, 43, 37, 18, 17]

# 创建绘图对象
fig, ax = plt.subplots()

# 绘制横向条形图
bars = ax.barh(labels, values, color='#8FBC8F')  # 颜色可根据实际需求调整

# 在每个条形上标注数值和百分号
for bar, value in zip(bars, values):
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
            f'{value}', ha='left', va='center', fontsize=10)

# 设置标题和样式
ax.set_title('消费者对咖啡馆与不同业态跨界融合形式偏好')
ax.spines['right'].set_visible(False)  # 隐藏右侧边框
ax.spines['top'].set_visible(False)    # 隐藏顶部边框

# 调整布局使标注更美观
plt.tight_layout()

# 显示图表
plt.show()