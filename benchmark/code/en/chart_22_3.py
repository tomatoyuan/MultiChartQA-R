import matplotlib.pyplot as plt
import numpy as np

# Sponsor data
sponsors = {
    "Ping An Insurance": 1.815,
    "Nike": 1,
    "Ford": 0.4,
    "JD.com": 0.35,
    "Carlsberg": 0.2,
    "DHL": 0.2,
    "Red Bull": 0.2
}

# Create a canvas
plt.figure(figsize=(12, 8))

# Sponsor sponsorship bar chart
sponsor_names = list(sponsors.keys())
sponsor_values = list(sponsors.values())
bars = plt.bar(sponsor_names, sponsor_values, color='#66b3ff')
plt.title('Sponsor Sponsorship Amount')
plt.xlabel('Sponsor')
plt.ylabel('Amount (Billion)')
plt.xticks(rotation=45)

# Add numerical labels
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.3f}',
             ha='center', va='bottom')

plt.tight_layout()
plt.show()