import matplotlib.pyplot as plt

# 体检原因
reasons = ["个人定期健康检查", "硬性规定检查（例：婚检、入职前体检）", 
           "突然想了解自身健康情况", "患有疾病急需检查"]
# 对应占比（%）
proportions = [50.82, 44.83, 44.46, 31.22]
# 对应颜色（与图表中橙色一致）
colors = ['#FF7F27', '#1E90FF', '#4B53FF', '#32CD32'] * len(reasons)  

fig, ax = plt.subplots(figsize=(8, 8))
# 绘制环形图，设置宽度让中间空心，wedgeprops 控制环形样式
wedges, texts, autotexts = ax.pie(proportions, labels=reasons, colors=colors, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})  

# 调整标注文字位置，让其在环形合适区域（针对这种环形布局做适配）
for autotext in autotexts:
    autotext.set_horizontalalignment('center')
    autotext.set_verticalalignment('center')

ax.set_title('2025年中国健康体检消费者参加体检原因')

plt.show()