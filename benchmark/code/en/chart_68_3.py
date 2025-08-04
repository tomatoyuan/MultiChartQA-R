import matplotlib.pyplot as plt
import numpy as np

# Time nodes
years = ["2018.12", "2019.6", "2020.3", "2020.6", "2020.12"]
# Number of online audio - visual users (in hundreds of millions)
user_scale = [7.32, 7.8, 8.57, 9.01, 9.44]
# Internet user usage rate (%)
usage_rate = [88.3, 91.3, 94.8, 95.8, 95.4]

# Create a canvas and sub - plots with a dual y - axis
fig, ax1 = plt.subplots(figsize=(8, 5))
ax2 = ax1.twinx()

ax1.set_ylim(0, 20)  # Y - axis for the number of users (in hundreds of millions)
ax2.set_ylim(75, 100)  # Y - axis for the usage rate (%)

# Draw a bar chart of the number of online audio - visual users
x = np.arange(len(years))
bar_width = 0.6
bars = ax1.bar(x, user_scale, width=bar_width, color="#A4C639", label="Number of online audio - visual users (in hundreds of millions)")

# Draw a line chart of the internet user usage rate
line, = ax2.plot(x, usage_rate, marker='o', color="#64B5F6", label="Internet user usage rate (%)", linewidth=2)

# Add data labels for the number of users
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),  # Adjust the label position
                 textcoords="offset points",
                 ha='center', va='bottom')

# Add data labels for the usage rate
for x_val, y_val in zip(x, usage_rate):
    ax2.annotate(f'{y_val}%',
                 xy=(x_val, y_val),
                 xytext=(0, 5),  # Adjust the label position
                 textcoords="offset points",
                 ha='center', va='bottom',
                 color="#64B5F6")

# Set the x - axis ticks and labels
ax1.set_xticks(x)
ax1.set_xticklabels(years)
# Set the y - axis labels
ax1.set_ylabel("Number of online audio - visual users (in hundreds of millions)", color="#A4C639", fontsize=10)
ax2.set_ylabel("Internet user usage rate (%)", color="#64B5F6")
# Set the title
ax1.set_title("Online audio - visual user scale and usage in China from 2018 to 2020", fontsize=14, fontweight="bold")

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