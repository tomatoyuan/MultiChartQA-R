import matplotlib.pyplot as plt
import numpy as np

# Data
years = ["2018", "2019", "2020", "2021", "2022", "H1 2023"]
export = [6116, 7981, 10850, 13918, 15321, 8254]  # Export (billion yuan)
import_ = [4441, 4922, 5370, 5319, 5278, 2771]    # Import (billion yuan)
total = [10557, 12903, 16220, 19237, 20599, 11025] # Total import and export (billion yuan)

x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(12, 7))

# Draw a stacked bar chart (from bottom to top: total import and export, import, export, corresponding to the original figure order)
ax.bar(x, total, color='#8B4513', label='Total import and export (billion yuan)')
ax.bar(x, import_, bottom=total, color='#FF8C69', label='Import (billion yuan)')
ax.bar(x, export, bottom=np.array(total) + np.array(import_), color='#FFDAB9', label='Export (billion yuan)')

ax.set_ylabel('Amount (billion yuan)')
ax.set_xlabel('Year')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()
ax.set_title('China\'s cross - border e - commerce import and export scale from 2018 to 2023')

# Add numerical annotations (annotate the values of total import and export, import, and export respectively)
for i in range(len(years)):
    # Annotate the total import and export value
    ax.text(i, total[i] / 2, f'{total[i]}', ha='center', va='center', color='white', fontweight='bold')
    # Annotate the import value
    ax.text(i, total[i] + import_[i] / 2, f'{import_[i]}', ha='center', va='center', color='white', fontweight='bold')
    # Annotate the export value
    bottom_sum = total[i] + import_[i]
    ax.text(i, bottom_sum + export[i] / 2, f'{export[i]}', ha='center', va='center', color='white', fontweight='bold')

plt.tight_layout()
plt.show()