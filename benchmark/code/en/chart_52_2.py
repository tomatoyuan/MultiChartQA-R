import matplotlib.pyplot as plt

# Data definition
labels = ["Pursue academic innovation", "Actively participate in scientific research projects and accumulate academic experience", "Be able to independently produce personal research results", "Not take the initiative to engage, only do it when the school requires"]
sizes = [33.8, 31.0, 27.3, 7.8]  # Roughly simulated data, can be adjusted according to actual situation
# Color settings, as close to the original image as possible
colors = ["greenyellow", "green", "limegreen", "lightgray"]

# Create a pie chart
fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors,
                                  textprops={'fontsize': 12}, wedgeprops={'linewidth': 1, 'edgecolor': 'white'})

# Beautify the annotation text color
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_weight('bold')

# Set the title
ax.set_title("College students' self - requirements in academic aspects", fontsize=16, fontweight='bold', y=1.05)

# Adjust the legend position (optional, can be adjusted if needed)
ax.legend(loc='upper right', bbox_to_anchor=(2.5, 0.8), fontsize=12)

# Adjust the layout
plt.tight_layout()

plt.show()