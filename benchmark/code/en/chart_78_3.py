import matplotlib.pyplot as plt
import numpy as np

# Years
years = np.arange(2001, 2022)
# Number of job vacancies in Hong Kong (in ten thousands), the data can be approximately the same
vacancies = [1.7, 1.6, 2.1, 2.9, 3.7, 3.9, 4.8, 3.2, 3.5, 4.8, 5.5, 6.5, 7.2, 7.4, 7.1, 6.7, 7.4, 7.8, 5.4, 3.5, 6.1]

# Create a figure and a sub - plot
fig, ax = plt.subplots(figsize=(8, 6))

# Draw a line chart
line, = ax.plot(years, vacancies, marker='o', color="#39C6BA", label="Number of job vacancies in Hong Kong (in ten thousands)", linewidth=2)

# Add data annotations
for x, y in zip(years, vacancies):
    ax.annotate(f'{y}',
                xy=(x, y),
                xytext=(5, 5),  # Adjust the annotation position
                textcoords="offset points",
                ha='center', va='bottom',
                color="#39C6BA")

# Set x - axis ticks and labels
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
# Set y - axis label
ax.set_ylabel("Number of job vacancies in Hong Kong (in ten thousands)")
# Set the title
ax.set_title("Number of job vacancies in Hong Kong from 2001 to 2021", fontsize=14, fontweight="bold")

# Add a legend
ax.legend()

# Beautify the chart, hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()