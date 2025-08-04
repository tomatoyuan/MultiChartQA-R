import matplotlib.pyplot as plt

# Data
labels = ["Smart Home", "High - quality Materials", "Green and Environment - friendly", "Personalized Customization"]
sizes = [29.09, 22.85, 25.35, 22.71]
# Corresponding colors
colors = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0']

fig, ax = plt.subplots()
# Draw a donut chart, wedgeprops sets the width of the donut
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# Adjust the position and style of the annotation text (optional) to make the annotation clearer
for autotext in autotexts:
    autotext.set_horizontalalignment('center')
    autotext.set_verticalalignment('center')

ax.set_title('2025 Chinese consumers\' views on the future development trends of the home furnishing industry')

plt.show()