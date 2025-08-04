import matplotlib.pyplot as plt

# Enterprise types and their proportion data
labels = [
    "Manufacturing", "Information Transmission, Computer Services and Software", "Mining", "Culture, Sports and Entertainment",
    "Agriculture, Forestry, Animal Husbandry and Fishery", "Wholesale and Retail Trade", "Education", "Construction", "Real Estate",
    "Production and Supply of Electricity, Gas and Water", "Transportation, Warehousing and Postal Services", "Finance",
    "Health, Social Security and Social Welfare", "Others"
]
sizes = [14.74, 14.32, 2.14, 8.55, 4.27, 8.55, 3.85, 5.34, 7.26, 9.40, 8.97, 4.49, 7.91, 0.21]
# Corresponding colors (try to match the original image, can be fine - tuned according to actual situation)
colors = [
    '#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63',
    '#1E90FF', '#FFD700', '#00FA9A', '#FF69B4', '#00BFFF',
    '#FFA07A', '#9370DB', '#7FFF00', '#BA55D3'
]

fig, ax = plt.subplots(figsize=(12, 8))
# Draw a donut chart, wedgeprops sets the width of the donut
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# Adjust the size and color of the annotation text (optional) to make the annotation position more reasonable
for text in texts:
    text.set_fontsize(10)
for autotext in autotexts:
    autotext.set_fontsize(9)
    autotext.set_color('black')  # Make the values clearer on the colored blocks

ax.set_title('Types of Digital - Transforming Enterprises in China in 2025')

plt.tight_layout()
plt.show()