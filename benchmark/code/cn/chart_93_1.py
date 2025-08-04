import matplotlib.pyplot as plt
import numpy as np

# 月份
months = ["2021.4", "2021.5", "2021.6", "2021.7", "2021.8", "2021.9", "2021.10", "2021.11", "2021.12"]
# （天猫+淘宝）美护发整体月成交额指数（模拟数据）
tmall_taobao = [1400000000, 1200000000, 2200000000, 1100000000, 1500000000, 1700000000, 1300000000, 3200000000, 1400000000]
# （天猫国际）美护发整体月成交额指数（模拟数据）
tmall_global = [500000000, 500000000, 900000000, 400000000, 600000000, 600000000, 500000000, 1400000000, 500000000]
# 年增长数据
annual_growth = "+12.3%"
annual_growth_desc = "美护发市场年成交额\n(指数) 增长"

# 创建画布
fig, ax = plt.subplots(figsize=(10, 6))

ax.set_ylim(0, 5000000000)

# 绘制折线图（天猫+淘宝）
ax.plot(months, tmall_taobao, marker='o', color="#A4C639", label="(天猫+淘宝) 美护发整体月成交额指数", linewidth=2)
# 绘制折线图（天猫国际）
ax.plot(months, tmall_global, marker='o', color="#87CEEB", label="(天猫国际) 美护发整体月成交额指数", linewidth=2)

# 添加数据标注（简化，可按需完善）
for x, y in zip(months, tmall_taobao):
    ax.annotate(f'{y/1000000000:.1f}亿',
                xy=(x, y),
                xytext=(0, 5),
                textcoords="offset points",
                ha='center', va='bottom',
                color="#A4C639")
for x, y in zip(months, tmall_global):
    ax.annotate(f'{y/1000000000:.1f}亿',
                xy=(x, y),
                xytext=(0, 5),
                textcoords="offset points",
                ha='center', va='bottom',
                color="#87CEEB")

# 设置y轴标签
ax.set_ylabel("成交额指数")
# 设置标题
ax.set_title("2021年中国美护发整体：月成交额指数趋势变化", fontsize=14, fontweight='bold')

# 添加图例
ax.legend(loc='upper right')

# 美化：隐藏顶部、右侧边框
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()