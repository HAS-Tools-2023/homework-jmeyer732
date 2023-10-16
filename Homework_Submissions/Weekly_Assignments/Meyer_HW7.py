# %%
import os
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
pd.set_option('display.max_rows', 500)

# %%
filename = 'streamflow_week8.txt'
filepath = os.path.join('../../data', filename)
print(os.getcwd())
print(filepath)

# %%
df = pd.read_table(filepath, sep = '\t', skiprows=31, usecols = [2, 3],
        names = ['datetime', 'flow']
        )
print(df)

#%%
df = df.dropna()
df[["year", "month", "day"]] =df['datetime'].str.split("-", expand=True)
df['year'] = df['year'].astype(int)
df['month'] = df['month'].astype(int)
df['day'] = df['day'].astype(int)

#%%
print(df.shape)

# %%
df = df.set_index('datetime')

# %%
print(df)

# %%
#df.columns = ['flow', 'year', 'month', 'day']
#df.columns.values
#df.index = pd.to_datetime(df.index)

# %%
print(df)

# %%
#df.values

#%%
# this is creating a new dataframe with a subset of the conditional data
# this one only subsets the flow and index into the new dataframe 'lastweek'
lastweekaverage = (df.flow[(df.month >= 10) & (df.year == 2023) & (df.day >= 8) & (df.day <= 14)]).mean()
print(lastweekaverage)

#%%
average2weekflow = (df.flow[(df.month >= 10) & (df.year <= 2022) & (df.year >= 1990) & (df.day >= 8) & (df.day <= 14)]).mean()
print(average2weekflow)
timeslower1 = (df.flow[(df.month >= 10) & (df.year <= 2022) & (df.year >= 2018) & (df.day >= 8) & (df.day <= 14)]).mean()
timeslower2 = (df.flow[(df.month >= 10) & (df.year <= 2017) & (df.year >= 2013) & (df.day >= 8) & (df.day <= 14)]).mean()
timeslower3 = (df.flow[(df.month >= 10) & (df.year <= 2012) & (df.year >= 2008) & (df.day >= 8) & (df.day <= 14)]).mean()
timeslower4 = (df.flow[(df.month >= 10) & (df.year <= 2007) & (df.year >= 2003) & (df.day >= 8) & (df.day <= 14)]).mean()
print(timeslower1)
print(timeslower2)
print(timeslower3)
print(timeslower4)
percent = (lastweekaverage / timeslower2)
average2weekflow * percent

#%%
# this is also creating a new dataframe with a subset of data, however,
# the new dataframe 'histflow' includes all data that meet the conditions.
# name = (df[(conditional statements)]) yeilds all data into new dataframe
# name = (df.flow[(conditional statements)]) yeilds only the flow data and 
#       its associated index.
histflow = (df[(df.month == 10) & (df.year >= 1990) & (df.day >= 15) 
               & (df.day <= 21)])
print(histflow.mean())
print(histflow)

#%%
histflow.sort_values(by='flow', ascending = True)

#%%
print(histflow.flow.max())
print(histflow.flow.min())
histflow.describe()

#%%
# historical flow average 71.3cfs for oct 8-14, 2020
histflow2020week2 = (df[(df.month == 10) & (df.year == 2020) & (df.day >= 8) & (df.day <= 14)])
print('histflow2020week2:', histflow2020week2)
print('histflow2020week2 mean:', histflow2020week2.mean())

#%%
# historical flow average 93.31cfs for oct 8-14, 2019
histflow2019week2 = (df[(df.month == 10) & (df.year == 2019) & (df.day >= 8) & (df.day <= 14)])
print('histflow2019week2:', histflow2019week2)
print('histflow2019week2 mean:', histflow2019week2.mean())

#%%
# historical flow average 76.214cfs for oct 15-21, 2020
histflow2020 = (df[(df.month == 10) & (df.year == 2020) & (df.day >= 15) & (df.day <= 21)])
print('histflow2020:', histflow2020)
print('histflow2020 mean:', histflow2020.mean())

