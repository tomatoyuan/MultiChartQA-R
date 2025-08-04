import matplotlib.pyplot as plt
import numpy as np

# Data
years = ["2019", "2020", "2021", "2022"]
export_growth = [30.5, 39.2, 28.3, 10.1]  # Year-on-year growth rate of export volume (%)
import_growth = [10.8, 9.1, -0.9, 0.8]    # Year-on-year growth rate of import volume (%)
total_growth = [22.2, 25.7, 18.6, 7.1]    # Year-on-year growth rate of import and export volume (%)

x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(10, 6))

# Draw the line chart
ax.plot(x, total_growth, marker='o', color='blue', label='Year-on-year growth rate of import and export volume (%)', linewidth=2)
ax.plot(x, import_growth, marker='o', color='orange', label='Year-on-year growth rate of import volume (%)', linewidth=2)
ax.plot(x, export_growth, marker='o', color='green', label='Year-on-year growth rate of export volume (%)', linewidth=2)

ax.set_ylabel('Year-on-year growth rate (%)')
ax.set_xlabel('Year')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()
ax.set_title('Year-on-year growth rate of China\'s cross - border e - commerce import and export volume from 2019 to 2022')

# Add numerical annotations
for i in range(len(years)):
    # Annotate the year-on-year value of import and export volume
    ax.text(i, total_growth[i] + 1, f'{total_growth[i]}', ha='center', va='bottom', color='blue')
    # Annotate the year-on-year value of import volume
    ax.text(i, import_growth[i] + 1, f'{import_growth[i]}', ha='center', va='bottom', color='orange')
    # Annotate the year-on-year value of export volume
    ax.text(i, export_growth[i] + 1, f'{export_growth[i]}', ha='center', va='bottom', color='green')

plt.tight_layout()
plt.show()