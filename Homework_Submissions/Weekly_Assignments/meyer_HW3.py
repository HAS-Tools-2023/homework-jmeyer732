#%%
# Import the necessary libraries
import os
import numpy as np
import pandas as pd
import matplotlib as plt

#%%
# The data is stored one level higher
filename = 'streamflow_week3.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)

# %%
# Read the data into a pandas dataframe - a 3d dataframe
data = pd.read_table(filepath, sep = '\t', skiprows = 31, names = ['agency_cd', 'site_no', 'datetime', 'flow', 'code'])

#%% 
# Drop nan values from the pandas dataframe
data = data.dropna()

#%%
# Expand the dates to year, month, day
data[["year", "month", "day"]] = data["datetime"].str.split("-", expand = True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)



#%%
# Make lists of the data
flow = data.flow.values.tolist()
date = data.datetime.values.tolist()
year = data.year.values.tolist()
month = data.month.values.tolist()
day = data.day.values.tolist()

#%%
# Get rid of the pandas dataframe since we wont use it this week for the homework
del(data)

#%%
# Basic calcs
print('flow min:', min(flow))
print('flow max:', max(flow))
print('flow mean:', np.mean(flow))
print('flow standard deviation:', np.std(flow))

# %%
# Make an empty list to store the index values
ilist1 = []

# %%
# Loop through the length of the list to add your criteria of values
for i in range(len(flow)):
    if flow[i] > 90 and month[i] == 9 and year[i] == 2023:
        ilist1.append(i)

# Make an empty list to store the index values for the partial dataset
# Loop through the length of the list from 1981-2000 to add your criteria of values
ilist2 = []
for i in range(len(flow)):
    if flow[i] > 90 and month[i] == 9 and year[i] < 2001:
        ilist2.append(i)

# Make an empty list to store the index values for partial dataset
# Loop through the length of the list from 2010 to current and add criteria to list
ilist3 = []
for i in range(len(flow)):
    if flow[i] > 90 and month[i] == 9 and year[i] > 2009:
        ilist3.append(i)

# %%
# Make an empty list to store the index values for the full dataset
# Loop through the length of the list from 1981 to current and add criteria
ilist4 = []
for i in range(len(flow)):
    if flow[i] > 90 and month[i] == 9:
        ilist4.append(i)

#%%
#Same for first half and second half of september for the full dataset
firsthalfsept = []
for i in range(len(flow)):
    if month[i] == 9 and 0 <= day[i] <= 15:
        firsthalfsept.append(i)

secondhalfsept = []
for i in range(len(flow)):
    if month[i] == 9 and 16 <= day[i] <= 30:
        secondhalfsept.append(i)
# %%
# Check to see if the criteria was met by printing the list
print('Sept 2023:', len(ilist1))
print('Sept 1981-2010:', len(ilist2))
print('Sept 2010-current:', len(ilist3))
print('Sept 1981-current:', len(ilist4))

#%%
print('first half of sept avg:', np.mean(firsthalfsept))
print('first half of sept deviation:', np.std(firsthalfsept))
print('first half of sept min:', np.min(firsthalfsept))
print('first half of sept max:', np.max(firsthalfsept))

#%%
print('second half of sept avg:', np.mean(secondhalfsept))
print('second half of sept deviation:', np.std(secondhalfsept))
print('second half of sept min:', np.min(secondhalfsept))
print('second half of sept max:', np.max(secondhalfsept))

# %%
# Subset the data for the elements identified within the list
subset = [flow[j] for j in ilist]

# %%
# Write a for loop to create the same list
forlooplist = [i for i in range(len(flow)) if flow[i] > 80]
print(len(forlooplist))

# %%
