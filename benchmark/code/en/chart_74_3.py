import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2017", "2018", "2019", "2020", "2021", "2022e", "2023e", "2024e"]
# Scale of industries related to influencer economy (in billions of yuan), the data only needs to be roughly consistent
industry_scale = [22506, 28857, 35868, 41571, 50295, 57185, 64431, 71169]
# Growth rate (%), the data only needs to be roughly consistent
growth_rate = [39.4, 28.2, 24.3, 15.9, 20.2, 15.7, 13.1, 10.8]

# Create a canvas and subplots with a dual y-axis
fig, ax1 = plt.subplots(figsize=(10, 6))
ax2 = ax1.twinx()

ax1.set_ylim(0, 150000)
ax2.set_ylim(-50, 60)

# Draw a bar chart of the scale of industries related to influencer economy
x = np.arange(len(years))
bar_width = 0.6
bars = ax1.bar(x, industry_scale, width=bar_width, color="#A4C639", label="Scale of industries related to influencer economy (in billions of yuan)")

# Draw a line chart of the growth rate
line, = ax2.plot(x, growth_rate, marker='o', color="#64B5F6", label="Growth rate (%)", linewidth=2)

# Add data labels for the industry scale
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),  # Adjust the annotation position
                 textcoords="offset points",
                 ha='center', va='bottom')

# Add data labels for the growth rate
for x_val, y_val in zip(x, growth_rate):
    ax2.annotate(f'{y_val}%',
                 xy=(x_val, y_val),
                 xytext=(0, 5),  # Adjust the annotation position
                 textcoords='offset points',
                 ha='center', va='bottom',
                 color="#64B5F6")

# Set x-axis ticks and labels
ax1.set_xticks(x)
ax1.set_xticklabels(years)
# Set y-axis labels
ax1.set_ylabel("Scale of industries related to influencer economy (in billions of yuan)", color="#A4C639")
ax2.set_ylabel("Growth rate (%)", color="#64B5F6")
# Set the title
ax1.set_title("Market scale of industries related to China's new influencer economy from 2017 to 2024", fontsize=14, fontweight="bold")

# Combine legends
handles, labels = ax1.get_legend_handles_labels()
handles.append(line)
labels.append(line.get_label())
ax1.legend(handles, labels, loc='upper left')

# Beautify the chart by hiding the top and right borders (for ax1 and ax2)
for spine in ["top", "right"]:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()