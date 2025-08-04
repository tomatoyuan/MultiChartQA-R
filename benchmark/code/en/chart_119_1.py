import matplotlib.pyplot as plt
import numpy as np

# Data preparation
labels = ["Very Satisfied", "Fairly Satisfied", "Average", "Not Very Satisfied"]
sizes = [27.2, 58.3, 14.0, 0.5]
# Corresponding colors, can be adjusted according to the original image
colors = ["#4BA6FF", "#FF9933", "#FFCC33", "#FF6666"]

fig, ax = plt.subplots(figsize=(6, 6))
# Draw a pie chart, set the starting angle, whether to separate, etc.
patches, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%",
                                    startangle=90, wedgeprops={"width": 0.4})

# Adjust the style of the annotation text
for text in texts:
    text.set_fontsize(12)
for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_color("black")

ax.set_title("Survey on Chinese Public's Satisfaction with Their Own Health", fontsize=14, y=1.05)
plt.show()