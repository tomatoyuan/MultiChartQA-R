import matplotlib.pyplot as plt

# Data
labels = [
    "The support of skin - care \n"
    "technology can better enhance\n"
    " the efficacy of ingredients",  # 这里“发挥成分功效”英文可改为 "enhance the efficacy of ingredients"
    "Don't care about the technology in products\nStill focus on ingredients\n",
    "Never paid attention to \nthe concept of \n'tech - based skin care'"
]
sizes = [83, 12, 5]
colors = ['#FFB6C1', '#FFCCE5', '#FFE6F0']  # Gradient of pink tones
explode = (0.05, 0, 0)  # Highlight the first slice

# Plotting
fig, ax = plt.subplots(figsize=(7, 5))
wedges, texts, autotexts = ax.pie(
    sizes,
    explode=explode,
    labels=labels,
    colors=colors,
    autopct='%1.0f%%',
    startangle=140,
    textprops={'fontsize': 12},
    wedgeprops={'linewidth': 1, 'edgecolor': 'white'}
)

ax.axis('equal')  # Ensure the pie chart is circular
plt.title("Survey on contemporary female consumers' views on \nthe concept of 'tech - based skin care'", fontsize=14, weight='bold',pad=30)
plt.tight_layout()
plt.show()