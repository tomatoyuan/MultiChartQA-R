import matplotlib.pyplot as plt

# Data
labels = ["Optimistic, decent drama quality", "Neutral", "Pessimistic, concerning drama quality"]
sizes = [49.63, 33.83, 16.54]
# Corresponding colors
colors = ['#FF7F27', '#4B53FF', '#32CD32']

fig, ax = plt.subplots()
# Draw a donut chart, wedgeprops sets the width of the donut
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# Set the title
ax.set_title("Views of Chinese TV drama viewers on the domestic drama industry in 2025")

# Adjust the size and color of the annotation text (optional)
for text in texts + autotexts:
    text.set_fontsize(12)

plt.show()