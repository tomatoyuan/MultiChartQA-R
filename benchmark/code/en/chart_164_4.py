import matplotlib.pyplot as plt

# Data
labels = [
    "Function + Fashion + Comfort\n are equally important\nMulti - purpose needs are put forward",
    "Functionality is the main focus, \nwith fashion and comfort as supplements",
    "Only require function\n and sports performance",
    "Only focus on product information \nsuch as category and brand",
    "Only focus on fashion"
]
sizes = [48, 26, 15, 5, 5]
colors = ['#FFB84C', '#FBC374', '#FFDCA8', '#FFE9C1', '#FFF3DC']

# Draw a pie chart
plt.figure(figsize=(8, 6))
wedges, texts, autotexts = plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    startangle=140,
    autopct='%1.0f%%',
    textprops={'fontsize': 10}
)

# Title and data source description
plt.title('Distribution of consumers\' demands for luxury outdoor clothing (%)', fontsize=14)
plt.figtext(0.5, 0.02, "Data source: CBNData survey in May 2024; N = 1000", ha="center", fontsize=10)

plt.tight_layout()
plt.show()