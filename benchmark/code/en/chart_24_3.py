import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

# Emoji pack color scheme (strictly corresponding to types)
color_map = {
    'Celebrity Emojis': '#FF5252',
    'Text Emojis': '#00E5FF',
    'QQ & WeChat Built - in Emojis': '#FFD740',
    'Elderly - Style Emojis': '#9C27B0',
    'Emoji Icons': '#00E676',
    'Comic Emojis': '#2979FF',
}

# Data definition (keep the original logic)
categories = ['Celebrity Emojis', 'Text Emojis', 'QQ & WeChat Built - in Emojis', 
              'Elderly - Style Emojis', 'Emoji Icons', 'Comic Emojis']
percentages = [43, 27, 21, 16, 25, 41]

#鄙视链关系（明确类型对应，方便颜色映射）
# Disdain chain relationships (clearly correspond to types for easy color mapping)
connections = [
    ('Celebrity Emojis', 'Comic Emojis', 3.5),   # Celebrity → Comic
    ('Comic Emojis', 'Text Emojis', 3),    # Comic → Text
    ('Text Emojis', 'Emoji Icons', 2.5),       # Text → Emoji
    ('Emoji Icons', 'QQ & WeChat Built - in Emojis', 2),    # Emoji → QQ
    ('QQ & WeChat Built - in Emojis', 'Elderly - Style Emojis', 1.5),  # QQ → Elderly
]

# Create a canvas and basic settings
fig, ax = plt.subplots(figsize=(14, 12), facecolor='#FAFAFA')
ax.set_facecolor('#FAFAFA')
ax.grid(True, linestyle='--', alpha=0.3, color='#EEEEEE')

# Draw a pie chart (enhance shadow and border)
wedges, texts, autotexts = ax.pie(
    percentages, 
    labels=categories, 
    autopct=lambda p: f'{p:.1f}%\n({int(p * sum(percentages) / 100)})',
    colors=[color_map[c] for c in categories],
    startangle=140,
    pctdistance=0.75,
    explode=[0.04] * 6,
    shadow=True,
    wedgeprops={'edgecolor': 'white', 'linewidth': 2, 'antialiased': True},
    textprops={'fontsize': 12, 'weight': 'bold', 'color': '#212121'}
)

# Center white mask (enhance the sense of hierarchy)
center_circle = plt.Circle((0, 0), 0.4, color='#FAFAFA', linewidth=0, zorder=1)
ax.add_artist(center_circle)

# Optimize the style of percentage labels (with a white background box)
for a in autotexts:
    a.set_bbox(dict(boxstyle="round,pad=0.3", fc="white", ec="#BDBDBD", alpha=0.85))

# Set the title
ax.set_title('Post - 2000s Version: Disdain Logic - Relevance between Celebrities and Anime', 
             fontsize=22, 
             fontweight='bold', 
             color='#212121',
             pad=25)

# Draw disdain chain arrows (the color strictly corresponds to the main color of the emoji pack)
for start_cat, end_cat, weight in connections:
    # Find the angle of the corresponding sector
    start_wedge = [w for w, l in zip(wedges, categories) if l == start_cat][0]
    end_wedge = [w for w, l in zip(wedges, categories) if l == end_cat][0]
    
    start_angle = (start_wedge.theta2 + start_wedge.theta1) / 2
    end_angle = (end_wedge.theta2 + end_wedge.theta1) / 2
    
    # Calculate coordinates (unified radius to avoid confusion)
    radius = 0.65
    start_x = np.cos(np.radians(start_angle)) * radius
    start_y = np.sin(np.radians(start_angle)) * radius
    end_x = np.cos(np.radians(end_angle)) * radius
    end_y = np.sin(np.radians(end_angle)) * radius
    
    # Draw an arrow (single color, consistent with the color of the starting emoji pack)
    ax.annotate(
        '', 
        xy=(end_x, end_y), 
        xytext=(start_x, start_y),
        arrowprops=dict(
            arrowstyle='-|>', 
            color=color_map[start_cat],  # Use the color of the starting type
            lw=weight,
            connectionstyle="arc3,rad=0.2"
        )
    )

# Build a legend (divided into two groups: types + relationships)
legend_type = [
    Line2D([0], [0], color=color_map[c], lw=4, label=c) 
    for c in categories
]

legend_arrow = [
    Line2D([0], [0], color=color_map[start], lw=weight, label=f'{start} → {end}') 
    for start, end, weight in connections
]

# Combine the legends (types first, then relationships)
legend1 = ax.legend(
    handles=legend_type, 
    loc='upper right', 
    title="Emoji Pack Types", 
    fontsize=11, 
    frameon=True,
    framealpha=0.9, 
    facecolor='white', 
    edgecolor='#BDBDBD'
)
ax.add_artist(legend1)

ax.legend(
    handles=legend_arrow, 
    loc='lower right', 
    title="Disdain Chain Relationships", 
    fontsize=10, 
    frameon=True,
    framealpha=0.9, 
    facecolor='white', 
    edgecolor='#BDBDBD'
)

# Bottom note
plt.figtext(
    0.15, 0.02, 
    "Note: This chart is for fun and the data does not represent real statistical results, for entertainment and discussion only.", 
    ha="left", 
    fontsize=10, 
    bbox={"facecolor":"white", "alpha":0.8, "pad":6}
)

# Adjust the layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()