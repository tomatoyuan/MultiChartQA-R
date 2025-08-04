import matplotlib.pyplot as plt

# Data
labels = ["Very optimistic", "Somewhat optimistic", "Neutral", "Somewhat pessimistic", "Very pessimistic"]
sizes = [20.84, 47.66, 21.22, 5.82, 4.46]
# Corresponding colors
colors = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63']

fig, ax = plt.subplots()
# Draw a donut chart, wedgeprops sets the width of the donut
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# Adjust the position and style of the annotation text (optional) to make the annotation clearer
for autotext in autotexts:
    autotext.set_horizontalalignment('center')
    autotext.set_verticalalignment('center')

ax.set_title('Chinese consumers\' views on the future development prospects of agricultural product retail in 2025')

plt.show()