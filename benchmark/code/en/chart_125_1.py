import matplotlib.pyplot as plt

# Data
labels = ["Two years", "Three years", "Four years and above", "Within one year"]
sizes = [49.0, 33.7, 9.3, 8.0]
colors = ["#8B4513", "#FFA07A", "#32CD32", "#FF8C00"]

fig, ax = plt.subplots(figsize=(6, 6))
# Draw a pie chart, autopct displays the percentage, startangle sets the starting angle
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)

# Adjust the annotation text color to white for better clarity
for autotext in autotexts:
    autotext.set_color("white")

ax.set_title("Frequency of Chinese consumers changing mobile phones")
plt.show()