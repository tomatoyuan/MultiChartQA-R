import matplotlib.pyplot as plt
import numpy as np

# 行业名称
industries = ["高科技", "零售业", "银行", "航空运输", "高端制造", "消费品包装货物", "健康康养", "行政管理", "能源", 
              "基本材料", "教育", "房地产", "半导体", "化学", "基础工程", "公共部门", "媒体娱乐", 
              "制药和医疗产品", "远程通讯", "保险", "农业"]
# 生产力数据（十亿美元），大体模拟，可根据实际调整
productivity = [450, 390, 340, 300, 290, 270, 260, 250, 240, 230, 200, 180, 170, 140, 150, 110, 110, 110, 100, 70, 70]
# 标记需要特殊框选的行业索引
special_indices = [6, 19]  # 健康康养、保险对应的索引

x = np.arange(len(industries))  # x 轴刻度位置
bar_width = 0.6  # 条形宽度

fig, ax = plt.subplots(figsize=(12, 6))

# 绘制条形图，颜色设置为接近的绿色
bars = ax.bar(x, productivity, width=bar_width, color='greenyellow')

# 添加标题
ax.set_title('按行业划分的生成式AI的生产力提升')

# 设置 x 轴刻度标签，旋转一定角度避免重叠
ax.set_xticks(x)
ax.set_xticklabels(industries, rotation=45, ha='right')

# 为特殊行业添加红色虚线框
for idx in special_indices:
    rect = bars[idx].get_bbox()
    ax.plot([rect.x0, rect.x1, rect.x1, rect.x0, rect.x0], 
            [rect.y0, rect.y0, rect.y1, rect.y1, rect.y0], 
            'r--', linewidth=1.5)

# 为每个条形添加数值标签
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 垂直偏移 3 个点
                textcoords="offset points",
                ha='center', va='bottom')

# 设置 y 轴标签
ax.set_ylabel('生产力 (十亿美元)')

plt.tight_layout()  # 自动调整布局，避免标签重叠
plt.show()