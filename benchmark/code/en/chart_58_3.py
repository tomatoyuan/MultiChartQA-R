import matplotlib.pyplot as plt
import numpy as np

# Data
weeks = ["Week 1, April", "Week 2, April", "Week 3, April", "Week 4, April", "Week 5, April"]
data_2024 = [3500.2, 3726.2, 3616.5, 3628.3, 3598.8]  # Simulated data, can be replaced with actual values
data_2025 = [4039.3, 4230.8, 4409.0, 4232.3, 3966.2]  # Simulated data, can be replaced with actual values

# Create a canvas
fig, ax = plt.subplots(figsize=(8, 5))

# Draw the lines
ax.plot(weeks, data_2025, color="#a5d65d", marker="o", label="Year 2025", linewidth=2)
ax.plot(weeks, data_2024, color="#4bb7e6", marker="o", label="Year 2024", linewidth=2)

# Add data labels
for x, y in zip(weeks, data_2025):
    ax.text(x, y + 20, f'{y}', ha='center', va='bottom', fontsize=9)
for x, y in zip(weeks, data_2024):
    ax.text(x, y + 20, f'{y}', ha='center', va='bottom', fontsize=9)

# Beautify the settings
ax.set_title("UserTracker - Comparison of trends of cultural performance APPs from Tomb - Sweeping Festival to May Day in 2024 and 2025\nUnit: Number of weekly active user devices (in ten thousand units)", fontsize=12, fontweight='bold')
ax.legend()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()