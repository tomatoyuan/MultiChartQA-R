import matplotlib.pyplot as plt
import numpy as np

fraud_methods = [
    "猜猜我是谁", "冒充公检法\n'协助调查'", "冒充\n电信/邮局", "消费退税",
    "伪装熟人\n行骗", "虚假\n中奖短信", "'响一声'\n骗回电", "群发\n卡号/姓名"
]
values = np.array([15, 30, 10, 5, 20, 8, 7, 5])  # 使用更真实的数据比例
total = sum(values)

# 创建画布
fig, ax = plt.subplots(figsize=(10, 8), facecolor='#f8f9fa')
fig.patch.set_alpha(0.9)  # 设置画布透明度

# 定义爆炸效果，突出显示占比最大的部分
explode = [0.05 if v == max(values) else 0 for v in values]

# 自定义颜色方案（使用更鲜明的配色）
colors = [
    '#ff6b6b', '#4ecdc4', '#ffd166', '#06d6a0', 
    '#118ab2', '#ef476f', '#9381ff', '#ff9f1c'
]

# 绘制饼图
wedges, texts, autotexts = ax.pie(
    values,
    explode=explode,
    labels=None,  # 暂时不显示标签，通过图例展示
    autopct=lambda p: f'{p:.1f}%\n({int(p*total/100)})',  # 同时显示百分比和实际数量
    startangle=140,
    colors=colors,
    wedgeprops=dict(width=0.7, edgecolor='w', linewidth=1),  # 环形饼图效果
    pctdistance=0.85,  # 百分比标签位置
    textprops={'fontsize': 10, 'weight': 'bold', 'color': 'w'}
)

# 添加标题和副标题
ax.set_title("电信诈骗常见手段分布", fontsize=18, fontweight="bold", pad=20)

# 添加图例
legend = ax.legend(
    wedges, fraud_methods,
    title="诈骗手段",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1),
    fontsize=11,
    title_fontsize=13
)
legend.get_frame().set_alpha(0.8)  # 图例背景半透明

# 美化布局
plt.tight_layout(pad=4)  # 增加边距
plt.subplots_adjust(right=0.75)  # 为图例腾出空间

# 显示图表
plt.show()