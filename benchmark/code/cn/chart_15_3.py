import matplotlib.pyplot as plt

# 原始数据（直接使用星号数量）
provinces = ["广东", "江苏", "山东", "浙江", "河南", "台湾", "四川", "河北", "湖北", "湖南"]
stars = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]  # 对应各省份的星号数量

# 反转数据顺序，使星级最高的省份在最上面
provinces_reversed = provinces[::-1]
stars_reversed = stars[::-1]

# 创建画布
plt.figure(figsize=(12, 6))

# 绘制水平条形图（星级最高的在最上面）
plt.barh(provinces_reversed, stars_reversed, color='skyblue')

# 添加星号标签
for i, (province, star_count) in enumerate(zip(provinces_reversed, stars_reversed)):
    plt.text(star_count + 0.2, i, '★' * star_count, va='center', fontsize=12)

# 设置图表标题和坐标轴标签
plt.title('2015年中国省市GDP排名')
plt.xlabel('星级数量')
plt.ylabel('省份')

# 设置x轴范围
plt.xlim(0, max(stars_reversed) + 2)  # 留出足够空间显示星号

# 美化图表
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()  # 确保布局紧凑
plt.show()