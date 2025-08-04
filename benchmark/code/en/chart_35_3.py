import matplotlib.pyplot as plt

# Data
labels = ['Cardiovascular and cerebrovascular diseases', 'Cancer', 'Chronic respiratory diseases', 'Others']
sizes = [53, 27, 10, 10]  # The proportion of the "Others" part to make the total 100. The data can be approximately close.
colors = ['#008060', '#80e0a0', '#c0ffe0', '#d9d9d9']  # The colors should be as close as possible to the original chart.

# Draw a pie chart
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
ax.set_title('Cause of death composition of chronic diseases')

# Adjust the legend position (simulate the annotation style of the original chart, and can be fine - tuned according to actual needs)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right', bbox_to_anchor=(-0.1, 1.1))

plt.show()