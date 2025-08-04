import matplotlib.pyplot as plt
import numpy as np

# Industry names
industries = ["High - Tech", "Retail", "Banking", "Air Transport", "High - End Manufacturing", "Consumer Packaged Goods",
              "Health and Wellness", "Administrative Management", "Energy", "Basic Materials", "Education", "Real Estate",
              "Semiconductor", "Chemicals", "Infrastructure Engineering", "Public Sector", "Media and Entertainment",
              "Pharmaceuticals and Medical Products", "Telecommunications", "Insurance", "Agriculture"]
# Productivity data (in billions of dollars), roughly simulated and can be adjusted according to actual situation
productivity = [450, 390, 340, 300, 290, 270, 260, 250, 240, 230, 200, 180, 170, 140, 150, 110, 110, 110, 100, 70, 70]
# Mark the indices of industries that need to be specially framed
special_indices = [6, 19]  # Indices corresponding to Health and Wellness, Insurance

x = np.arange(len(industries))  # x - axis tick positions
bar_width = 0.6  # Bar width

fig, ax = plt.subplots(figsize=(12, 6))

# Draw a bar chart, set the color to a similar green
bars = ax.bar(x, productivity, width=bar_width, color='greenyellow')

# Add a title
ax.set_title('Productivity Improvement of Generative AI by Industry')

# Set x - axis tick labels, rotate by a certain angle to avoid overlap
ax.set_xticks(x)
ax.set_xticklabels(industries, rotation=45, ha='right')

# Add red dashed boxes for special industries
for idx in special_indices:
    rect = bars[idx].get_bbox()
    ax.plot([rect.x0, rect.x1, rect.x1, rect.x0, rect.x0],
            [rect.y0, rect.y0, rect.y1, rect.y1, rect.y0],
            'r--', linewidth=1.5)

# Add numerical labels to each bar
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Vertical offset of 3 points
                textcoords="offset points",
                ha='center', va='bottom')

# Set y - axis label
ax.set_ylabel('Productivity (Billions of Dollars)')

plt.tight_layout()  # Automatically adjust the layout to avoid label overlap
plt.show()