import matplotlib.pyplot as plt
import numpy as np

# 数据
price_bands = ['低于50元', '50-100元', '100-300元', '超过300元']
volume_2022 = [0.38, 0.25, 0.22, 0.15]
volume_2023 = [v + d for v, d in zip(volume_2022, [0.12, -0.06, -0.05, -0.01])]
volume_change = ['+12%', '-6%', '-5%', '-1%']

# 绘图
fig, ax = plt.subplots(figsize=(7, 5))
y = np.arange(len(price_bands))
bar_height = 0.35

# 条形图
ax.barh(y - bar_height / 2, volume_2022, height=bar_height, color='#e55322', label='2022H2')
ax.barh(y + bar_height / 2, volume_2023, height=bar_height, color='black', label='2023H2')

# 数值标注
for i in range(len(price_bands)):
    ax.text(volume_2022[i] + 0.005, y[i] - bar_height / 2,
            f'{int(volume_2022[i]*100)}%', va='center', ha='left', fontsize=9,
            color='white' if volume_2022[i] > 0.3 else 'black')
    ax.text(volume_2023[i] + 0.005, y[i] + bar_height / 2,
            f'{int(volume_2023[i]*100)}%', va='center', ha='left', fontsize=9,
            color='white' if volume_2023[i] > 0.3 else 'black')
    ax.text(max(volume_2022[i], volume_2023[i]) + 0.03, y[i],
            volume_change[i], va='center', fontsize=10)

# 样式
ax.set_title('各价格带销量占比变化\n（2023下半年同比 / 抖音服饰鞋包）', fontsize=12)
ax.set_yticks(y)
ax.set_yticklabels(price_bands, fontsize=11)
ax.set_xlim(0, max(volume_2023) + 0.2)
ax.invert_yaxis()
ax.legend(loc='lower right', fontsize=9)
ax.xaxis.grid(True, linestyle='--', alpha=0.3)

# 数据来源
fig.text(0.01, 0.01,
         '数据来源：有米有数新电商营销大数据分析平台，统计时间为2022.6.1–12.31、2023.6.1–12.31',
         ha='left', va='bottom', fontsize=9)

plt.tight_layout(rect=[0, 0.03, 1, 1])
plt.show()