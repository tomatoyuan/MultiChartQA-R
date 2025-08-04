import matplotlib.pyplot as plt

# Original data (using the number of asterisks directly)
provinces = ["Guangdong", "Jiangsu", "Shandong", "Zhejiang", "Henan", "Taiwan", "Sichuan", "Hebei", "Hubei", "Hunan"]
stars = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]  # Corresponding number of asterisks for each province

# Reverse the data order so that the province with the highest star rating is at the top
provinces_reversed = provinces[::-1]
stars_reversed = stars[::-1]

# Create a canvas
plt.figure(figsize=(12, 6))

# Draw a horizontal bar chart (the province with the highest star rating is at the top)
plt.barh(provinces_reversed, stars_reversed, color='skyblue')

# Add asterisk labels
for i, (province, star_count) in enumerate(zip(provinces_reversed, stars_reversed)):
    plt.text(star_count + 0.2, i, '★' * star_count, va='center', fontsize=12)

# Set the chart title and axis labels
plt.title('GDP Ranking of Chinese Provinces and Cities in 2015')
plt.xlabel('Number of Stars')
plt.ylabel('Province')

# Set the x-axis range
plt.xlim(0, max(stars_reversed) + 2)  # Leave enough space to display the asterisks

# Beautify the chart
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()  # Ensure a compact layout
plt.show()