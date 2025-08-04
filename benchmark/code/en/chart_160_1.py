# Reset Chinese font and drawing configuration
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Data
years = ['2020', '2021', '2022', '2023']
creators = [900, 1100, 1310, 1420]
growth_rates = ['+22%', '+18%', '+8%']

# Drawing
plt.figure(figsize=(10, 6))
plt.plot(years, creators, marker='o', color='#6A78FF', linewidth=3)

# Label the values of the points (bold, blue)
for i, value in enumerate(creators):
    plt.text(i, value + 30, f"{value}", ha='center', fontsize=14, color='#1F3BB3', fontweight='bold')

# Label the growth rates (larger font, italic, purple)
for i in range(1, len(creators)):
    mid_x = (i - 1 + i) / 2
    mid_y = (creators[i - 1] + creators[i]) / 2 + 20
    plt.text(mid_x, mid_y, growth_rates[i - 1], ha='center', fontsize=16, color='#B03ACC', fontstyle='italic')

# Chart settings
plt.title("Total number of creators with over 10,000 followers on major social platforms (in ten thousands)", fontsize=16, fontweight='bold')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.ylim()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()