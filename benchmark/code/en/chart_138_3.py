import matplotlib.pyplot as plt

# Haidilao data
haidilao_labels = ["First-tier", "New first-tier", "Second-tier", "Third-tier", "Fourth-tier", "Fifth-tier", "Other"]
haidilao_sizes = [17.3, 30.1, 21.7, 16.9, 8.5, 4.0, 1.5]
haidilao_provinces = {"Guangdong Province": 162, "Zhejiang Province": 111, "Shandong Province": 77}
haidilao_colors = ["#FF7F50", "#FFD700", "#32CD32", "#8B4513", "#9370DB", "#8B8B83", "#F4A460"]

# Xiaolongkan data
xiaolongkan_labels = ["First-tier", "New first-tier", "Second-tier", "Third-tier", "Fourth-tier", "Fifth-tier", "Other"]
xiaolongkan_sizes = [8.9, 18.8, 24.0, 8.3, 25.7, 13.0, 1.3]
xiaolongkan_provinces = {"Anhui Province": 76, "Guangdong Province": 62, "Jiangsu Province": 44}
xiaolongkan_colors = ["#FF7F50", "#FFD700", "#32CD32", "#8B4513", "#9370DB", "#8B8B83", "#F4A460"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Draw Haidilao donut chart
wedges, texts, autotexts = ax1.pie(haidilao_sizes, colors=haidilao_colors, autopct='%1.1f%%', startangle=90,
                                    wedgeprops=dict(width=0.4))
ax1.set_title('Haidilao Store Distribution')
# Draw province text box
province_text = "\n".join([f"{province}: {count} stores" for province, count in haidilao_provinces.items()])
ax1.text(-1.5, 0.8, province_text, fontsize=10, bbox=dict(facecolor='white', edgecolor='orange', boxstyle='round,pad=0.5'))
# Adjust the legend and place it on the right side of the pie chart
ax1.legend(wedges, haidilao_labels, title="City Tier", loc="center left", bbox_to_anchor=(1, 0.5))
# Make the annotation text color clearer (distinguish between dark/light slices)
for autotext in autotexts:
    autotext.set_color('black' if autotext.get_position()[1] > 0.5 else 'black')

# Draw Xiaolongkan donut chart
wedges2, texts2, autotexts2 = ax2.pie(xiaolongkan_sizes, colors=xiaolongkan_colors, autopct='%1.1f%%', startangle=90,
                                      wedgeprops=dict(width=0.4))
ax2.set_title('Xiaolongkan Store Distribution')
# Draw province text box
province_text2 = "\n".join([f"{province}: {count} stores" for province, count in xiaolongkan_provinces.items()])
ax2.text(0.3, 0.8, province_text2, fontsize=10, ha='right',
         bbox=dict(facecolor='white', edgecolor='orange', boxstyle='round,pad=0.5'))
ax2.legend(wedges2, xiaolongkan_labels, title="City Tier", loc="center right", bbox_to_anchor=(-0.2, 0.5))
for autotext in autotexts2:
    autotext.set_color('black' if autotext.get_position()[1] > 0.5 else 'black')

plt.suptitle('Store Distribution of Some Popular Hot Pot Brands in China in 2023', fontsize=14)
plt.tight_layout()
plt.show()