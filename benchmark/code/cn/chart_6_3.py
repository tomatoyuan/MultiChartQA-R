import matplotlib.pyplot as plt
import numpy as np

# 数据定义
categories = ["一线城市", "二线城市", "三线城市", "四线城市"]
percentages = [42, 20, 17, 12]  # 占比数据
growth_rates = [2, 3, -8, -7]   # 增速数据

# 创建画布和双Y坐标轴
fig, ax1 = plt.subplots(figsize=(8, 5))
ax2 = ax1.twinx()

# 绘制占比柱状图
x = np.arange(len(categories))
bars = ax1.bar(
    x, percentages, 
    color="blue", 
    width=0.5, 
    label="占比"
)
ax1.set_ylabel("占比（%）", fontsize=12, color="blue")
ax1.set_ylim(0, 45)
ax1.tick_params(axis="y", labelcolor="blue")

# 绘制增速折线图
ax2.plot(
    x, growth_rates, 
    color="orange", 
    marker="o", 
    label="增速"
)
ax2.set_ylabel("增速（%）", fontsize=12, color="orange")
ax2.set_ylim(-10, 4)
ax2.tick_params(axis="y", labelcolor="orange")

# 设置X轴刻度和标签
ax1.set_xticks(x)
ax1.set_xticklabels(categories)

# 设置标题
plt.title("5月法律服务行业分城市等级关注度占比和增速", fontsize=14, y=1.02)

# 为柱状图添加占比数据标注（仅保留条形数据标注）
for bar in bars:
    height = bar.get_height()
    ax1.annotate(
        f'{height}%',  # 显示百分比符号
        xy=(bar.get_x() + bar.get_width() / 2, height),
        xytext=(0, 5),  # 向上偏移5个点，避免与柱顶重叠
        textcoords="offset points",
        ha='center', va='bottom',
        fontsize=10,
        color='blue',  # 与柱状图同色，增强关联性
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="blue", alpha=0.8)  # 白色背景框突出显示
    )

# 调整图例位置到图表下方
fig.legend(
    loc="lower center", 
    bbox_to_anchor=(0.5, -0.05),
    ncol=2, 
    frameon=False
)

# 优化布局
plt.subplots_adjust(bottom=0.2)
plt.tight_layout()

# 显示图表
plt.show()