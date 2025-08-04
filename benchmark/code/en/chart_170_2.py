import matplotlib.pyplot as plt
import pandas as pd

# Data preparation
labels = ['Somatization', 'Obsessive-compulsive\n symptoms', 'Interpersonal sensitivity', 'Depression', 'Anxiety',
          'Hostility', 'Phobia', 'Paranoia', 'Psychoticism', 'Others\n (such as sleep problems)']
obvious = [8.1, 19.2, 17.9, 24.6, 16.7, 14.3, 8.9, 13.2, 11.2, 14.5]
mild = [29.9, 41.9, 39.6, 40.3, 37.5, 33.1, 27.3, 34.6, 36.6, 38.6]
healthy = [62.0, 38.9, 42.5, 35.1, 45.8, 52.6, 63.7, 52.2, 52.1, 46.9]

df = pd.DataFrame({
    'Obvious': obvious,
    'Mild': mild,
    'Healthy': healthy
}, index=labels)

# Plotting
fig, ax = plt.subplots(figsize=(10, 8))
df[::-1].plot(kind='barh', stacked=True, color=['#FFCB2F', '#7D65AD', '#99DEEB'], ax=ax)

# Add labels
for i, (obs, mid, hea) in enumerate(zip(obvious[::-1], mild[::-1], healthy[::-1])):
    ax.text(obs / 2, i, f'{obs}%', va='center', ha='center', color='black', fontsize=8)
    ax.text(obs + mid / 2, i, f'{mid}%', va='center', ha='center', color='white', fontsize=8)
    ax.text(obs + mid + hea / 2, i, f'{hea}%', va='center', ha='center', color='black', fontsize=8)

# Style adjustment
ax.set_title('Distribution of self - assessment results of \nusers\' mental health in psychological assessment', fontsize=14)
ax.set_xlabel('Percentage')
ax.set_xlim(0, 100)
ax.legend(loc='upper center', ncol=3, bbox_to_anchor=(0.5, -0.08))
plt.tight_layout()
plt.show()