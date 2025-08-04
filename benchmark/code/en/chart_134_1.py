import matplotlib.pyplot as plt
import numpy as np

# Left: Data on the necessity of sun protection
labels_left = ["Think sun protection is necessary", "Think sun protection is not necessary"]
proportions_left = [92.5, 7.5]

# Right: Data on the important factors of sun protection
labels_right = ["Prevent sun - tanning", "Prevent skin sunburn", "Prevent photo - aging", "Prevent pigmentation", "Prevent skin cancer"]
proportions_right = [52.5, 83.2, 57.2, 57.3, 31.5]

fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(14, 6))

# Draw the left comparison chart
x_left = np.arange(len(labels_left))
bars = ax_left.bar(x_left, proportions_left, color=['#FFA07A', '#FFD700'])
for i, prop in enumerate(proportions_left):
    ax_left.text(i, prop + 1, f'{prop}%', ha='center', va='bottom')
ax_left.set_ylabel('Proportion (%)')
ax_left.set_xticks(x_left)
ax_left.set_xticklabels(labels_left)
ax_left.set_title('Chinese consumers\' views on sun protection')
ax_left.yaxis.set_ticks([])
for spine in ['top', 'right', 'left']:
    ax_left.spines[spine].set_visible(False)

# Draw the right radar chart
num_vars = len(labels_right)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
proportions_right += proportions_right[:1]
angles += angles[:1]
ax_right.fill(angles, proportions_right, color='#FFA07A', alpha=0.25)
ax_right.plot(angles, proportions_right, color='#FFA07A', linewidth=2)
for i, (angle, prop) in enumerate(zip(angles[:-1], proportions_right[:-1])):
    ax_right.text(angle, prop + 1, f'{prop}%', ha='center', va='bottom')
ax_right.set_yticklabels([])
ax_right.set_xticks(angles[:-1])
ax_right.set_xticklabels(labels_right, rotation=45, ha='right')
ax_right.set_title('Important factors of sun protection recognized by Chinese consumers')

plt.tight_layout()
plt.show()