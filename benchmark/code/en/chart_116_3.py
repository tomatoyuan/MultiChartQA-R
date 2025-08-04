import matplotlib.pyplot as plt

# Data
labels = ["Will give special consideration", "Will consider, but not the primary factor", "Will not consider"]
sizes = [47.01, 39.58, 13.41]
# Corresponding colors
colors = ['#FF7F27', '#4B53FF', '#32CD32']

fig, ax = plt.subplots()
# Draw a donut chart, wedgeprops sets the width of the donut
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# Adjust the position and style of the annotation text (optional)
for autotext in autotexts:
    autotext.set_horizontalalignment('center')
    autotext.set_verticalalignment('center')

ax.set_title('Consideration of well - known local agricultural products by Chinese consumers in 2025')

plt.show()