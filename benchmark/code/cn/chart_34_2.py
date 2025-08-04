import matplotlib.pyplot as plt
import numpy as np

# 数据（类别、对应百分比，大体接近原数据即可）
labels = ["更注重舒适性和健康性能", "更加注重品牌价值和品质", "更注重自我愉悦感", 
          "更加重视特定场景的功能性", "更注重产品的复合功能"]
percentages = [76.0, 59.2, 52.7, 49.4, 49.1]

# 为每个条形设置位置（横向条形图用 y 轴坐标）
y_pos = np.arange(len(labels))  

# 创建画布和轴对象
fig, ax = plt.subplots(figsize=(8, 5))  # 可调整尺寸适配原图表比例

# 绘制横向条形图，颜色选接近原图表的浅色调，这里用 #D3D3D3 类似灰色系（可根据实际微调）
ax.barh(y_pos, percentages, color='#D3D3D3')  

# 设置 y 轴刻度和标签，让类别显示在左侧
ax.set_yticks(y_pos)
ax.set_yticklabels(labels)

# 设置 x 轴标签（百分比），并调整字体等样式让其更贴近原图表风格
ax.set_xlabel('百分比（%）', fontsize=10)  

# 添加数据标签，在每个条形右侧显示百分比数值
for i, v in enumerate(percentages):
    ax.text(v + 1, i, f'{v}%', va='center', fontsize=9)  

# 隐藏顶部和右侧边框，更贴近原图表简洁风格
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 设置标题（与原图表标题一致）
ax.set_title('消费者内衣消费态度不断进阶，多元与个性化需求增加', fontsize=12, pad=15)  

# 调整布局，避免标签挤压
plt.tight_layout()  

# 显示图表
plt.show()