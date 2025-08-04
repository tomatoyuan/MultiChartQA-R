import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# -------------------- Data Definition --------------------
# Node information: name, percentage, color
nodes = [
    {"name": "Short text and image", "percent": 82.9, "color": "#a5d65d", "desc": "Such as posting daily status, like photos, internet emoticons/GIFs"},
    {"name": "Short video/mini - video", "percent": 74.0, "color": "#81c784", "desc": "Video content within about 5 minutes"},
    {"name": "Long text", "percent": 33.2, "color": "#4dd0e1", "desc": "Long blog posts, online novels, official account articles, etc."},
    {"name": "Music and audio", "percent": 25.8, "color": "#ffe082", "desc": "Such as original music, K - song covers, audio program production, etc."},
    {"name": "Medium - long video", "percent": 29.1, "color": "#87de87", "desc": "Over 5 minutes, such as life vlogs, experience sharing, etc."}
]

# Connection relationships (simulating a circular connection)
edges = [
    (0, 1), (1, 2), (2, 3), (3, 4), (4, 0)
]

# -------------------- Create Graph Structure --------------------
G = nx.Graph()
# Add nodes
for i, node in enumerate(nodes):
    G.add_node(i, 
               name=node["name"], 
               percent=node["percent"], 
               color=node["color"],
               desc=node["desc"])
# Add edges
G.add_edges_from(edges)

# -------------------- Layout Settings (Circular Layout) --------------------
pos = nx.circular_layout(G, scale=0.8)  # Circular layout, increase scale to disperse nodes

# -------------------- Create Canvas --------------------
fig, ax = plt.subplots(figsize=(8, 8))

# -------------------- Draw Nodes (with color and size) --------------------
node_sizes = [n["percent"] * 48 for n in nodes]  # Node size is positively correlated with the percentage
node_colors = [n["color"] for n in nodes]

nx.draw_networkx_nodes(
    G, pos,
    node_size=node_sizes,
    node_color=node_colors,
    alpha=0.8,
    ax=ax
)

# -------------------- Draw Edges (Gray Connecting Lines) --------------------
nx.draw_networkx_edges(
    G, pos,
    width=2,
    edge_color="#cccccc",
    ax=ax
)

# -------------------- Add Node Annotations (Name, Percentage, Description) --------------------
for i, node in enumerate(nodes):
    # Annotate the name and percentage (inside the node)
    ax.text(
        pos[i][0], pos[i][1], 
        f"{node['name']}\n{node['percent']}%",
        ha="center", va="center",
        fontsize=8,
        color="blue",
        fontweight="bold"
    )
    # Annotate the description information (outside the node, adjust the offset)
    desc_x = pos[i][0] + (1.5 if pos[i][0] > 0 else -1.5) * 0.1  # Horizontal offset
    desc_y = pos[i][1] + (1.5 if pos[i][1] > 0 else -1.5) * 0.1  # Vertical offset
    ax.text(
        desc_x, desc_y, 
        node["desc"],
        ha="left" if pos[i][0] > 0 else "right",
        va="center",
        fontsize=9,
        color="#424242"
    )

# -------------------- Beautify the Chart --------------------
# Hide the axes
ax.axis("off")

# Add a title
ax.set_title(
    "Types of Original Content Published by Chinese Beauty - shooting APP Users in 2022",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Adjust the layout
plt.tight_layout()

plt.show()