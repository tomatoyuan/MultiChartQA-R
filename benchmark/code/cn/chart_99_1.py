import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2015年", "2016年", "2017年", "2018年", "2019年", "2020年"]
# 模拟消费量数据（千克，贴近原图趋势）
consumptions = [40.5, 43.9, 45.6, 47.4, 51.4, 51.3]
# 自由配色（可调整，示例用橙色系）
line_color = "#FF8C00"  # 可替换为其他颜色如 "#32CD32"

# 创建画布
fig, ax = plt.subplots(figsize=(7, 5))

# 绘制折线图
x = np.arange(len(years))
line, = ax.plot(x, consumptions, marker='o', color=line_color, label="重量（千克）")

# 添加数据标注
for i, val in enumerate(consumptions):
    ax.annotate(f'{val}',
                xy=(x[i], val),
                xytext=(5, 5),  # 标注位置：右下方偏移 5
                textcoords="offset points",
                ha='center', va='bottom',
                color='black')

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(years)
# 设置y轴刻度（35-55千克，适配数据）
ax.set_ylim(35, 55)
# 设置标题
ax.set_title("2015-2020年全国居民人均鲜瓜果消费量", fontsize=14, fontweight="bold")
# 添加图例
ax.legend()

# 美化：隐藏顶部、右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()