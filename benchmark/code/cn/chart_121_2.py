import matplotlib.pyplot as plt

# 营收构成类别
labels = ["机构及交易", "财富管理", "投资银行", "投资管理", "国际业务", "其他"]
# 对应占比（%）
sizes = [41.31, 26.99, 9.73, 13.14, 5.99, 2.84]
# 对应颜色（尽量匹配原图，可微调）
colors = ['#E4725F', '#F6C85F', '#81C784', '#94572E', '#C08B30', '#4F4F4F']

fig, ax = plt.subplots(figsize=(6, 6))
# 绘制饼图，autopct 控制数值显示格式，startangle 设置起始角度
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct='%1.2f%%', startangle=90)

# 调整标注文字颜色为白色，让数值在彩色块上更清晰
for autotext in autotexts:
    autotext.set_color('white')

ax.set_title('2023年国泰君安的营业收入构成')

plt.tight_layout()
plt.show()