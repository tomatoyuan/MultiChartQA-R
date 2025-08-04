import matplotlib.pyplot as plt
import numpy as np

# 数据
years = ["2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", 
         "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023年1-11月"]
retail_sales = [4.2, 4.7, 5.1, 5.8, 6.6, 7.7, 9.1, 11.1, 12.8, 15.2, 18.0, 20.6, 23.2, 25.9, 28.7, 31.6, 
                34.7, 37.8, 40.8, 39.2, 44.1, 44.0, 42.8]
growth_rate = [0,11.6, 8.9, 13.1, 14.6, 15.5, 18.0, 22.5, 15.6, 18.5, 18.2, 14.3, 13.0, 11.7, 10.4, 10.2, 
               10.0, 8.8, 8.0, -3.9, 12.5, -0.2,-0.5]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(12, 7))

# 绘制社会消费品零售总额柱状图
ax1.bar(x, retail_sales, color='orange', label='社会消费品零售总额（万亿元）')
ax1.set_ylabel('社会消费品零售总额（万亿元）')
ax1.set_xlabel('年份')
ax1.set_xticks(x)
ax1.set_xticklabels(years, rotation=45, ha='right')
ax1.legend(loc='upper left')

# 创建双轴，绘制同比增长折线图
ax2 = ax1.twinx()
ax2.plot(x, growth_rate, marker='o', color='brown', label='同比增长（%）', linewidth=2)
ax2.set_ylabel('同比增长（%）')
ax2.legend(loc='upper right')

# 添加社会消费品零售总额数值标注
for i, sales in enumerate(retail_sales):
    ax1.text(i, sales + 0.5, f'{sales}', ha='center', va='bottom')

# 添加同比增长数值标注
for i, rate in enumerate(growth_rate):
    ax2.text(i, rate + 0.5, f'{rate}%', ha='center', va='bottom')

ax1.set_title('2001-2023年前11月中国社会消费品零售总额及增速')

plt.tight_layout()
plt.show()