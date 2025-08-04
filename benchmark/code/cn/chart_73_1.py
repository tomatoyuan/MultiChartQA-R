import matplotlib.pyplot as plt

# 数据
labels = ["10-20元", "21-30元", "31-40元", "41元或以上"]
data = [18.4, 50.3, 26.5, 4.8]
colors = ['#FFA07A', '#FF4500', '#FF8C00', '#FFD700']  # 暖色调

# 画环形图
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    data,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    wedgeprops=dict(width=0.4, edgecolor='white')  # 宽度控制成环形
)

# 设置标题
ax.set_title("用户常用即配平台的单次支付费用", fontsize=14, fontweight="bold")

plt.tight_layout()
plt.show()