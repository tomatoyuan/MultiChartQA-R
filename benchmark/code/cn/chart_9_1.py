import matplotlib.pyplot as plt
import numpy as np

# 严格按照图表顺序定义数据（保持原始顺序）
data = [
    {"province": "广西", "region": "西部", "growth": 145},
    {"province": "宁夏", "region": "西部", "growth": 135},
    {"province": "内蒙古", "region": "西部", "growth": 135},
    {"province": "天津", "region": "东部", "growth": 120},
    {"province": "江西", "region": "中部", "growth": 105},
    {"province": "辽宁", "region": "东北部", "growth": 100},
    {"province": "江苏", "region": "东部", "growth": 100},
    {"province": "河北", "region": "东部", "growth": 90},
    {"province": "浙江", "region": "东部", "growth": 85},
    {"province": "海南", "region": "东部", "growth": 85},
    {"province": "贵州", "region": "西部", "growth": 80},
    {"province": "上海", "region": "东部", "growth": 75},
    {"province": "黑龙江", "region": "东北部", "growth": 70},
    {"province": "广东", "region": "东部", "growth": 65},
    {"province": "湖北", "region": "中部", "growth": 60},
    {"province": "四川", "region": "西部", "growth": 55},
    {"province": "山西", "region": "中部", "growth": 45},
    {"province": "山东", "region": "东部", "growth": 40},
    {"province": "重庆", "region": "西部", "growth": 40},
    {"province": "新疆", "region": "西部", "growth": 35},
    {"province": "北京", "region": "东部", "growth": 30},
    {"province": "河南", "region": "中部", "growth": 25},
    {"province": "湖南", "region": "中部", "growth": 20},
    {"province": "吉林", "region": "东北部", "growth": 10}
]

# 提取数据
provinces = [item["province"] for item in data]
regions = [item["region"] for item in data]
growths = [item["growth"] for item in data]

# 区域-颜色映射（严格匹配原图）
region_color = {
    "东部": "#4CADDF",   # 蓝色
    "中部": "#8FC31F",   # 绿色
    "西部": "#FBBE28",   # 橙色
    "东北部": "#F26522"  # 红色
}
colors = [region_color[reg] for reg in regions]

# 创建画布
plt.figure(figsize=(8, 10))  # 调整画布大小适配数据

# 创建主坐标轴（下x轴）
ax1 = plt.subplot(111)

# 绘制横向条形图（Y轴数据顺序为倒序）
y_pos = np.arange(len(provinces))
bars = ax1.barh(y_pos[::-1], growths, color=colors, height=0.7)

# 设置Y轴标签（省市名称，保持原始顺序）
ax1.set_yticks(y_pos)
ax1.set_yticklabels(provinces[::-1], fontsize=10)

# 设置下x轴刻度（百分比格式）
ax1.set_xlim(0, 150)
ax1.set_xticks([0, 30, 60, 90, 120, 150])
ax1.set_xticklabels(["0%", "30%", "60%", "90%", "120%", "150%"], fontsize=9)
ax1.set_xlabel("增长幅度", fontsize=10)

# 创建上x轴（与下x轴共享Y轴）
ax2 = ax1.twiny()
ax2.set_xlim(ax1.get_xlim())  # 确保上下x轴范围一致
ax2.set_xticks([0, 30, 60, 90, 120, 150])
ax2.set_xticklabels(["0%", "30%", "60%", "90%", "120%", "150%"], fontsize=9)

# 添加标题
plt.title("2020年，各省市用户对新国货搜索的同比增长幅度", 
          fontsize=12, fontweight="bold", y=1.03)

# 手动构建图例（匹配原图位置和样式）
from matplotlib.patches import Patch
legend_patches = [
    Patch(color=region_color["东部"], label="东部"),
    Patch(color=region_color["中部"], label="中部"),
    Patch(color=region_color["西部"], label="西部"),
    Patch(color=region_color["东北部"], label="东北部")
]
ax1.legend(handles=legend_patches, bbox_to_anchor=(1, 0.7), 
           fontsize=9, frameon=False)

# 调整布局（避免图例和内容重叠）
plt.subplots_adjust(left=0.3, right=0.8)  # 预留右侧空间放图例

# 添加数据标注（修正顺序）
for i, bar in enumerate(bars):
    width = bar.get_width()
    ax1.text(width + 2, bar.get_y() + bar.get_height()/2,
             f"{growths[i]}%",  # 修正索引，直接使用i
             ha='left', va='center', fontsize=9)

# 添加注释（严格还原底部注释）
plt.figtext(0.55, 0.05, "注释: 分区参考中国四大经济区域。", 
            ha="center", fontsize=8, color="gray")

# 显示图表
plt.show()