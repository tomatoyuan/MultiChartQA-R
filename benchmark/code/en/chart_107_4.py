import matplotlib.pyplot as plt
import numpy as np

# Understanding Channels
channels = ["Newspapers/books", "Informed by family/friends", "Outdoor media (subway, bus TV, airport ads, etc.)",
            "Technology exhibitions/conferences (telecom exhibitions, technology forums, etc.)",
            "Content sharing platforms (Xiaohongshu, Weibo, etc.)",
            "Industry research reports/analyses (research reports and market analyses from technology companies, etc.)",
            "Short - video platforms (Douyin, Kuaishou, etc.)",
            "TV/radio programs (news, technology channels, etc.)",
            "Mobile app push notifications (app stores, news apps, etc.)",
            "Social media platforms (WeChat, QQ, etc.)",
            "Promotion activities of telecom operators (营业厅, online and offline promotional activities, etc.)"]
# Corresponding proportions (%)
proportions = [12.67, 18.39, 23.13, 23.24, 23.79, 26.32, 27.64, 27.75, 28.52, 29.07, 34.69]

y = np.arange(len(channels))  # y - axis coordinates

fig, ax = plt.subplots(figsize=(12, 8))
# Draw a horizontal bar chart
bars = ax.barh(y, proportions, color='orange')

# Add numerical labels
for i, proportion in enumerate(proportions):
    ax.text(proportion, i, f'{proportion}', va='center', ha='left', fontsize=9)

# Set y - axis ticks and labels
ax.set_yticks(y)
ax.set_yticklabels(channels)
ax.set_xlabel('Proportion (%)')
ax.set_title('Channels for Chinese users to understand 5G in 2025')

plt.tight_layout()
plt.show()