import matplotlib.pyplot as plt
import numpy as np

# 数据定义
brands = ['苹果', '华为', '荣耀', '小米', 'OPPO', 'vivo']
tgi_data = [95, 105, 110, 95, 92, 95]  # 关注度（TGI）数据
search_ratio_raw = [100, 110, 85, 87, 90, 89]  # 搜索占比折线原始值
search_percent_labels = [30, 44, 5, 7, 10, 8]  # 实际要标注的搜索占比
highlight_huawei = (1, 44)  # 华为特殊标注 (索引, 标注值)
highlight_honor = (2, 110)  # 荣耀特殊标注 (索引, 标注值)

# 初始化图表与双轴
fig, ax1 = plt.subplots(figsize=(7, 5), dpi=100)
ax2 = ax1.twinx()

# 绘制柱状图（TGI）
x = np.arange(len(brands))  # 明确刻度位置
bar_plot = ax1.bar(x, tgi_data, color='#4CAF50', width=0.6, edgecolor='white')
ax1.set_ylim(80, 120)
ax1.set_ylabel('(关注度/TGI)', color='#1f77b4', fontsize=9)
ax1.tick_params(axis='y', labelcolor='#1f77b4', labelsize=8, length=0)  # 去除 y 轴刻度线
ax1.set_xticks(x)  # 新增：明确设置刻度位置
ax1.set_xticklabels(brands, fontsize=9)
ax1.tick_params(axis='x', length=0)  # 去除 x 轴刻度线

# 绘制折线图（搜索占比）
line_plot, = ax2.plot(x, search_ratio_raw, color='#FF9800', marker='o', markersize=5, linewidth=2)
ax2.set_ylim(80, 120)
ax2.set_ylabel('(搜索占比)', color='#FF9800', fontsize=9)
ax2.tick_params(axis='y', labelcolor='#FF9800', labelsize=8, length=0)  # 去除 y 轴刻度线

# 右侧轴百分比映射
def map_to_percent(tick):
    return ((tick - 80) / (120 - 80)) * 60

# 自定义右侧轴刻度与标签
ax2.set_yticks([80, 90, 100, 110, 120])
ax2.set_yticklabels([f'{map_to_percent(tick):.0f}%' for tick in [80, 90, 100, 110, 120]], fontsize=8)

# 添加虚线辅助线（参考原图表）
for y in [90, 100, 110]:
    ax1.axhline(y, color='gray', linestyle='--', linewidth=0.8)

# 特殊数据标注（华为 44%、荣耀 110）
# 华为折线点标注
ax2.text(highlight_huawei[0], search_ratio_raw[highlight_huawei[0]], 
         f'{highlight_huawei[1]}%', 
         ha='center', va='bottom', fontsize=8, color='#FF9800',
         bbox=dict(facecolor='white', edgecolor='gray', pad=2, alpha=0.8))
# 荣耀柱状图标注
ax1.text(highlight_honor[0], tgi_data[highlight_honor[0]] + 1, 
         f'{highlight_honor[1]}', 
         ha='center', va='bottom', fontsize=8, color='black',
         bbox=dict(facecolor='white', edgecolor='gray', pad=2, alpha=0.8))

# 标题与注释
plt.title('主要手机品牌用户对新国货的关注度（TGI）与搜索占比', fontsize=10, fontweight='bold', pad=15)

annotation_text = (
    '注释：在我们的数据统计周期中(2019-2020年),荣耀品牌尚未独立于华为。\n'
    'TGI: 衡量关注度,高于100代表该用户群的关注度高于平均水平。'
)
plt.figtext(0.12, 0.01, annotation_text, fontsize=8, color='gray', wrap=True)

# 图例与布局优化
ax1.legend([bar_plot, line_plot], ['关注度/TGI', '搜索占比'], 
           loc='upper left', fontsize=8, frameon=True, facecolor='white')
plt.tight_layout(pad=3)

# 去除图表周围边框
for spine in ax1.spines.values():
    spine.set_visible(False)
for spine in ax2.spines.values():
    spine.set_visible(False)

plt.show()