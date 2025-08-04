import matplotlib.pyplot as plt

# Charm data
charm_labels = ["Above 700 yuan", "500 - 700 yuan", "350 - 500 yuan", "Below 350 yuan"]
charm_sizes = [12.0, 23.0, 41.0, 24.0]
charm_colors = ["#E4725F", "#F6C85F", "#94B49F", "#92574C"]

# Bracelet data
bracelet_labels = ["Above 1000 yuan", "600 - 1000 yuan", "Below 600 yuan"]
bracelet_sizes = [14.0, 46.0, 40.0]
bracelet_colors = ["#E4725F", "#F6C85F", "#94B49F"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Draw the charm pie chart
wedges, texts, autotexts = ax1.pie(charm_sizes, colors=charm_colors, autopct='%1.1f%%', startangle=90,
                                    wedgeprops=dict(width=0.4))
ax1.set_title('Pandora Charm Price Distribution in China')
# Adjust the legend and place it on the right side of the pie chart
ax1.legend(wedges, charm_labels, title="Price Range", loc="center left", bbox_to_anchor=(1, 0.5))
# Make the annotation text color clearer (distinguish between dark/light slices)
for autotext in autotexts:
    autotext.set_color('blue' if autotext.get_position()[1] > 0.5 else 'black')

# Draw the bracelet pie chart
wedges2, texts2, autotexts2 = ax2.pie(bracelet_sizes, colors=bracelet_colors, autopct='%1.1f%%', startangle=90,
                                      wedgeprops=dict(width=0.4))
ax2.set_title('Pandora Bracelet Price Distribution in China')
ax2.legend(wedges2, bracelet_labels, title="Price Range", loc="center left", bbox_to_anchor=(1, 0.5))
for autotext in autotexts2:
    autotext.set_color('blue' if autotext.get_position()[1] > 0.5 else 'black')

plt.tight_layout()
plt.show()