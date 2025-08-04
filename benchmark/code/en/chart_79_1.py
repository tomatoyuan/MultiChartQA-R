import matplotlib.pyplot as plt

# Categories
labels = ["Increased Attention and Trust", "Others"]
# Proportion of each category (%), approximate data is acceptable
sizes = [65.0, 35.0]
# Colors of each part of the pie chart, try to be close to the original image
colors = ["#A4C639", "#64B5F6"]

# Create a canvas and a sub - plot
fig, ax = plt.subplots(figsize=(6, 6))

# Draw a pie chart
wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, autopct='%1.1f%%', 
    startangle=90, colors=colors, 
    textprops={'color': 'black'}
)

# Beautify the annotation text (adjust the size, etc.)
for text in texts + autotexts:
    text.set_fontsize(12)

# Add the bottom explanatory text
ax.text(0.5, -0.2, "● 65% of consumers indicated that their attention and trust in traditional Chinese medicine increased after the pandemic.", 
        ha='center', va='bottom', fontsize=10, color='green')

# Set the title
ax.set_title("Attention and Trust in TCM for COVID - 19 Diagnosis and Treatment in 2021", fontsize=14, fontweight="bold", y=1.05)

plt.tight_layout()  # Automatically adjust the layout
plt.show()