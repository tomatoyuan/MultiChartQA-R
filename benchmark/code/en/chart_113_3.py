import matplotlib.pyplot as plt
import numpy as np

# Main types of anxiety during pregnancy
anxieties = ["Economic pressure anxiety", "Knowledge of pregnancy and childbirth anxiety", "Future planning anxiety", "Information asymmetry anxiety", 
             "Family relationship anxiety", "Personal growth/work anxiety", "Body image anxiety", "Health anxiety", "Product selection and shopping anxiety"]
# Corresponding proportions (%)
proportions = [31.57, 28.51, 27.90, 27.70, 26.68, 26.48, 25.87, 25.46, 23.42]

x = np.arange(len(anxieties))  # x-axis coordinates

fig, ax = plt.subplots(figsize=(12, 7))
# Draw a bar chart
bars = ax.bar(x, proportions, color='orange')

# Add numerical annotations
for i, proportion in enumerate(proportions):
    ax.text(i, proportion + 1, f'{proportion}', ha='center')

# Set x-axis ticks and labels, rotate labels
ax.set_xticks(x)
ax.set_xticklabels(anxieties, rotation=45, ha='right')
ax.set_ylabel('Proportion (%)')
ax.set_title('Main anxieties of Chinese expectant mothers in 2025')

plt.tight_layout()
plt.show()