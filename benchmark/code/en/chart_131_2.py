import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
# Population aged 65 and above (in ten thousand people)
elderly_pop = [12777, 13262, 13902, 14524, 15037, 15961, 16724, 17767, 19064, 20056, 20978, 21676]

x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(10, 6))

# Draw a bar chart
bars = ax.bar(x, elderly_pop, color='green')

# Add numerical labels
for i, pop in enumerate(elderly_pop):
    ax.text(i, pop + 200, f'{pop}', ha='center', va='bottom')

# Set the axes
ax.set_ylabel('Population aged 65 and above (in ten thousand people)')
ax.set_xlabel('Year')
ax.set_xticks(x)
ax.set_xticklabels(years)

ax.set_title('Population aged 65 and above in China from 2012 to 2023')

plt.tight_layout()
plt.show()