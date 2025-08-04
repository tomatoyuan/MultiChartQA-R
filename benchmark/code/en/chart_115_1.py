import matplotlib.pyplot as plt

# Data
labels = ["No, not at all", "Yes, digital transformation has been considered and implemented in the business strategy"]
sizes = [13.81, 86.19]
# Corresponding colors
colors = ['#FF7F27', '#4B53FF']

fig, ax = plt.subplots()
# Draw a donut chart, wedgeprops sets the width of the donut
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# Set the title
ax.set_title("Status of Chinese enterprises incorporating digital transformation into their business plans in 2025")

# Adjust the size and color of the annotation text (optional)
for text in texts + autotexts:
    text.set_fontsize(12)

plt.show()