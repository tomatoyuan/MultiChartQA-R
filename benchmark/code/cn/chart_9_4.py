import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
import random

# 设置随机种子，确保结果可重现
np.random.seed(42)
random.seed(42)

# 精准提取图表数据，调整为浮点数并添加轻微随机偏移
# 数据格式：省份: (搜索占比, 关注度TGI, 区域, 颜色)
province_data = {
    "江西": (4.2, 171.5, "中部", "#00cc99"),
    "天津": (2.1, 132.3, "东部", "#66b3ff"),
    "贵州": (1.9, 121.7, "西部", "#ffcc66"),
    "河北": (6.3, 120.8, "东部", "#66b3ff"),
    "山东": (8.9, 131.2, "东部", "#66b3ff"),
    "江苏": (10.1, 140.5, "东部", "#66b3ff"),
    "宁夏": (1.0, 110.3, "西部", "#ffcc66"),
    "上海": (3.2, 99.8, "东部", "#66b3ff"),
    "浙江": (7.1, 100.4, "东部", "#66b3ff"),
    "广东": (9.3, 100.7, "东部", "#66b3ff"),
    "黑龙江": (1.1, 90.2, "东北部", "#ff6666"),
    "安徽": (2.9, 90.5, "中部", "#00cc99"),
    "湖北": (4.1, 89.7, "中部", "#00cc99"),
    "北京": (3.8, 90.3, "东部", "#66b3ff"),
    "广西": (1.2, 80.4, "西部", "#ffcc66"),
    "湖南": (3.1, 79.8, "中部", "#00cc99"),
    "吉林": (0.9, 70.6, "东北部", "#ff6666"),
    "福建": (3.3, 70.1, "东部", "#66b3ff"),
    "重庆": (1.1, 70.3, "西部", "#ffcc66"),
    "云南": (1.8, 69.7, "西部", "#ffcc66"),
    "山西": (2.2, 60.5, "中部", "#00cc99"),
    "甘肃": (0.8, 50.2, "西部", "#ffcc66"),
    "新疆": (1.0, 40.3, "西部", "#ffcc66"),
    "青海": (1.1, 30.1, "西部", "#ffcc66"),
    "西藏": (0.9, 20.4, "西部", "#ffcc66"),
    "河南": (5.2, 100.2, "中部", "#00cc99"),
    "海南": (1.0, 99.8, "东部", "#66b3ff"),
    "辽宁": (3.1, 100.3, "东部", "#66b3ff"),
    "四川": (5.0, 99.7, "西部", "#ffcc66"),
    "内蒙古": (2.1, 120.5, "西部", "#ffcc66"),
    "陕西": (1.9, 110.2, "西部", "#ffcc66"),
}

# 按区域分组
region_dict = defaultdict(list)
for prov, (ratio, tgi, region, color) in province_data.items():
    region_dict[region].append((prov, ratio, tgi, color))

# 创建画布
plt.figure(figsize=(10, 7), facecolor='white')
ax = plt.gca()

# 绘制散点图（按区域循环）
for region, prov_list in region_dict.items():
    ratios = [d[1] for d in prov_list]
    tgis = [d[2] for d in prov_list]
    colors = [d[3] for d in prov_list]
    ax.scatter(ratios, tgis, c=colors, label=region, s=50, zorder=2)

    # 添加省份文本标注（微调位置避免重叠）
    for d in prov_list:
        prov, ratio, tgi, _ = d
        # 手动微调部分省份标注位置（根据原图视觉调整）
        if prov == '江西':
            ax.text(ratio + 0.1, tgi - 5, prov, fontsize=9)
        elif prov in ['天津', '江苏']:
            ax.text(ratio - 0.3, tgi + 2, prov, fontsize=9)
        else:
            ax.text(ratio + 0.1, tgi + 1, prov, fontsize=9)

# 绘制关注度TGI=100的参考线
ax.axhline(y=100, color='gray', linestyle='--', linewidth=1, zorder=1)

# 设置坐标轴标签
ax.set_xlabel('搜索占比(%)', fontsize=12, labelpad=15)
ax.set_ylabel('关注度(TGI)', fontsize=12, labelpad=15)

# 设置标题
ax.set_title('各省市用户对新国货的搜索占比与关注度(TGI)', fontsize=14, pad=20)

# 调整坐标轴范围和刻度
ax.set_xlim(0, 11)
ax.set_ylim(0, 180)
ax.set_xticks([1, 3, 5, 7, 9])  # 严格匹配原图x轴刻度
ax.set_yticks(range(20, 180, 20))

# 设置图例（位置与原图对齐）
ax.legend(loc='upper right', bbox_to_anchor=(1, 1), frameon=True, fontsize=10)

# 添加网格
ax.grid(linestyle='--', alpha=0.5, zorder=0)

# 优化布局
plt.tight_layout()
plt.show()