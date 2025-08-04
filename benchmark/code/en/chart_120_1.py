import matplotlib.pyplot as plt
import numpy as np

# Left: Data on the ways Chinese investors obtain investment and financial information
left_labels = [
    "Professional investment professionals such as\n wealth managers from banks/securities institutions", 
    "Social relationships such as family and friends", 
    "Investment apps", 
    "Self - media, social media, etc.", 
    "Official documents, announcements, data, etc.", 
    "Others (financial websites, news apps, databases, etc.)"
]
left_proportions = [56.01, 38.37, 36.24, 34.11, 33.91, 0.97]

# Right: Data on the types of investment apps used by Chinese investors
right_labels = [
    "Third - party payment platforms such as Alipay and WeChat", 
    "Self - owned apps of securities companies", 
    "Third - party Internet financial platforms such as Flush"
]
right_proportions = [75.94, 68.45, 51.34]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Draw a horizontal bar chart of the ways to obtain information on the left
y1 = np.arange(len(left_labels))
ax1.barh(y1, left_proportions, color='orange')
ax1.set_yticks(y1)
ax1.set_yticklabels(left_labels)
ax1.set_xlabel('Proportion (%)')
ax1.set_title('Ways for Chinese investors to obtain investment and financial information')
# Add numerical annotations on the left
for i, proportion in enumerate(left_proportions):
    ax1.text(proportion + 1, i, f'{proportion}%', va='center')

# Draw a horizontal bar chart of the types of apps used on the right
y2 = np.arange(len(right_labels))
ax2.barh(y2, right_proportions, color='orange')
ax2.set_yticks(y2)
ax2.set_yticklabels(right_labels)
ax2.set_xlabel('Proportion (%)')
ax2.set_title('Types of investment apps used by Chinese investors')
# Add numerical annotations on the right
for i, proportion in enumerate(right_proportions):
    ax2.text(proportion + 1, i, f'{proportion}%', va='center')

plt.tight_layout()
plt.show()