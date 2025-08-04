import matplotlib.pyplot as plt

# Data preparation
labels = ["100 - 1000 yuan", "1001 - 2000 yuan", "2001 - 4000 yuan", "4001 - 8000 yuan", "8001 - 10000 yuan", "Over 10000 yuan"]
sizes = [20.1, 26.3, 32.7, 14.2, 5.3, 1.4]
colors = ["blue", "orange", "gray", "yellow", "cyan", "green"]

fig, ax = plt.subplots(figsize=(8, 6))

# Draw a pie chart
wedges, texts, autotexts = ax.pie(sizes, colors=colors, autopct='%1.1f%%', startangle=140)

ax.set_title('Proportion of weight - loss expenditure of Chinese netizens in 2023')

# Adjust the legend
ax.legend(wedges, labels, title="Expenditure range", loc="center left", bbox_to_anchor=(1, 0.5))

# Adjust the color of the annotation text (make the annotation text of dark - colored slices white and that of light - colored slices black for better clarity)
for autotext in autotexts:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

plt.tight_layout()
plt.show()