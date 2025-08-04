import matplotlib.pyplot as plt
import numpy as np

# 促进措施
measures = ["引进青年人才", "加强农村网络基础建设", "政府部门的政策和资金扶持", 
            "提供优质电商运营场地", "加强技术和管理人员的培训", "扶持农业类企业提供更多产品", 
            "规范电商市场，营造良好的经营环境", "行业协会提供更多指导和信息"]
# 对应占比（%）
proportions = [28.79, 30.30, 30.45, 31.52, 31.67, 33.18, 34.09, 34.24]

y = np.arange(len(measures))  # y轴坐标

fig, ax = plt.subplots(figsize=(10, 7))
# 绘制水平柱状图
bars = ax.barh(y, proportions, color='orange')

# 添加数值标注
for i, proportion in enumerate(proportions):
    ax.text(proportion, i, f'{proportion}', va='center', ha='left', fontsize=9)

# 设置y轴刻度和标签
ax.set_yticks(y)
ax.set_yticklabels(measures)
ax.set_xlabel('占比（%）')
ax.set_title('2025年中国农村电商消费者认为有效促进农村电商发展措施')

plt.tight_layout()
plt.show()