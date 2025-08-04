import matplotlib.pyplot as plt
import numpy as np

# 数据
years = np.arange(2016, 2021)  
# 模拟搜索热度（仅为复现趋势，非真实数据，可替换）
search_heat = [10, 30, 50, 70, 100]  

# 绘图
plt.figure(figsize=(6, 4))
# 渐变色柱状图（简单模拟，更精细可结合 colormap 自定义）
bars = plt.bar(years, search_heat, color=plt.cm.get_cmap('Purples')(np.linspace(0.3, 0.9, len(years))))

# 数据标注
for bar, heat in zip(bars, search_heat):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 2,
             f'{heat}', ha='center', va='bottom', fontsize=10)

# 标题与标签
plt.title('2020，教师资格证搜索爆表！当老师越来越香！', fontsize=12)
plt.xlabel('年份')
plt.ylabel('搜索热度（模拟）')

# 优化显示
plt.xticks(years)
# 隐藏顶部、右侧边框
for spine in ['top', 'right']:  
    plt.gca().spines[spine].set_visible(False)

plt.show()