import matplotlib.pyplot as plt

# Data
labels = ["Less than 3 times a month", "1 - 2 times a week", "3 - 4 times a week", "More than 5 times a week"]
sizes = [9.92, 49.60, 29.22, 11.26]
# Corresponding colors
colors = ["#FF7F27", "#4B53FF", "#32CD32", "#9467BD"]

fig, ax = plt.subplots()
# Draw a donut chart, wedgeprops sets the width of the donut
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# Set the title
ax.set_title("Frequency of Chinese consumers drinking packaged drinking water in 2025")

# Adjust the size and color of the annotation text (optional)
for text in texts + autotexts:
    text.set_fontsize(12)

plt.show()