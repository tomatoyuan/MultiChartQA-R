import matplotlib.pyplot as plt

# Data
labels = [
    "E-commerce", "Education", "Transportation", "Media", "Finance", "Film and Television", 
    "Real Estate Services", "Games", "Health, Social Security and Social Welfare", "Culture and Tourism", "Others"
]
sizes = [16.49, 11.97, 8.24, 8.24, 10.51, 7.31, 7.85, 6.78, 12.91, 8.64, 1.06]
# Corresponding colors (try to match the original image and fine - tune according to the actual situation)
colors = [
    '#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63',
    '#1E90FF', '#FFD700', '#00FA9A', '#FF69B4', '#00BFFF', '#BA55D3'
]

fig, ax = plt.subplots(figsize=(12, 8))
# Draw a donut chart, wedgeprops sets the width of the donut
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# Adjust the size and color of the annotation text (optional) to make the annotation clearer
for text in texts:
    text.set_fontsize(10)
for autotext in autotexts:
    autotext.set_fontsize(9)
    autotext.set_color('black')  # Make the values clearer on the colored blocks

ax.set_title('Industry Distribution of Chinese Enterprises Using AI Digital Humans in 2025')

plt.tight_layout()
plt.show()