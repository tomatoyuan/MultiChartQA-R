import matplotlib.pyplot as plt
import numpy as np

# 礼物类型
gifts = ["手机", "巧克力", "箱包", "鲜花", "香水"]
# 对应礼物的数值
values = [430998, 416132, 411167, 323635, 124097]

# 创建水平条形图
plt.figure(figsize=(10, 6))

# 定义自定义颜色
colors = ['#FF69B4', '#FF7F50', '#FFB6C1', '#FF1493', '#DB7093']

# 绘制带自定义颜色的条形
bars = plt.barh(gifts, values, color=colors)

# 添加标题和标签
plt.title('今年情人节礼物排行', fontsize=16)
plt.xlabel('礼物数量', fontsize=12)
plt.ylabel('礼物类型', fontsize=12)

# 添加格式化的数据标签
for bar in bars:
    width = bar.get_width()
    plt.text(width + 5000, bar.get_y() + bar.get_height()/2,
             f'{width:,}', ha='left', va='center', fontsize=10)

# 设置x轴标签的千位分隔符
plt.gca().get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

# 添加网格线提高可读性
plt.grid(axis='x', linestyle='--', alpha=0.7)

# 调整布局防止标签被裁剪
plt.tight_layout()

# 显示图表
plt.show()