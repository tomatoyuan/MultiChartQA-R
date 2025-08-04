# Data
labels = ["Greatly benefited", "Gained something", "Little feeling"]
sizes = [35.76, 53.31, 10.93]
# Corresponding colors
colors = ["#FF7F27", "#4B53FF", "#32CD32"]

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
# Draw a donut chart, wedgeprops sets the width of the donut
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# Set the title
ax.set_title("2025 Chinese users' perception of music learning in cultivating aesthetics and thinking")

# Adjust the size and color of the annotation text (optional)
for text in texts + autotexts:
    text.set_fontsize(12)

plt.show()