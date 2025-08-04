import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, PathPatch
from matplotlib.path import Path

# Data configuration (combine gender and age groups)
data = {
    "gender": {
        "groups": ["Male", "Female"],
        "tgi": [120, 93],
        "outer_color": "#D9D9D9",  # Outer serrated ring color
        "inner_colors": ["#4CAD8F", "#4CAD8F"],  # Inner circle colors (dark for male, light for female)
        "title": "By Gender",
        "label_pos": [(-2.2, 0.5), (2.2, 0.5)],  # Label positions (distributed left and right)
        "annotation": "Attention (TGI)"  # Annotation text
    },
    "age": {
        "groups": ["18-24", "25-34", "35-44", ">45 years old"],
        "tgi": [104, 117, 95, 82],
        "outer_color": "#D9D9D9",  # Outer serrated ring color
        "inner_colors": ["#4DA6FF", "#4DA6FF", "#4DA6FF", "#4DA6FF"],  # Blue
        "title": "By Age Group",
        "label_pos": [(-2.2, 1.2), (2.2, 1.2), (-2.2, -0.8), (2.2, -1.8)],  # Label positions
        "annotation": ""  # Do not repeat annotation for age groups
    }
}

# Create a canvas (adjust the height to accommodate two groups)
fig = plt.figure(figsize=(6, 8), facecolor='white')  # Increase the canvas height
ax = fig.add_subplot(111)

# Core function to draw a serrated outer frame
def draw_serrated_ring(center, radius, color, num_teeth=30):
    """
    Draw a fixed outer frame with serrations
    :param center: Coordinates of the circle center (x, y)
    :param radius: Radius of the outer frame
    :param color: Color of the outer frame
    :param num_teeth: Number of serrations (controls aesthetics)
    """
    theta = np.linspace(0, 2 * np.pi, num_teeth * 2, endpoint=False)
    radii = np.array([radius, radius * 0.95] * num_teeth)
    path_data = []
    for t, r in zip(theta, radii):
        x = center[0] + r * np.cos(t)
        y = center[1] + r * np.sin(t)
        path_data.append((Path.MOVETO if t == 0 else Path.LINETO, (x, y)))
    
    # Close the path
    path_data.append((Path.CLOSEPOLY, (center[0], center[1])))
    codes, verts = zip(*path_data)
    path = Path(verts, codes)
    patch = PathPatch(path, facecolor='none', edgecolor=color, lw=2)
    ax.add_patch(patch)

# Function to draw a dynamic inner circle
def draw_dynamic_inner_circle(center, tgi, color, max_tgi=120):
    """
    Draw an inner circle that changes dynamically with TGI
    :param center: Coordinates of the circle center (x, y)
    :param tgi: TGI value
    :param color: Color of the inner circle
    :param max_tgi: Maximum TGI (used for normalization)
    """
    # Calculate the radius of the inner circle according to the TGI ratio
    radius_ratio = np.sqrt(tgi / max_tgi)
    base_radius = 0.9  # Base radius (relative to the outer frame radius of 1.0)
    radius = base_radius * radius_ratio
    
    inner_circle = Circle(center, radius, color=color, zorder=2)
    ax.add_artist(inner_circle)
    
    # Add TGI text
    ax.text(
        center[0], center[1], 
        f"{tgi}", 
        ha='center', 
        va='center', 
        fontsize=14, 
        fontweight='bold', 
        color='#333333',
        zorder=3
    )

# Function to draw a separator line
def draw_separator(y_pos, length=6, color='#E0E0E0', linestyle='-', linewidth=1.5):
    """
    Draw a horizontal separator line
    :param y_pos: Y-coordinate position of the separator line
    :param length: Length of the separator line
    :param color: Color of the separator line
    :param linestyle: Line style
    :param linewidth: Line width
    """
    x_start = -length / 2
    x_end = length / 2
    ax.plot([x_start, x_end], [y_pos, y_pos], color=color, linestyle=linestyle, linewidth=linewidth, zorder=1)

# Draw all groups
for group_type, group_data in data.items():
    # Vertical offset (gender group on top, age group on bottom)
    y_offset = -3.5 if group_type == "age" else 0  # Adjust the vertical offset
    
    # Draw all circles for each group
    for i, (group, tgi, color) in enumerate(zip(
        group_data["groups"], 
        group_data["tgi"], 
        group_data["inner_colors"]
    )):
        # Calculate the center position (alternate left and right)
        center = (1.5 if i % 2 == 1 else -1.5, y_offset + (1.0 if i < 2 else -1.0))
        
        # Draw the serrated outer frame
        draw_serrated_ring(center, radius=1.0, color=group_data["outer_color"])
        
        # Draw the dynamic inner circle
        draw_dynamic_inner_circle(center, tgi, color)
        
        # Add group labels
        label_x, label_y = group_data["label_pos"][i]
        ax.text(
            label_x, label_y + y_offset, 
            group, 
            ha='center', 
            va='center', 
            fontsize=12, 
            fontweight='bold', 
            color='#333333',
            bbox=dict(facecolor='white', edgecolor='none', pad=2),
            zorder=4
        )
    
    # Move the group title up
    title_y = 2.5 + y_offset
    ax.text(
        -2.5, title_y, 
        group_data["title"], 
        ha='left', 
        va='center', 
        fontsize=16, 
        fontweight='bold', 
        color='#333333',
        zorder=5
    )
    
    # Move the annotation arrow up
    if group_data["annotation"]:
        ax.annotate(
            group_data["annotation"], 
            xy=(-0.5, 0.5 + y_offset), 
            xytext=(-1.2, 1.8 + y_offset),
            arrowprops=dict(arrowstyle='->', color='#666666'),
            fontsize=12, 
            color='#666666',
            zorder=6
        )

# Add the overall title
ax.text(
    0, 4.0,  # Move the overall title up
    "Attention to New Chinese Brands by Gender and Age Group (TGI)", 
    ha='center', 
    va='center', 
    fontsize=18, 
    fontweight='bold', 
    color='#333333',
    zorder=7
)

# Move the bottom description text down
ax.text(
    0, -8.0,  # Move the bottom text further down
    "TGI: Measures attention. A value higher than 100 indicates that the user group's attention is higher than the average level.\n"
    "The area of the circle is proportional to the TGI value", 
    ha='center', 
    va='center', 
    fontsize=12, 
    color='#666666',
    zorder=8
)

# Draw three separator lines
draw_separator(y_pos=3.0)  # Separate the title and the gender group
draw_separator(y_pos=-0.5)  # Separate the gender group and the age group
draw_separator(y_pos=-6.4)  # Separate the age group and the bottom annotation

# Set the axis range
ax.set_xlim(-3, 3)
ax.set_ylim(-9, 4.5)  # Expand the Y-axis range to accommodate all content
ax.axis('off')  # Hide the axes

# Adjust the layout
plt.subplots_adjust(left=0.1, right=0.9, top=0.85, bottom=0.25)
plt.show()