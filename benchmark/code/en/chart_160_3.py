import matplotlib.pyplot as plt

# Data
categories = ["Life Records", "Appearance", "Food", "Humor", "Games", "Music", "Movies", "Beauty", "Fashion", "Emotions"]
values = [100, 90, 70, 80, 80, 70, 65, 60, 60, 50]  # Example values

highlight_indices = [0, 7, 8]  # Highlight "Life Records", "Beauty", "Fashion"

# Plotting
fig, ax = plt.subplots(figsize=(10, 4))
bars = ax.bar(categories, values, color="#4da6ff")

# Mark the key categories with a dashed box
for idx in highlight_indices:
    bar = bars[idx]
    height = bar.get_height()
    ax.add_patch(plt.Rectangle(
        (bar.get_x() - 0.1, 0), bar.get_width() + 0.2, height + 5,
        fill=False, edgecolor="#b084e9", linewidth=2, linestyle='--'
    ))

# Add numerical annotations
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 2, f"{height}",
            ha='center', va='bottom', fontsize=10)

# Beautify the graph
ax.set_title("Top 10 Proportion Distribution of Content Categories of Mid - tier TikTok Influencers", fontsize=12)
ax.set_ylabel("Quantity (Schematic)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()