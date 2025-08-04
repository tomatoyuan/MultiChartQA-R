import matplotlib.pyplot as plt
import numpy as np

# Health indicators
indicators = ["HPV", "Tumor Markers", "Helicobacter pylori", "Clinical Examinations (Blood Pressure, BMI, Oral, ENT)", 
              "Functional Examinations (Radiology, Ultrasound, Electrocardiogram)", "Biochemical and Laboratory Tests (Blood Routine, Urine Routine, Biochemistry, Liver Function, Kidney Function, Thyroid Function, Blood Glucose)"]
# Corresponding proportions (%)
proportions = [23.77, 30.67, 35.57, 44.83, 46.28, 61.89]

y = np.arange(len(indicators))  # y-axis coordinates

fig, ax = plt.subplots(figsize=(10, 6))
# Draw a horizontal bar chart
bars = ax.barh(y, proportions, color='orange')

# Add numerical annotations
for i, proportion in enumerate(proportions):
    ax.text(proportion, i, f'{proportion}', va='center', ha='left', fontsize=9)

# Set y-axis ticks and labels
ax.set_yticks(y)
ax.set_yticklabels(indicators)
ax.set_xlabel('Proportion (%)')
ax.set_title('Health Indicators Most Concerned by Chinese Health Check-up Consumers in 2025')

plt.tight_layout()
plt.show()