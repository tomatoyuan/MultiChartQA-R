import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
# Number of births (in ten thousand people)
births = [1635, 1640, 1687, 1655, 1786, 1723, 1523, 1465, 1200, 1062, 956, 902]

x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(10, 6))

# Draw a bar chart
bars = ax.bar(x, births, color='gold')

# Add numerical annotations
for i, birth in enumerate(births):
    ax.text(i, birth + 20, f'{birth}', ha='center', va='bottom')

# Set the axes
ax.set_ylabel('Number of births (in ten thousand people)')
ax.set_xlabel('Year')
ax.set_xticks(x)
ax.set_xticklabels(years)

ax.set_title('Number of births in China from 2012 to 2023')

plt.tight_layout()
plt.show()