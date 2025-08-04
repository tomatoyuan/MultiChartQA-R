import matplotlib.pyplot as plt

# Data
labels = [
    "Efficiency improvement over 50%", "Efficiency improvement between 40 - 50%", "Efficiency improvement between 30 - 40%",
    "Efficiency improvement between 20 - 30%", "Efficiency improvement between 10 - 20%", "Efficiency improvement below 10%"
]
sizes = [12.53, 27.52, 31.61, 18.53, 6.54, 3.27]
# Corresponding colors (try to match the original image and fine - tune according to the actual situation)
colors = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63', '#1E90FF']

fig, ax = plt.subplots(figsize=(10, 7))
# Draw a donut chart, wedgeprops sets the width of the donut
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# Adjust the size and color of the annotation text (optional) to make the annotation clearer
for text in texts:
    text.set_fontsize(10)
for autotext in autotexts:
    autotext.set_fontsize(9)
    autotext.set_color('black')  # Make the values clearer on the colored blocks

ax.set_title('The improvement of work efficiency or quality of Chinese enterprises by AI digital humans in 2025')

plt.tight_layout()
plt.show()