import matplotlib.pyplot as plt

# Usage frequency data
frequency_labels = ["Almost never used", "Occasionally used", "Used when needed", "Frequently used"]
frequency_sizes = [10.0, 45.5, 33.7, 10.8]
frequency_colors = ["#FF9933", "#FF5733", "#FFD700", "#FFC300"]

# Experience data
experience_labels = ["Improved shopping experience", "Had little impact on shopping experience", "Worsened shopping experience", "Not sure", "Other (please specify)"]
experience_sizes = [33.3, 37.4, 25.2, 3.9, 0.2]
experience_colors = ["#FFB6C1", "#FF8C69", "#FFDAB9", "#D8BFD8", "#C0C0C0"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Draw the usage frequency pie chart
wedges, texts, autotexts = ax1.pie(frequency_sizes, colors=frequency_colors, autopct='%1.1f%%', startangle=90)
ax1.set_title('Usage Frequency')
# Adjust the legend and place it on the right side of the pie chart
ax1.legend(wedges, frequency_labels, title="Usage Frequency Categories", loc="center left", bbox_to_anchor=(1, 0.5))
# Make the annotation text color clearer (distinguish between dark/light slices)
for autotext in autotexts:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

# Draw the experience pie chart
wedges2, texts2, autotexts2 = ax2.pie(experience_sizes, colors=experience_colors, autopct='%1.1f%%', startangle=90)
ax2.set_title('Experience')
ax2.legend(wedges2, experience_labels, title="Experience Categories", loc="center left", bbox_to_anchor=(1, 0.5))
for autotext in autotexts2:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

plt.suptitle('2024 Usage Frequency and Experience of Chinese Consumers with AI E-commerce Manual Intervention Features', fontsize=14)
plt.tight_layout()
plt.show()