#%%
# historical flow average 78.628cfs for oct 15-21, 2019
histflow2019 = (df[(df.month == 10) & (df.year == 2019) & (df.day >= 15) & (df.day <= 21)])
print('histflow2019:', histflow2019)
print('histflow2019 mean:', histflow2019.mean())

#%%
# historical flow average 93.23cfs for oct 22-28, 2020
histflow2020week4 = (df[(df.month == 10) & (df.year == 2020) & (df.day >= 22) & (df.day <= 28)])
print('histflow2020week4:', histflow2020week4)
print('histflow2020week4 mean:', histflow2020week4.mean())

#%%
# historical flow average 89.2cfs for oct 22-28, 2019
histflow2019week4 = (df[(df.month == 10) & (df.year == 2019) & (df.day >= 22) & (df.day <= 28)])
print('histflow2019week4:', histflow2019week4)
print('histflow2019week4 mean:', histflow2019week4.mean())

#%%
# historical flow average cfs for oct 29-31, 2019
histflow2019week5 = (df[(df.month == 10) & (df.year == 2019) & (df.day >= 29) & (df.day <= 31)])
print('histflow2019week4:', histflow2019week5)
print('histflow2019week4 mean:', histflow2019week5.mean())

#%%
# historical flow average 89.2cfs for nov1-4, 2019
histflow2019week6 = (df[(df.month == 11) & (df.year == 2019) & (df.day >= 1) & (df.day <= 4)])
print('histflow2019week:', histflow2019week6)
print('histflow2019week4 mean:', histflow2019week6.mean())

#%%
# historical flow average cfs for oct 29-31, 2020
histflow2019week8 = (df[(df.month == 10) & (df.year == 2020) & (df.day >= 29) & (df.day <= 31)])
print('histflow2019week4:', histflow2019week8)
print('histflow2019week4 mean:', histflow2019week8.mean())

#%%
# historical flow average 89.2cfs for nov1-4, 2020
histflow2019week7 = (df[(df.month == 11) & (df.year == 2020) & (df.day >= 1) & (df.day <= 4)])
print('histflow2019week:', histflow2019week7)
print('histflow2019week4 mean:', histflow2019week7.mean())

#%%
print('2019 avg:', ((123.25 * 4) + (104.33 * 3)) / 7)
print('2020 avg:', ((117 * 3) + (121.5 * 4)) / 7)

#%%
# forecast value for 1 week out: 91cfs
# forecast value for 2 weeks out: 117 cfs
#%%
histflow2 = (df[(df.month == 10) & (df.year == 2023) & (df.day >= 1) & (df.day<=14)])
flow2 = histflow2['flow']
histflow3 = (df[(df.month == 10) & (df.year == 2022) & (df.day >= 1) & (df.day<=14)])
flow3 = histflow3['flow']
histflow4 = (df[(df.month == 10) & (df.year == 2021) & (df.day >= 1) & (df.day<=14)])
flow4 = histflow4['flow']
#%%
ax = plt.figure(figsize = (20,20))
ax = histflow.plot.scatter(figsize = (10,8), x='year', y='flow', c='day', colormap='viridis_r', marker='*', s = 50, grid = 'black')
ax.set_title("Historical October Thirdweek Streamflow", color = 'black', fontsize = 14)
ax.set_ylim(50, 300)
ax.set_xlabel('Year')
ax.set_ylabel('Flow (cfs)')
ax.set_xticklabels(ax.get_xticks(), rotation=45, fontsize = 8)
plt.savefig('scatterplot1.jpg')



# %%
fig, (ax1) = plt.subplots(1, 1, figsize = (8,8))
start = '2023-10-01'
end = '2023-10-14'
ax1.plot(df.flow[start:end], color = 'b')
ax1.set_title("October Streamflow 2023", color = 'black', fontsize = 14)
ax1.set_ylim(50, 100)
ax1.set_xlabel('Day')
ax1.set_ylabel('Flow (cfs)')
ax1.grid(which = 'major', linestyle = '-', alpha = 0.5)
ax1.set_xticklabels(ax1.get_xticks(), rotation=45, fontsize = 8)
plt.savefig('linegraph1.jpg')

