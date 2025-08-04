import matplotlib.pyplot as plt
import numpy as np

# 数据整理
companies = ["伊利集团", "光明乳业", "新乳业"]
# 2022年营业收入（亿元）
revenue_2022 = [1227.0, 282.15, 100.06]  
# 2023年中期营业收入（亿元）
revenue_2023h = [659.82, 141.39, 52.98]  
# 2022年液态乳占比（%）
ratio_2022 = [69.22, 57.03, 87.76]  
# 2023年液态乳占比（%）
ratio_2023 = [64.29, 58.40, 90.94]  

x = np.arange(len(companies))  # 乳企名称作为X轴坐标
width = 0.35  # 柱状图宽度

# 创建画布
fig, ax1 = plt.subplots(figsize=(10, 6))

# 绘制 2022年和2023年中期营业收入柱状图
bar_2022 = ax1.bar(x - width/2, revenue_2022, width, label='2022年营业收入', color='#FF7F50')
bar_2023h = ax1.bar(x + width/2, revenue_2023h, width, label='2023年中期营业收入', color='#40E0D0')

# 标注营业收入数值
for bar in bar_2022 + bar_2023h:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, height + 5, f'{height:.1f}亿元', ha='center', va='bottom')

# 配置左侧Y轴（营业收入）
ax1.set_ylabel('营业收入（亿元）', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(companies, fontsize=12)
ax1.legend(loc='upper left')

# 创建右侧Y轴（液态乳占比）
ax2 = ax1.twinx()
ax2.plot(x, ratio_2022, marker='o', color='#FFD700', label='2022年液态乳占比', linewidth=2)
ax2.plot(x, ratio_2023, marker='s', color='#DA70D6', label='2023年液态乳占比', linewidth=2)

# 标注液态乳占比数值
for i, (r22, r23) in enumerate(zip(ratio_2022, ratio_2023)):
    ax2.text(i, r22 + 1, f'{r22:.2f}%', ha='center', va='bottom', color='#FFD700')
    ax2.text(i, r23 + 1, f'{r23:.2f}%', ha='center', va='bottom', color='#DA70D6')

# 配置右侧Y轴（液态乳占比）
ax2.set_ylabel('液态乳收入占比（%）', fontsize=12)
ax2.legend(loc='upper right')

# 图表标题
plt.title('部分中国乳企营业收入及液态乳收入占比', fontsize=14, pad=20)
plt.tight_layout()
plt.show()