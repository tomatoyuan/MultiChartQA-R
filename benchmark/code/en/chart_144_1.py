import matplotlib.pyplot as plt
import numpy as np

# --------------------- Data for the chart of the number of college entrance examination applicants and growth rate ---------------------
years_gaokao = ["2016", "2017", "2018", "2019", "2020", "2021", "2022"]
enroll_gaokao = [940, 940, 975, 1031, 1071, 1078, 1193]
growth_gaokao = [np.nan, 0.0, 3.7, 5.7, 3.9, 0.7, 10.7]  # No growth rate in 2016 (as the starting year)

# --------------------- Data for the chart of the scale of higher education institutions and growth rate ---------------------
years_school = ["2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
scale_school = [2879, 2914, 2914, 2956, 3005, 3012, 3013, 3072]
growth_school = [np.nan, 1.2, 0.0, 1.4, 1.7, 0.2, 0.0, 0.0]  # No growth rate in 2016 (as the starting year)

# Create a canvas with a 1x2 layout
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# --------------------- Draw the chart of the number of college entrance examination applicants and growth rate (left chart) ---------------------
ax1.bar(years_gaokao, enroll_gaokao, color='orange', label='Number of applicants (in ten thousands)')
ax1.set_ylabel('Number of applicants (in ten thousands)')
ax1.set_xlabel('Year')
ax1.set_title('Number of Chinese college entrance examination applicants and growth rate from 2016 - 2022')
ax1.legend(loc='upper left')

# Draw the growth rate line chart (dual - axis)
ax1_2 = ax1.twinx()
ax1_2.plot(years_gaokao, growth_gaokao, marker='o', color='gold', label='Growth rate (%)', linewidth=2)
ax1_2.set_ylabel('Growth rate (%)')
ax1_2.legend(loc='center right')

# Add numerical labels for the number of college entrance examination applicants
for i, num in enumerate(enroll_gaokao):
    ax1.text(i, num + 10, f'{num}', ha='center', va='bottom')

# Add numerical labels for the college entrance examination growth rate (no label for 2016, starting from 2017)
for i, rate in enumerate(growth_gaokao[1:], start=1):
    ax1_2.text(i, rate + 0.1, f'{rate}%', ha='center', va='bottom')

# --------------------- Draw the chart of the scale of higher education institutions and growth rate (right chart) ---------------------
ax2.bar(years_school, scale_school, color='orange', label='Scale of higher education institutions (number)')
ax2.set_ylabel('Scale of higher education institutions (number)')
ax2.set_xlabel('Year')
ax2.set_title('Scale of Chinese higher education institutions and growth rate from 2016 - 2023')
ax2.legend(loc='center left')

# Draw the growth rate line chart (dual - axis)
ax2_2 = ax2.twinx()
ax2_2.plot(years_school, growth_school, marker='o', color='gold', label='Growth rate (%)', linewidth=2)
ax2_2.set_ylabel('Growth rate (%)')
ax2_2.legend(loc='center right')

# Add numerical labels for the scale of higher education institutions
for i, num in enumerate(scale_school):
    ax2.text(i, num + 10, f'{num}', ha='center', va='bottom')

# Add numerical labels for the growth rate of higher education institutions (no label for 2016, starting from 2017)
for i, rate in enumerate(growth_school[1:], start=1):
    ax2_2.text(i, rate + 0.1, f'{rate}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()