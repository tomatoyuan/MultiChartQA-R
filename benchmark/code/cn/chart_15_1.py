import matplotlib.pyplot as plt

# 省份数据
provinces = ["辽宁", "江苏", "湖北", "北京", "山东", "广东", "浙江", "上海", "四川", "湖南"]
# 对应金牌数
gold_medals = [36, 29, 26, 22, 22, 22, 16, 15, 14, 14]
# 设置柱状图颜色
bar_color = "#FFD700"  # 金色，可根据需求调整
# 创建柱状图
bars = plt.bar(provinces, gold_medals, color=bar_color)
# 添加标题和坐标轴标签，设置字体大小
plt.title("第23届~第30届各省奥运会金牌总数TOP10", fontsize=14, fontweight='bold')
plt.xlabel("省份", fontsize=12)
plt.ylabel("金牌数", fontsize=12)
# 添加数值标注
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2., height,
             '%d' % int(height),
             ha='center', va='bottom', fontsize=10)
# 旋转 x 轴刻度标签，避免重叠，根据实际情况调整旋转角度
plt.xticks(rotation=45)
# 显示图表
plt.tight_layout()  # 自动优化布局
plt.show()