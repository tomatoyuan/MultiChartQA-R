import matplotlib.pyplot as plt

# Data
labels = ["More than three times a day", "Once or twice a day", "Four to six times a week", "Two to three times a week", "Once a week or less"]
sizes = [8.91, 41.49, 39.23, 7.05, 3.32]
# Corresponding colors
colors = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63']

fig, ax = plt.subplots()
# Draw a donut chart, wedgeprops sets the width of the donut
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# Set the title
ax.set_title("Average frequency of Chinese audiobook users using audiobook APPs in 2025")

# Adjust the size and color of the annotation text (optional)
for text in texts + autotexts:
    text.set_fontsize(12)

plt.show()