import matplotlib.pyplot as plt

# 数据
brands = [
    "NEC欧洲杯之夜",
    "小米欧洲杯沸腾之夜",
    "三星欧洲杯之夜",
    "途观百万车主欧洲杯之夜",
    "君跃荃新时代欧洲杯之夜",
    "看尚魅族良品青年超级晚",
    "海信欧洲杯千人狂欢不眠夜",
    "滴滴出租车欧洲杯之夜",
    "长安铃木大篷车炫酷之夜",
    "宝沃德使馆欧洲杯之夜"
]
ratings = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(10, 6))  # figsize可调整图表大小

# 绘制横向条形图
ax.barh(brands[::-1], ratings[::-1], color='royalblue')  

# 设置标题和坐标轴标签
ax.set_title('争夺“欧洲杯之夜”品牌线下营销星级情况', fontsize=14, fontweight='bold')
ax.set_xlabel('星级评分', fontsize=12)
ax.set_ylabel('品牌活动', fontsize=12)

# 设置x轴刻度（根据星级数量，这里0 - 10 ）
ax.set_xticks(range(0, 11))

# 显示图表
plt.tight_layout()  # 调整布局，避免标签重叠
plt.show()