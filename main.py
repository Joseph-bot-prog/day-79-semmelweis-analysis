import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Set display format to show two decimal places
pd.options.display.float_format = '{:,.2f}'.format

# Create locators for ticks on the time axis
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')

# Register date converters to avoid warning messages
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Fetch data on annual clinic deaths
annual_deaths = pd.read_csv('annual_deaths_by_clinic.csv')

# Retrieve monthly mortality records
monthly_deaths = pd.read_csv('monthly_deaths.csv', parse_dates=['date'])

# Generate a comprehensive dual-axis plot for profound insights
fig, primary_axis = plt.subplots(figsize=(14, 8), dpi=200)
plt.title('Dynamic Exploration: Monthly Births and Deaths', fontsize=18)

# Chart births on the primary y-axis with a vibrant skyblue trajectory
primary_axis.plot(monthly_deaths.date, monthly_deaths.births, color='skyblue', linewidth=3, label='Births')
primary_axis.set_xlabel('Date', fontsize=14)
primary_axis.set_ylabel('Births Count', color='skyblue', fontsize=14)
primary_axis.tick_params(axis='y', labelcolor='skyblue')
primary_axis.grid(color='grey', linestyle='--', alpha=0.5)

# Establish a secondary y-axis for deaths with a crimson dashed line
secondary_axis = primary_axis.twinx()
secondary_axis.plot(monthly_deaths.date, monthly_deaths.deaths, color='crimson', linewidth=2, linestyle='--', label='Deaths')
secondary_axis.set_ylabel('Deaths Count', color='crimson', fontsize=14)
secondary_axis.tick_params(axis='y', labelcolor='crimson')

# Format x-axis dates with major ticks for years and minor ticks for months
primary_axis.xaxis.set_major_locator(years)
primary_axis.xaxis.set_major_formatter(years_fmt)
primary_axis.xaxis.set_minor_locator(months)

# Implement gridlines for enhanced readability
primary_axis.grid(True, linestyle='--', alpha=0.5)

# Integrate a legend for both y-axes
primary_legend_lines, primary_legend_labels = primary_axis.get_legend_handles_labels()
secondary_legend_lines, secondary_legend_labels = secondary_axis.get_legend_handles_labels()
secondary_axis.legend(primary_legend_lines + secondary_legend_lines,
                      primary_legend_labels + secondary_legend_labels,
                      loc='upper left', fontsize=12)

# Annotate the graph with an arrow indicating a noteworthy event
primary_axis.annotate('Landmark Event: Discovery of Blood Groups', xy=(mdates.datestr2num('1905-01-01'), 100),
                      xytext=(mdates.datestr2num('1900-01-01'), 300),
                      arrowprops=dict(facecolor='green', shrink=0.05),
                      fontsize=10, color='green')

# Embed a dynamic line annotation at the last date for increased emphasis
primary_axis.axvline(x=monthly_deaths.date.iloc[-1], color='green', linestyle='dashed', linewidth=2)

# Showcase the masterpiece
plt.show()



# NOTE - do not copy my code try making yours by (josephidaagu@gmail.com)
