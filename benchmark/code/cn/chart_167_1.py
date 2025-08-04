import matplotlib.pyplot as plt

# 设置数据
months = ['Jan\'23', 'Mid\'23', 'Jan\'24']
life_cost = [57, 63, 63]
economy = [48, 42, 53]
job = [38, 57, 48]

# 创建图表
plt.figure(figsize=(10, 6))
plt.plot(months, life_cost, marker='o', label='生活成本提升', color='#2F66FF')
plt.plot(months, economy, marker='o', label='经济放缓', color='#0D1C55')
plt.plot(months, job, marker='o', label='工作不稳定', color='#F97316')

# 添加数据标签
for i, value in enumerate(life_cost):
    plt.text(months[i], value + 1, f'{value}%', ha='center', va='bottom', fontsize=10, color='#2F66FF')
for i, value in enumerate(economy):
    plt.text(months[i], value + 1, f'{value}%', ha='center', va='bottom', fontsize=10, color='#0D1C55')
for i, value in enumerate(job):
    plt.text(months[i], value + 1, f'{value}%', ha='center', va='bottom', fontsize=10, color='#F97316')

# 设置标题和图例
plt.title("消费者经济状况变差的原因", fontsize=14, pad=20)
plt.legend(loc='upper center', ncol=3, frameon=False, fontsize=10)

# 设置轴标签和范围
plt.ylim(30, 70)
plt.ylabel('比例（%）')

# 添加数据说明和来源
plt.figtext(0.5, -0.05, "Q: 您的财务状况变差的原因是什么？\nSource: 2024NIQ中国消费者展望", ha='center', fontsize=10)

# 美化布局
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.tight_layout()

plt.show()