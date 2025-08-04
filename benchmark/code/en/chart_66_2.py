import matplotlib.pyplot as plt
import numpy as np

# Set the font to display English properly
plt.rcParams["font.sans-serif"] = ["Arial"]
plt.rcParams["axes.unicode_minus"] = False

# Define age groups and categories in English
age_groups = ["Post - 95s", "Post - 90s", "Post - 85s", "Pre - 85s"]
categories = ["Need regular daily supplementation", "Supplement only when pets have relevant symptoms or are in special periods"]
data = [[46, 52, 56, 54], [33, 35, 28, 30]]
colors = [["#C0C0C0", "#A4C639", "#8DB328", "#7EA11E"], 
          ["#A4C639", "#8DB328", "#C0C0C0", "#D3D3D3"]]

# Generate x - coordinates for the bars
x = np.arange(len(age_groups))  
width = 0.35  

# Create a figure and an axis
fig, ax = plt.subplots(figsize=(8, 5))

# Plot the bars for each category
for i in range(len(categories)):
    rects = ax.bar(x + i * width, data[i], width, color=colors[i], edgecolor="white", label=categories[i])
    # Add data labels to the bars
    for rect, label in zip(rects, data[i]):
        height = rect.get_height()
        ax.annotate(f'{label}%',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  
                    textcoords="offset points",
                    ha='center', va='bottom')

# Set the x - tick positions and labels
ax.set_xticks(x + width / 2)
ax.set_xticklabels(age_groups)
# Set the y - axis limit
ax.set_ylim(0, 60)
# Set the title of the chart
ax.set_title("Acceptance of pet health products among different age groups", fontsize=14, fontweight="bold")

# Adjust the legend position, for example, place it on the left outside the chart
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))  

# Display the chart
plt.show()