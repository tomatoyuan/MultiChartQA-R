import matplotlib.pyplot as plt

# 数据（假设的热度搜索量数值，可根据实际数据替换）
cities = ['北京', '上海', '成都']
search_volumes = [2200000, 950000, 780000]  # 假设的搜索量数值

# 创建柱状图
plt.figure(figsize=(10, 6))  # 设置图表大小
bars = plt.bar(cities, search_volumes, color=['#b378d8', '#4b79e2', '#4b79e2'])

# 添加标题和标签
plt.title('城市教师资格证热度搜索量对比', fontsize=16, fontweight='bold')
plt.xlabel('城市', fontsize=14)
plt.ylabel('搜索量（次）', fontsize=14)

# 添加数值标签
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 10000,
             f'{height:,}', ha='center', va='bottom', fontsize=12)

# 设置y轴刻度为更易读的格式
plt.ticklabel_format(axis='y', style='plain')

# 显示网格线
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 显示图表
plt.tight_layout()  # 确保标签和标题完整显示
plt.show()