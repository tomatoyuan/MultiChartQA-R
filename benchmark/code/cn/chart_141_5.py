import matplotlib.pyplot as plt
import numpy as np

# 数据
platforms = ["母婴APP（如妈妈网孕育，宝宝树孕育，妈妈社区）", "女性健康管理APP（如美柚）", 
             "内容社区平台（如小红书）", "社交平台（如微信群）", "短视频平台（如抖音）"]
percentages = [61.5, 16.6, 12.0, 5.0, 4.9]

x = np.arange(len(platforms))

fig, ax = plt.subplots(figsize=(10, 6))

# 绘制水平柱状图
bars = ax.barh(x, percentages, color='orange', label='接触占比（%）')
ax.set_xlabel('接触占比（%）')
ax.set_ylabel('平台类型')
ax.set_yticks(x)
ax.set_yticklabels(platforms)
ax.invert_yaxis()  # 让第一个平台显示在最上方
ax.set_title('2023年中国备孕人群最常接触备孕商品的平台分布')

# 添加数值标注
for bar in bars:
    length = bar.get_width()
    ax.text(length + 1, bar.get_y() + bar.get_height() / 2, 
            f'{length}%', ha='left', va='center')

plt.tight_layout()
plt.show()