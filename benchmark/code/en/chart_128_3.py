import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
# Number of non - VR games/applications
non_vr = [3935, 5844, 8028, 7522, 8924, 10827, 11620, 13765]
# Number of VR games/applications
vr = [735, 1105, 872, 612, 822, 562, 945, 689]

x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(12, 7))

# Plot the non - VR part (orange)
ax.bar(x, non_vr, color='orange', label='Non - VR Games/Applications')
# Plot the VR part (yellow, stacked on top of non - VR)
ax.bar(x, vr, bottom=non_vr, color='gold', label='VR Games/Applications')

# Add labels for non - VR quantity
for i, nv in enumerate(non_vr):
    ax.text(i, nv / 2, f'{nv}', ha='center', va='center', color='white')

# Add labels for VR quantity
for i, v in enumerate(vr):
    ax.text(i, non_vr[i] + v / 2, f'{v}', ha='center', va='center', color='black')

ax.set_ylabel('Quantity (units)')
ax.set_xlabel('Year')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()
ax.set_title('Number of Newly Added Games/Applications on the Steam Platform Yearly from 2016 - 2023')

plt.tight_layout()
plt.show()