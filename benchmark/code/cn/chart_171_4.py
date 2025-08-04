import matplotlib.pyplot as plt
import numpy as np

# 数据
price_bands = ['低于50元', '50-100元', '100-300元', '超过300元']
value_2022 = [0.30, 0.28, 0.27, 0.15]
value_2023 = [v + d for v, d in zip(value_2022, [0.09, -0.01, -0.03, -0.04])]
value_change = ['+9%', '-1%', '-3%', '-4%']

# 绘图
fig, ax = plt.subplots(figsize=(7, 5))
y = np.arange(len(price_bands))
bar_height = 0.35

# 条形图
ax.barh(y - bar_height / 2, value_2022, height=bar_height, color='#e55322', label='2022H2')
ax.barh(y + bar_height / 2, value_2023, height=bar_height, color='black', label='2023H2')

# 数值标注
for i in range(len(price_bands)):
    ax.text(value_2022[i] + 0.005, y[i] - bar_height / 2,
            f'{int(value_2022[i]*100)}%', va='center', ha='left', fontsize=9,
            color='white' if value_2022[i] > 0.3 else 'black')
    ax.text(value_2023[i] + 0.005, y[i] + bar_height / 2,
            f'{int(value_2023[i]*100)}%', va='center', ha='left', fontsize=9,
            color='white' if value_2023[i] > 0.3 else 'black')
    ax.text(max(value_2022[i], value_2023[i]) + 0.03, y[i],
            value_change[i], va='center', fontsize=10)

# 样式
ax.set_title('各价格带销售额占比变化\n（2023下半年同比 / 抖音服饰鞋包）', fontsize=12)
ax.set_yticks(y)
ax.set_yticklabels(price_bands, fontsize=11)
ax.set_xlim(0, max(value_2022) + 0.2)
ax.invert_yaxis()
ax.legend(loc='lower right', fontsize=9)
ax.xaxis.grid(True, linestyle='--', alpha=0.3)

# 数据来源
fig.text(0.01, 0.01,
         '数据来源：有米有数新电商营销大数据分析平台，统计时间为2022.6.1–12.31、2023.6.1–12.31',
         ha='left', va='bottom', fontsize=9)

plt.tight_layout(rect=[0, 0.03, 1, 1])
plt.show()