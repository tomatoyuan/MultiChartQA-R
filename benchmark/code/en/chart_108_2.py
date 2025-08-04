import matplotlib.pyplot as plt

# Data
labels = ["Every day", "4 - 5 times a week", "1 - 3 times a week", "Irregular, fragmented reading"]
sizes = [19.96, 51.54, 21.93, 6.57]
# Corresponding colors
colors = ["#FF7F27", "#4B53FF", "#32CD32", "#9400D3"]

fig, ax = plt.subplots()
# Draw a donut chart, wedgeprops sets the width of the donut
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# Set the title
ax.set_title("Frequency of Chinese financial news users reading financial media information in 2025")

# Adjust the size and color of the annotation text (optional)
for text in texts + autotexts:
    text.set_fontsize(12)

plt.show()