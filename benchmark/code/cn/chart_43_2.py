import matplotlib.pyplot as plt
import numpy as np

# 国家/地区名称
countries = ["美国", "中国", "日本", "英国", "德国", "印度", "中国【她经济】", "法国", "意大利", "加拿大", "澳大利亚"]
# 对应的数据（单位：万亿人民币，这里根据图表大致估算，你可按实际精准数据调整 ）
data = [1500, 600, 200, 200, 200, 200, 100, 100, 100, 100, 100]  

x = np.arange(len(countries))  # x 轴位置
width = 0.5  # 柱状图宽度

fig, ax = plt.subplots()

# 为每个条形设置颜色，中国【她经济】为黄色，其余为青色
colors = ['cyan'] * len(countries)
index = countries.index("中国【她经济】")
colors[index] = 'orange'

rects = ax.bar(x, data, width, color=colors)

# 修复：使用 bbox 参数替代 padding 参数，并将标注位置上移
ax.text(5.7, 300, "超10万亿人民币", fontsize=12, ha='center', va='bottom',
        bbox=dict(facecolor='orange', alpha=1.0, pad=5))

# 设置 x 轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(countries, rotation=45, ha='right')
# 设置 y 轴标签
ax.set_ylabel('规模（万亿人民币）')
# 设置标题
ax.set_title('2023年我国“她经济”规模足以构成第七大经济体')

# 显示图表
plt.tight_layout()
plt.show()