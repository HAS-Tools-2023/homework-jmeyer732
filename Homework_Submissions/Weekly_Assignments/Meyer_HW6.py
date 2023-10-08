# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 500)
# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week7.txt'
filepath = os.path.join('../../data', filename)
print(os.getcwd())
print(filepath)

# %%
# DON'T change this part -- this creates the lists you 
# should use for the rest of the assignment
# no need to worry about how this is being done now we will cover
# this in later sections. 

#Read the data into a pandas dataframe
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
df.columns = ['flow', 'year', 'month', 'day']
df.columns.values
df.index = pd.to_datetime(df.index)
# %%
print(df)
# %%
df.values

#%%
df.describe()

# %%
jan = df[(df.month == 1)]
print('JAN:')
jan.describe()

#%%
feb = (df[(df.month == 2)])
print('FEB:')
feb.describe()

#%%
march = (df[(df.month == 3)])
print('MARCH:')
march.describe()

#%%
april = df[(df.month == 4)]
print('APRIL:')
april.describe()

#%%
may = (df[(df.month == 5)])
print('MAY:')
may.describe()

#%%
june = (df[(df.month == 6)])
print('JUNE:')
june.describe()

#%%
july = df[(df.month == 7)]
print('JULY:')
july.describe()

#%%
aug = (df[(df.month == 8)])
print('AUG:')
aug.describe()

#%%
sept = (df[(df.month == 9)])
print('SEPT:')
sept.describe()

#%%
oct = df[(df.month == 10)]
print('OCT:')
oct.describe()

#%%
nov = (df[(df.month == 11)])
print('NOV:')
nov.describe()

#%%
dec = (df[(df.month == 12)])
print('DEC:')
dec.describe()

# %%
df.sort_values(by='flow', ascending = True)

# %%
df.sort_values(by='flow', ascending = False)

# %%
val1 = 115 + ((115 * 0.1) / 2)
val2 = 115 - ((115 * 0.1) / 2)
print(val1,val2)

#%%
historicaldates = (df[(df.flow >= 109.25) & (df.flow <= 120.75) & (df.month == 9)])
print("Historial Dates:")
historicaldates.sort_values(by='datetime', ascending = True)
print(historicaldates.shape)

# %%
recentflow = (df[(df.month >= 9) & (df.year == 2023)])
print(recentflow)
# %%
octflow1 = (df.flow[(df.month == 10) & (df.year >= 2010) & (df.day >= 1) & (df.day <= 7)])
print(octflow1)

#%%
octflow2 = (df.flow[(df.month == 10) & (df.year >= 2010) & (df.day >= 8) & (df.day <= 15)])
print(octflow2)

# %%
octflow3 = (df.flow[(df.month == 10) & (df.year >= 2010) & (df.day >= 16) & (df.day <= 22)])
print(octflow3)

#%%
octflow4 = (df.flow[(df.month == 10) & (df.year == 2023) & (df.day >= 1) & (df.day <= 7)])
print(octflow4)
# %%
print('oct1-7currentavg:', np.mean(octflow4))
print('oct1-7avg:', np.mean(octflow1))
print('oct8-15avg:', np.mean(octflow2))
print('oct16-22avg:', np.mean(octflow3))

#%%
fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, 1, figsize = (20,25))
ax1.set_ylim(30,200)
ax2.set_ylim(30,200)
ax3.set_ylim(30,200)
ax4.set_ylim(30,200)
ax5.set_ylim(30,200)

ax1.plot(octflow1, color = 'b')
ax1.grid(which = 'major', linestyle = '-', alpha = 0.5)

ax2.plot(octflow2, color = 'r')
ax2.grid(which = 'major', linestyle = '-', alpha = 0.5)

ax3.plot(octflow3, color = 'g')
ax3.grid(which = 'major', linestyle = '-', alpha = 0.5)

ax4.plot(octflow4, color = 'orange')
ax4.grid(which = 'major', linestyle = '-', alpha = 0.5)

ax5.plot(recentflow, color = 'y')
ax5.grid(which = 'major', linestyle = '-', alpha = 0.5)
# %%