# %%
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize = (10,10), sharex = True)
plt.suptitle("October 1 - 14 streamflow in 2021, 2022, and 2023:", fontsize = 20)
start = '2021-10-01'
end = '2023-10-14'


## SUBPLOT 1
ax1.plot(flow4[start:end], color = 'blue', alpha = 1, linewidth = 4, label = '2023 Streamflow')
# Specify the minor and major gridlines
#ax1.grid(which = 'minor', linestyle = '-', alpha = 0.25)
ax1.grid(which = 'major', linestyle = '-', alpha = 0.5)
# Specify the y label axis, and the y limit for the first subplot
ax1.set_ylabel('Streamflow (cf/s)', fontsize = 11)
ax1.set_ylim(0, 300)
ax1.legend(fontsize = 8)

## SUBPLOT 2
ax2.plot(flow3[start:end], color = 'green', alpha = 1, linewidth = 4, label = '2022 Streamflow')
# Specify the minor and major gridlines
#ax2.grid(which = 'minor', linestyle = '-', alpha = 0.25)
ax2.grid(which = 'major', linestyle = '-', alpha = 0.5)
# Specify the y label axis, and the y limit for the first subplot
ax2.set_ylabel('Streamflow (cf/s)', fontsize = 11)
ax2.set_ylim(0, 300)
ax2.legend(fontsize = 8)

## SUBPLOT 3
ax3.plot(flow2[start:end], color = 'blue', alpha = 1, linewidth = 4, label = '2021 Streamflow')
# Specify the minor and major gridlines
#ax3.grid(which = 'minor', linestyle = '-', alpha = 0.25)
ax3.grid(which = 'major', linestyle = '-', alpha = 0.5)
# Specify the y label axis, and the y limit for the first subplot
ax3.set_ylabel('Streamflow (cf/s)', fontsize = 11)
ax3.set_ylim(0, 300)
ax3.legend(fontsize = 8)

#majorformattor = mdates.DateFormatter('%d-%b-%Y')
#ax3.get_xaxis().set_major_formatter(majorformattor)
fig.autofmt_xdate(rotation = 45, ha = 'center')
ax3.set_xlabel('Date')
plt.tight_layout()
plt.savefig('subplots.jpg', dpi = 300)
plt.show()
plt.close()
# %%
# %%
fig, (ax1) = plt.subplots(1, 1, figsize = (10,7), sharex = True)
plt.title("streamflow values of 2023 and 2022:", fontsize = 20)
start = '2021-10-01'
end = '2023-10-14'


## SUBPLOT 1
ax1.plot(flow2[start:end], color = 'blue', alpha = .5, linewidth = 3, label = 'Oct 2023 streamflow')
ax1.plot(flow3[start:end], color = 'green', alpha = 0.5, linewidth = 3, label = 'oct 2022 streamflow')
ax1.plot(flow4[start:end], color = 'orange', alpha = 0.5, linewidth = 3, label = 'oct 2022 streamflow')
# Specify the minor and major gridlines
#ax1.grid(which = 'minor', linestyle = '-', alpha = 0.25)
ax1.grid(which = 'major', linestyle = '-', alpha = 0.5)
# Specify the y label axis, and the y limit for the first subplot
ax1.set_ylabel('Streamflow (cf/s)', fontsize = 16)
ax1.set_ylim(0, 1200)
ax1.legend(fontsize = 8)
fig.autofmt_xdate(rotation = 45, ha = 'center')
ax1.set_xlabel('Date', fontsize = 16)
plt.tight_layout()
plt.savefig('multipleseries.jpg')

# %%
# Make a histogram of data
# Use the linspace  funciton to create a set  of evenly spaced bins
mybins = np.linspace(0, 100, num=100)
# another example using the max flow to set the upper limit for the bins
#mybins = np.linspace(0, np.max(flow_data[:,3]), num=15) 
#Plotting the histogram
plt.hist(df.flow, bins = mybins, width = .5, color = 'red')
plt.title('Streamflow')
plt.xlabel('Flow (cf/s)')
plt.ylabel('Number of Occurrances')
plt.savefig('histogram.jpg')
# %%
