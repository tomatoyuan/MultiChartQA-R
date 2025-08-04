import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 数据：省份及对应购物车数量
data = {
    "广东": 6,
    "浙江": 3,
    "北京": 2
}
# 省份坐标（y 轴位置，控制上下排版）
province_y = {
    "广东": 2,
    "浙江": 1,
    "北京": 0
}
# 购物车基础尺寸
cart_width = 0.3
cart_height = 0.2

# 创建画布
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_xlim(0, 7)
ax.set_ylim(-1, 3)
ax.axis('off')  # 隐藏坐标轴

# 绘制标题 - 修改了x坐标和对齐方式
ax.text(
    3.5, 2.8, "哪些省市“剁手”实力更强？",  # x坐标从0.5改为3.5（x轴范围是0-7）
    fontsize=20, fontweight='bold',
    ha='center', va='top'  # ha=center保持居中对齐
)

# 定义绘制单个购物车的函数
def draw_cart(x, y):
    """
    在 (x, y) 位置绘制简化购物车图标
    """
    # 购物车筐（矩形）
    cart_basket = patches.Rectangle(
        (x, y), cart_width, cart_height,
        facecolor='none', edgecolor='black'
    )
    ax.add_patch(cart_basket)
    # 购物车把手（多边形模拟）
    cart_handle = patches.Polygon(
        [[x - 0.1, y + cart_height],
         [x + cart_width + 0.1, y + cart_height],
         [x + cart_width / 2, y + cart_height + 0.2]],
        facecolor='none', edgecolor='black'
    )
    ax.add_patch(cart_handle)
    # 购物车轮子（两个小圆）
    wheel1 = patches.Circle((x + 0.1, y - 0.1), 0.05, color='black')
    wheel2 = patches.Circle((x + 0.2, y - 0.1), 0.05, color='black')
    ax.add_patch(wheel1)
    ax.add_patch(wheel2)

# 遍历数据绘制省份名称 + 购物车
for province, count in data.items():
    # 绘制省份文本
    ax.text(
        0.2, province_y[province] + 0.1, 
        province, fontsize=16, fontweight='bold'
    )
    # 循环绘制购物车
    for i in range(count):
        cart_x = 1 + i * (cart_width + 0.2)  # 购物车横向间隔
        draw_cart(cart_x, province_y[province])

plt.tight_layout()
plt.show()