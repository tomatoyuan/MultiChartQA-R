import matplotlib.pyplot as plt
import numpy as np

# AI Digital Human Function Requirements
functions = [
    "Emotion Recognition", "Multi-round Dialogue", "Coding Ability", "Cross - language Communication (Translation, etc.)", "Text Rewriting", 
    "Logic and Reasoning", "Body Movement Recognition", "Text Classification", "Autonomous Learning and Evolution", "Generation and Creation", 
    "Facial Recognition", "Human - Machine Interaction", "Natural Language Understanding", "Multimodal Ability (Text, Image, Voice, Video Processing)"
]
# Corresponding Proportions (%)
proportions = [17.69, 17.95, 18.88, 19.02, 19.41, 
               19.68, 20.61, 21.41, 21.54, 22.34, 
               22.34, 24.87, 25.66, 32.98]

y = np.arange(len(functions))  # y-axis coordinates

fig, ax = plt.subplots(figsize=(12, 8))
# Draw a horizontal bar chart
bars = ax.barh(y, proportions, color='orange')

# Add numerical annotations on the right side of the bars
for i, proportion in enumerate(proportions):
    ax.text(proportion, i, f'{proportion}', va='center', ha='left', fontsize=9)

# Set y-axis ticks and labels
ax.set_yticks(y)
ax.set_yticklabels(functions)
ax.set_xlabel('Proportion (%)')
ax.set_title('Chinese Enterprises\' Functional Requirements for AI Digital Humans in 2025')

plt.tight_layout()
plt.show()