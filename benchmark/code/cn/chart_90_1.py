import matplotlib.pyplot as plt

# 数据
quarters = ["2021Q2", "2021Q3", "2021Q4", "2022Q1"]
sales = [7.0, 5.0, 4.2, 10.9]
colors = ['#AED581', '#81C784', '#4DB6AC', '#9575CD']  # 柔和配色

# 创建画布
fig, ax = plt.subplots(figsize=(7, 5))

# 绘制圆环图
wedges, texts, autotexts = ax.pie(
    sales, 
    labels=quarters, 
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    wedgeprops=dict(width=0.6, edgecolor='white')
)

# 美化百分比文本
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(10)

# 添加总销售额文本到中央
total_sales = sum(sales)
ax.text(0, 0, f'{total_sales:.1f}亿\n总销售额',
        ha='center', va='center',
        fontsize=13, fontweight='bold',
        color='#424242')

# 设置标题
ax.set_title("2021Q2-2022Q1啤酒电商销售额占比（单位：亿元）", fontsize=14, fontweight="bold", pad=20)

plt.tight_layout()
plt.show()