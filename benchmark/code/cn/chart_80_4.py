import matplotlib.pyplot as plt
import numpy as np

# 类别
labels = ["线上线下均有", "线上渠道", "线下渠道"]
# 各类别占比（%），数据大体一致即可
sizes = [75.8, 15.5, 8.7]
# 饼图各部分颜色，尽量贴近原图
colors = ["#A4C639", "#87D3F2", "#64B5F6"]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(6, 6))

# 绘制饼图
wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, autopct='%1.1f%%', 
    startangle=140, colors=colors, 
    textprops={'color': 'black'}
)

# 美化标注文本（调整大小等）
for text in texts + autotexts:
    text.set_fontsize(12)

# 模拟 TGI 箭头标注（指向线下渠道）
# 找到线下渠道对应的楔形
offline_wedge = wedges[2]
# 计算标注位置
annotation = ax.annotate(
    '低线城市消费者\nTGI=208',
    xy=offline_wedge.center,  # 楔形中心
    xytext=(1.2, 0.8),  # 文本位置
    arrowprops=dict(
        facecolor='blue', 
        shrink=0.1, 
        width=1, 
        headwidth=5,
        connectionstyle="arc3,rad=0.3"  # 弧形箭头
    ),
    ha='center', 
    va='bottom',
    color='blue', 
    fontsize=10
)

# 设置标题
ax.set_title("2022年中国婴儿纸尿裤产品消费者购买渠道占比", fontsize=14, fontweight="bold", y=1.05)

plt.tight_layout()  # 自动调整布局
plt.show()