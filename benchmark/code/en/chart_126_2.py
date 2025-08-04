import matplotlib.pyplot as plt
import numpy as np

# Regional distribution data on the left side
regions = ["East China", "South China", "Southwest China", "North China", "Central China", "Northwest China", "Northeast China", "Hong Kong, Macao and Taiwan"]
proportions_region = [24.2, 21.5, 17.6, 17.0, 9.8, 6.8, 3.0, 0.1]

# City - level distribution data on the right side
city_types = ["First - tier cities", "New first - tier cities", "Second - tier cities", "Third - tier cities", "Fourth - tier and other cities"]
proportions_city = [20.2, 27.4, 29.6, 14.8, 8.0]
colors_city = ["#FFD700", "#FF7F50", "#32CD32", "#8B4513", "#808000"]

fig = plt.figure(figsize=(16, 8))
# Left sub - plot (Regional distribution)
ax1 = fig.add_subplot(121)
x = np.arange(len(regions))
bars = ax1.bar(x, proportions_region, color=plt.cm.autumn(np.linspace(0, 1, len(regions))))
for i, proportion in enumerate(proportions_region):
    ax1.text(i, proportion + 1, f"{proportion}%", ha="center", va="bottom")
ax1.set_ylabel("Proportion (%)")
ax1.set_xlabel("Region")
ax1.set_xticks(x)
ax1.set_xticklabels(regions, rotation=45, ha="right")
ax1.set_title("Regional Distribution of Chinese Consumers in 2024")

# Right sub - plot (City - level distribution)
ax2 = fig.add_subplot(122)
wedges, texts, autotexts = ax2.pie(proportions_city, labels=city_types, colors=colors_city, autopct="%1.1f%%", 
                                  pctdistance=0.8, startangle=90)
for autotext in autotexts:
    autotext.set_color("white")
ax2.set_title("City - level Distribution of Chinese Consumers in 2024")

plt.tight_layout()
plt.show()