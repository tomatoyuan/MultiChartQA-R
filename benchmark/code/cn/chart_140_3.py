import matplotlib.pyplot as plt
import numpy as np

# 续航里程期待数据
mileage_labels = ["150—250公里", "250—350公里", "350—500公里", "500公里以上"]
mileage_sizes = [7.1, 41.2, 29.5, 22.2]
mileage_colors = ["#87CEFA", "#C0C0C0", "#4169E1", "#1E3A78"]

# 安全性能期待数据
safety_labels = ["动力系统保护措施", "轮胎安全性", "安全气囊", "自动泊车系统"]
safety_sizes = [65.7, 59.7, 58.8, 56.5]
safety_colors = ["#87CEFA", "#6495ED", "#4682B4", "#1E3A78"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# 绘制续航里程期待饼图
wedges, texts, autotexts = ax1.pie(mileage_sizes, colors=mileage_colors, autopct='%1.1f%%', startangle=90)
ax1.set_title('2023年中国消费者对新能源汽车续航里程的期待')
ax1.legend(wedges, mileage_labels, title="续航里程区间", loc="center left", bbox_to_anchor=(1, 0.5))
# 调整标注文字颜色
for autotext in autotexts:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

# 绘制安全性能期待分类图（用柱状图模拟，因是单一占比数据）
x = np.arange(len(safety_labels))
ax2.bar(x, safety_sizes, color=safety_colors, width=0.5)
ax2.set_title('2023年中国消费者对新能源汽车安全性能的期待')
ax2.set_ylabel('期待占比（%）')
ax2.set_xticks(x)
ax2.set_xticklabels(safety_labels)
# 添加安全性能数值标注
for i, size in enumerate(safety_sizes):
    ax2.text(i, size + 1, f'{size}%', ha='center', va='bottom')
ax2.legend(safety_labels, title="安全性能项", loc="upper right")

plt.suptitle('2023年中国消费者对新能源汽车的期待调查', fontsize=14)
plt.tight_layout()
plt.show()