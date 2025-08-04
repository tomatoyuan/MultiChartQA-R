import matplotlib.pyplot as plt
# 数据
labels = ["未确定关系的异性", "男朋友", "丈夫"]
values = [119, 1115, 139]
# 创建柱状图
plt.bar(labels, values, color="#F48FB1")  # 粉色系颜色，接近原图风格
# 添加标题和标签
plt.title("女性送礼对象比例", fontsize=16, fontweight="bold")
plt.xlabel("送礼对象", fontsize=12)
plt.ylabel("数量", fontsize=12)
# 显示数值在柱子上方
for i, v in enumerate(values):
    plt.text(i, v + 10, str(v), ha="center", fontsize=10)
# 优化布局并显示
plt.tight_layout()
plt.show()