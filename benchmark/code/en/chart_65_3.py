import matplotlib.pyplot as plt

# Data
labels = ["Less than 1000 yuan", "1001 - 5000 yuan", "5001 - 10000 yuan", "10000 - 30000 yuan", "Above 30000 yuan", "No income"]
sizes = [33.3, 17.0, 9.4, 3.5, 3.5, 33.3]
# Color settings, try to be close to the original image colors
colors = ["#A4C639", "#8DB328", "#7EA11E", "#668718", "#506D12", "#DCDCDC"]

fig, ax = plt.subplots()
# Draw a pie chart, set autopct to display percentages, pctdistance to adjust the percentage position, and textprops to adjust the text style
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", 
                                  startangle=90, pctdistance=0.8, textprops={"color": "black"})

# Adjust the size of the annotation text
for autotext in autotexts:
    autotext.set_size(10)
for text in texts:
    text.set_size(10)

# Set the title
ax.set_title("Income distribution of core content creators in China from content creation")

# Keep the pie chart circular
ax.axis("equal")

plt.show()