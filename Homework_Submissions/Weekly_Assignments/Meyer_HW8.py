# %%
import os
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
pd.set_option('display.max_rows', 500)

# %%
filename = 'streamflow_week9.txt'
filepath = os.path.join('../../data', filename)
print(os.getcwd())
print(filepath)

#%%
#Read the data into a pandas dataframe
df = pd.read_table(filepath, sep = '\t', skiprows=31, usecols = [2, 3],
        names = ['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )
print(df)

#%%
df = df.dropna()
df[["year", "month", "day"]] =df['datetime'].str.split("-", expand=True)
df['year'] = df['year'].astype(int)
df['month'] = df['month'].astype(int)
df['day'] = df['day'].astype(int)

# %%
df = df.set_index('datetime')

# %%
print(df)

# %%
clim_flow_week1 = pd.DataFrame(df.flow[(df.month == 10) & (df.year >= 1991) & (df.year <= 2020) 
                         & (df.day >= 22) & (df.day <= 28)])
clim_flow_week1.describe()

# %%
df1 = pd.DataFrame(df.flow[((df.month == 10) & (df.year >= 1991) & (df.year <= 2020) 
                         & (df.day >= 29) & (df.day <= 31))])
df2 = pd.DataFrame(df.flow[((df.month == 11) & (df.year >= 1991) & (df.year <= 2020) 
                         & (df.day >= 1) & (df.day <= 4))])
#%%
clim_flow_week2 =pd.DataFrame(pd.concat([df1, df2], axis = 0, ignore_index = False))
clim_flow_week2.describe()


# %%
print("1 week forecast:", (clim_flow_week1.mean() * 0.6))
print("2 week forecast:", (clim_flow_week2.mean() * 0.6))

# %%
flow1 = clim_flow_week1['flow']
flow2 = clim_flow_week2['flow']
# %%
fig, (ax1, ax2) = plt.subplots(2, 1, figsize = (10,7), sharex = True)
plt.suptitle("Climatological Streamflow Values of week 1 and week 2 outlooks:", fontsize = 14)

ax1.plot(flow1, color = 'green', alpha = 1, linewidth = 2, label = 'Oct 22 to Oct 28 Streamflow')
ax2.plot(flow2, color = 'blue', alpha = 1, linewidth = 2, label = 'Oct 29 to Nov 4 Streamflow')
ax1.plot(flow1.mean(), marker = '*', color = 'green', label = 'Week 1 Mean')
ax2.plot(flow2.mean(), marker = '*', color = 'blue', label = 'Week 2 Mean')
ax1.axhline(flow1.mean(), alpha = 0.25, color = 'green')
ax2.axhline(flow2.mean(), alpha = 0.25, color = 'blue')
ax1.axhline(94.99, alpha = 0.5, color = 'orange', label = 'My week 1 forecast')
ax2.axhline(111.83, alpha = 0.5, color = 'orange', label = 'My week 2 forecast')

ax1.set_ylabel('Streamflow (cf/s)', fontsize = 10)
ax1.set_ylim(0, 1500)
ax1.legend(fontsize = 8)
ax2.set_ylabel('Streamflow (cf/s)', fontsize = 10)
ax2.set_ylim(0, 1500)
ax2.legend(fontsize = 8)

ax1.set_xlabel('Date', fontsize = 7)
plt.tight_layout()

# %%
