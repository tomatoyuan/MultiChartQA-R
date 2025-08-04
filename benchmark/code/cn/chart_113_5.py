import matplotlib.pyplot as plt
import numpy as np

# 关注的内容类型
contents = ["营养健康饮食建议", "母婴知识经验分享", "在线医生问诊", "孕期心理辅导与情绪管理", 
            "专家知识问答", "亲子互动与活动", "孕期育儿全过程记录", "商城产品购买"]
# 对应占比（%）
proportions = [33.40, 32.59, 30.75, 29.94, 29.33, 28.31, 28.11, 27.29]

x = np.arange(len(contents))  # x轴坐标

fig, ax = plt.subplots(figsize=(10, 6))
# 绘制柱状图
bars = ax.bar(x, proportions, color='orange')

# 添加数值标注
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# 设置x轴刻度和标签，旋转标签
ax.set_xticks(x)
ax.set_xticklabels(contents, rotation=45, ha='right')
ax.set_ylabel('占比（%）')
ax.set_title('2025年中国母婴消费者使用母婴垂直APP时关注的内容')

plt.tight_layout()
plt.show()