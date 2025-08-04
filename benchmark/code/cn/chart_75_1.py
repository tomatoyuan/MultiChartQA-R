import matplotlib.pyplot as plt
import numpy as np

# 国家名称
countries = [
    "欧盟", "美国", "日本", "俄罗斯", "加拿大", "韩国",
    "阿尔及利亚", "澳大利亚", "土耳其", "乌克兰", "沙特阿拉伯", "瑞士",
    "巴西", "印度尼西亚", "埃塞俄比亚", "菲律宾", "越南", "墨西哥",
    "哥伦比亚", "印度", "泰国", "委内瑞拉"
]
# 咖啡进口国消费量（千袋），数据大体一致即可
import_consumption = [40251, 26982, 7386, 4681, 4011, 2513,
                      2131, 1962, 1754, 1379, 1253, 1074,
                      0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0]
# 咖啡出口国消费量（千袋），数据大体一致即可
export_consumption = [0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0,
                      22400, 5000, 3798, 3312, 2700, 2420,
                      2045, 1485, 1415, 1100]

# 分组条形图位置设置
x = np.arange(len(countries))
bar_width = 0.35

# 创建画布和子图
fig, ax = plt.subplots(figsize=(10, 8))

# 绘制咖啡进口国消费量条形图
import_bars = ax.barh(x - bar_width/2, import_consumption, height=bar_width, 
                      color="#C6C439", label="咖啡进口国咖啡生豆消费量（千袋）")
# 绘制咖啡出口国消费量条形图
export_bars = ax.barh(x + bar_width/2, export_consumption, height=bar_width, 
                      color="#AD64F6", label="咖啡出口国咖啡生豆消费量（千袋）")

# 添加进口国消费量数据标注
for bar in import_bars:
    width = bar.get_width()
    if width > 0:
        ax.annotate(f'{width}',
                    xy=(width, bar.get_y() + bar.get_height() / 2),
                    xytext=(5, 0),  # 标注位置调整
                    textcoords="offset points",
                    ha='left', va='center')

# 添加出口国消费量数据标注
for bar in export_bars:
    width = bar.get_width()
    if width > 0:
        ax.annotate(f'{width}',
                    xy=(width, bar.get_y() + bar.get_height() / 2),
                    xytext=(5, 0),  # 标注位置调整
                    textcoords="offset points",
                    ha='left', va='center')

# 设置y轴刻度和标签
ax.set_yticks(x)
ax.set_yticklabels(countries)
# 设置x轴标签
ax.set_xlabel("消费量（千袋）")
# 设置标题
ax.set_title("2020年全球主要国家咖啡生豆消费量", fontsize=14, fontweight="bold")

# 添加图例
ax.legend()

# 美化图表，隐藏顶部、右侧和底部边框
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()