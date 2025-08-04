import matplotlib.pyplot as plt
import numpy as np

# --------------------- Age distribution data ---------------------
age_labels = ["Under 18", "19 - 25", "26 - 30", "31 - 40", "41 - 50", "Over 51"]
age_sizes = [0.0, 13.0, 36.8, 39.9, 8.2, 2.1]
age_colors = ["#FADBD8", "#F9E79F", "#F5B041", "#F1948A", "#B03A2E", "#8B4513"]

# --------------------- Residential area distribution data ---------------------
region_labels = ["First-tier cities", "New first-tier cities", "Second-tier cities", "Third-tier cities", "Fourth-tier and other cities"]
region_sizes = [27.3, 27.6, 26.9, 12.6, 5.6]
region_colors = ["#FADBD8", "#F9E79F", "#F5B041", "#F1948A", "#8B4513"]

# --------------------- Gender distribution data ---------------------
gender_labels = ["Male", "Female"]
gender_sizes = [36.8, 63.2]
gender_colors = ["#F9E79F", "#F1948A"]

# Create a canvas with a 1x3 layout
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

# --------------------- Draw the age distribution pie chart (left chart) ---------------------
wedges1, texts1, autotexts1 = ax1.pie(age_sizes, colors=age_colors, autopct='%1.1f%%', startangle=90)
ax1.set_title('Age distribution of Chinese cultural \nand creative product consumers in 2023')
ax1.legend(wedges1, age_labels, title="Age range", loc="center left", bbox_to_anchor=(1, 0.5))
# Adjust the color of the annotation text
for autotext in autotexts1:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

# --------------------- Draw the residential area distribution pie chart (middle chart) ---------------------
wedges2, texts2, autotexts2 = ax2.pie(region_sizes, colors=region_colors, autopct='%1.1f%%', startangle=90)
ax2.set_title('Residential area distribution of Chinese cultural \nand creative product consumers in 2023')
ax2.legend(wedges2, region_labels, title="Region type", loc="center left", bbox_to_anchor=(1, 0.5))
# Adjust the color of the annotation text
for autotext in autotexts2:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

# --------------------- Draw the gender distribution pie chart (right chart) ---------------------
wedges3, texts3, autotexts3 = ax3.pie(gender_sizes, colors=gender_colors, autopct='%1.1f%%', startangle=90)
ax3.set_title('Gender distribution of Chinese cultural \nand creative product consumers in 2023')
ax3.legend(wedges3, gender_labels, title="Gender", loc="center left", bbox_to_anchor=(1, 0.5))
# Adjust the color of the annotation text
for autotext in autotexts3:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

plt.tight_layout()
plt.show()