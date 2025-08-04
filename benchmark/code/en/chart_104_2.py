import matplotlib.pyplot as plt
import numpy as np

# Course names
courses = ["Keyboard Instruments (Piano, Organ, Accordion, Electronic Keyboard, etc.)", 
           "String Instruments (Violin, Guitar, Erhu, Guzheng, Pipa, etc.)", 
           "Woodwind Instruments (Flute, Suona, Oboe, Saxophone, etc.)", 
           "Percussion Instruments (Xylophone, Snare Drum, Bass Drum, Clappers, Yangqin, etc.)", 
           "Brass Instruments (Trumpet, Cornet, Trombone, French Horn, Tuba, etc.)", 
           "Vocal Music"]
# Corresponding proportions
proportions = [40.08, 35.22, 31.31, 29.82, 27.94, 17.95]

y = np.arange(len(courses))  # y-axis coordinates

fig, ax = plt.subplots(figsize=(10, 6))
# Draw a horizontal bar chart
bars = ax.barh(y, proportions, color='orange')

# Add numerical labels
for i, proportion in enumerate(proportions):
    ax.text(proportion, i, f'{proportion}', va='center', ha='left', fontsize=9)

# Set y-axis ticks and labels
ax.set_yticks(y)
ax.set_yticklabels(courses)
ax.set_xlabel('Proportion (%)')
ax.set_title('Main courses enrolled by Chinese users in 2025')

plt.show()