import matplotlib.pyplot as plt
import numpy as np

# 省份名称
provinces = ["广东", "山东", "江苏", "河南", "浙江", "北京", "湖北", "河北", "湖南", "四川"]
# 模拟的搜索指数数据（可替换为真实数据），数值长度与省份数量一致
search_index = [18, 17, 16, 15, 14, 13, 12, 11, 10, 9]  

y_pos = np.arange(len(provinces))

fig, ax = plt.subplots()
# 绘制横向条形图，height控制条的高度（这里用搜索指数模拟），width控制条的宽度，align调整对齐
ax.barh(y_pos, search_index, height=0.6, align='center', color='orange')  
ax.set_yticks(y_pos)
ax.set_yticklabels(provinces)
# 让条形图从左到右显示（默认横向条形图是从下到上，反转后更贴合原图表视觉）
ax.invert_yaxis()  
ax.set_xlabel('搜索指数示意')
ax.set_title('搜索指数概况')

# 可添加数值标签，在每个条形末端显示数值
for i, v in enumerate(search_index):
    ax.text(v + 0.1, i, str(v), va='center')

plt.show()