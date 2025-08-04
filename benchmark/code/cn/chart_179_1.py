import matplotlib.pyplot as plt

# 年份
years = list(range(2015, 2027))

# 全球零售增长率（黑色线）
retail_growth = [6.2, 6.0, 6.5, 4.5, 5.3, -2.6, 5.0, 6.9, 3.9, 4.3, 3.7, 3.4]

# 全球电商零售增长率（橙色线）
ecommerce_growth = [23.0, 26.8, 28.4, 22.0, 20.9, 26.7, 16.8, 7.1, 8.9, 9.4, 8.8, 8.1]

# 绘图
plt.figure(figsize=(12, 6))
plt.plot(years, retail_growth, marker='o', color='black', label='全球零售增长')
plt.plot(years, ecommerce_growth, marker='o', color='orange', label='全球电商零售增长')

# 标注每个点的数据
for i, (r, e) in enumerate(zip(retail_growth, ecommerce_growth)):
    plt.text(years[i], r + 0.5, f'{r}%', ha='center', va='bottom', fontsize=9, color='black')
    plt.text(years[i], e + 0.5, f'{e}%', ha='center', va='bottom', fontsize=9, color='orange')

plt.title("全球零售以及全球电商零售增长率变化", fontsize=14)
plt.xlabel("年份")
plt.ylabel("增长率（%）")
plt.xticks(years)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()