import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# -------------------- 数据定义 --------------------
# 节点信息：名称、百分比、颜色
nodes = [
    {"name": "短图文类", "percent": 82.9, "color": "#a5d65d", "desc": "如发布日常状态，如照片、网络表情/GIF图等"},
    {"name": "短视频/小视频类", "percent": 74.0, "color": "#81c784", "desc": "约5分钟以内的视频内容"},
    {"name": "长文类", "percent": 33.2, "color": "#4dd0e1", "desc": "长博文、网文、公众号文章等"},
    {"name": "音乐音频类", "percent": 25.8, "color": "#ffe082", "desc": "如原创音乐、K歌翻唱、音频节目制作等"},
    {"name": "中长视频类", "percent": 29.1, "color": "#87de87", "desc": "5分钟以上，如生活vlog、经验分享等"},
]

# 连接关系（模拟环形连接）
edges = [
    (0, 1), (1, 2), (2, 3), (3, 4), (4, 0)
]

# -------------------- 创建图结构 --------------------
G = nx.Graph()
# 添加节点
for i, node in enumerate(nodes):
    G.add_node(i, 
               name=node["name"], 
               percent=node["percent"], 
               color=node["color"],
               desc=node["desc"])
# 添加边
G.add_edges_from(edges)

# -------------------- 布局设置（环形布局） --------------------
pos = nx.circular_layout(G, scale=0.8)  # 环形布局，扩大 scale 让节点分散

# -------------------- 创建画布 --------------------
fig, ax = plt.subplots(figsize=(8, 8))

# -------------------- 绘制节点（带颜色和大小） --------------------
node_sizes = [n["percent"] * 48 for n in nodes]  # 节点大小与百分比正相关
node_colors = [n["color"] for n in nodes]

nx.draw_networkx_nodes(
    G, pos,
    node_size=node_sizes,
    node_color=node_colors,
    alpha=0.8,
    ax=ax
)

# -------------------- 绘制边（灰色连接线） --------------------
nx.draw_networkx_edges(
    G, pos,
    width=2,
    edge_color="#cccccc",
    ax=ax
)

# -------------------- 添加节点标注（名称、百分比、描述） --------------------
for i, node in enumerate(nodes):
    # 标注名称和百分比（在节点内部）
    ax.text(
        pos[i][0], pos[i][1], 
        f"{node['name']}\n{node['percent']}%",
        ha="center", va="center",
        fontsize=8,
        color="white",
        fontweight="bold"
    )
    # 标注描述信息（在节点外部，调整偏移）
    desc_x = pos[i][0] + (1.5 if pos[i][0] > 0 else -1.5) * 0.1  # 左右偏移
    desc_y = pos[i][1] + (1.5 if pos[i][1] > 0 else -1.5) * 0.1  # 上下偏移
    ax.text(
        desc_x, desc_y, 
        node["desc"],
        ha="left" if pos[i][0] > 0 else "right",
        va="center",
        fontsize=9,
        color="#424242"
    )

# -------------------- 美化图表 --------------------
# 隐藏坐标轴
ax.axis("off")

# 添加标题
ax.set_title(
    "2022年中国美颜拍摄类APP用户原创内容发布类型",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# 调整布局
plt.tight_layout()

plt.show()