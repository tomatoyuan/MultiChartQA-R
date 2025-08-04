import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Data
labels = ["Anti - hair loss and \n"
          "new hair growth",
          "Oil - removal and scalp relaxation",
          "Hydration and moisturizing",
          "Deep cleansing",
          "Bright hair color",
          "Improve split ends",
          "Strengthen and prevent \n hair breakage",
          "Improve hair follicles",
          "Anti - dandruff \n and anti - itching"]
columns = ["Post - 05", "Post - 00", "Post - 95", "Post - 90", "Post - 85", "Pre - 80"]
data = [
    [96, 120, 105, 114, 95, 49],
    [101, 130, 82, 100, 96, 121],
    [160, 88, 119, 90, 58, 123],
    [104, 95, 72, 96, 120, 124],
    [121, 93, 109, 67, 122, 87],
    [78, 43, 117, 113, 147, 116],
    [45, 74, 132, 106, 85, 100],
    [95, 78, 107, 132, 60, 85],
    [85, 93, 105, 96, 115, 98]
]

# Create a DataFrame
df = pd.DataFrame(data, index=labels, columns=columns)

# Set values below 100 to NaN
masked_df = df.copy()
masked_df[df < 100] = np.nan

# Select color palette
cmap = sns.light_palette("deeppink", as_cmap=True)

# Draw a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(masked_df, annot=df, fmt="d", cmap=cmap, linewidths=0.5, linecolor='grey', cbar=True,
            mask=df < 100, annot_kws={"size": 10}, square=False)

# Set title and style
plt.title("Research on scalp health needs of women of different generations (TGI>100)", fontsize=14, pad=20)
plt.xticks(rotation=0)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()