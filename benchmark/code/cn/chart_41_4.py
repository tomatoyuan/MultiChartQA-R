import matplotlib.pyplot as plt

# 数据
labels = ['宠粮食品', '宠物用品', '宠物健康', '宠物活体', '宠物服务']
sizes = [49.7, 35.5, 8.4, 6.2, 0.2]
# 美化颜色方案（使用更柔和的渐变色）
colors = ['#6a89cc', '#82ccdd', '#b8e994', '#f8c291', '#d6a2e8']
# 突出显示最大部分
explode = (0.1, 0, 0, 0, 0)  

# 创建画布和子图
fig, ax = plt.subplots(figsize=(10, 7), dpi=300)

# 绘制带阴影和3D效果的饼图
wedges, texts, autotexts = ax.pie(
    sizes, 
    explode=explode,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    shadow=True,
    wedgeprops={'edgecolor': 'w', 'linewidth': 2},
    textprops={'fontsize': 12, 'weight': 'bold'}
)

# 调整百分比文本颜色
for text in autotexts:
    text.set_color('black')

# 设置标题和图例
ax.set_title('MAT2024宠物电商细分类目销售额占比', fontsize=16, pad=20)
ax.legend(wedges, labels, title="分类", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# 确保饼图是圆形
plt.axis('equal')
plt.tight_layout()

# 保存图表（可选）
# plt.savefig('pet_ecommerce_sales.png', bbox_inches='tight')

plt.show()