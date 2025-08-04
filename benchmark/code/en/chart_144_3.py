import matplotlib.pyplot as plt
import numpy as np

# Data preparation
labels = ["Open-air movies/concerts", "Networking salons", "Language corners", "Dances"]
percentages = [76.4, 67.7, 40.3, 27.3]
# Use text to simulate icons (you can customize more appropriate symbols)
icons = ["Open-air movies/concerts", "Networking salons", "Language corners", "Dances"]

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 100)
ax.set_ylim(0, len(labels) * 2)
ax.set_axis_off()

for i, (label, perc, icon) in enumerate(zip(labels, percentages, icons)):
    # Draw the icon (in text form)
    # ax.text(10, i * 2 + 1, icon, fontsize=20, va="center")
    # Draw the label
    ax.text(20, i * 2 + 1, label, fontsize=12, va="center")
    # Draw the percentage
    ax.text(90, i * 2 + 1, f"{perc}%", fontsize=12, va="center", ha="right")
    # Draw the progress bar
    ax.barh(i * 2 + 1, perc, left=20, height=1.5, color="#FF9933", alpha=0.8)

ax.set_title("Expectations of the main consumer groups in Chinese university towns for the addition of value - added services in future university town business districts in 2023", fontsize=14, y=1.05)
plt.tight_layout()
plt.show()