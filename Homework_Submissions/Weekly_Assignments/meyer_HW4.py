# Starter code for Homework 4

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week4.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)

# %%
# DON'T change this part -- this creates the lists you 
# should use for the rest of the assignment
# no need to worry about how this is being done now we will cover
# this in later sections. 

#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=31,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

#%%
data = data.dropna()

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# Make a numpy array of this data
# [[1981,...]
#  [month,..]
#  [day, ...]
#  [flowdata]]
flow_data = data[['year', 'month','day', 'flow']].to_numpy()
print(flow_data)

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

# %%
# Starter Code
# Count the number of values with flow > 600 and month ==7
flow_count = np.sum((flow_data[:,3] > 600) & (flow_data[:,1]==7))
flow_countsepttotal = np.sum((flow_data[:,3] > 0) & (flow_data[:,1]==9))
flow_count2 = np.sum((flow_data[:, 3] > 50) & (flow_data[:,1]==9))
flow_count3 = np.sum((flow_data[:, 3] < 50) & (flow_data[:,1]==9))

flow_countsepttotalbefore2001 = np.sum((flow_data[:,3] > 0) & (flow_data[:,0] <= 2001) & (flow_data[:,1]==9))
flow_countsepttotalafter1999 = np.sum((flow_data[:,3] > 0) & (flow_data[:,0] >= 1999) & (flow_data[:,1]==9))
print('flow_countsepttotalbefore2001', flow_countsepttotalbefore2001)
print('flow_countsepttotalafter1999', flow_countsepttotalafter1999)

flow_countbefore2001 = np.sum((flow_data[:,3] > 50) & (flow_data[:,0] <= 2001) & (flow_data[:,1] == 9))
flow_countafter1999 = np.sum((flow_data[:,3] > 50) & (flow_data[:,0] >= 1999) & (flow_data[:,1] == 9))
print('flow_countsepttotal', flow_countsepttotal)
percenttimes = (1017 * 100) / 1028
percentbefore2001 = (390 / 390) * 100
percentafter1999 = (717 / 728) * 100
print('percenttimes', percenttimes)
print('flow_countbefore2001', flow_countbefore2001)
print('flow_countafter1999', flow_countafter1999)
print('percentbefore2001', percentbefore2001)
print('percentafter1999', percentafter1999)


criteria = (flow_data[:, 3] > 600) & (flow_data[:, 1] == 7)
pick_data = flow_data[criteria, 3]
flow_mean = np.mean(pick_data)

criteria2 = (flow_data[:, 3] > 50) & (flow_data[:, 1] == 9)
pick_data2 = flow_data[criteria2, 3]
flow_mean2 = np.mean(pick_data2)

criteria3 = (flow_data[:, 3] < 50) & (flow_data[:, 1] == 9)
pick_data3 = flow_data[criteria3, 3]
flow_mean3 = np.mean(pick_data3)

# Calculate the average flow for these same criteria 

flow_mean = np.mean(flow_data[(flow_data[:,3] > 600) & (flow_data[:,1]==7),3])
flow_mean2 = np.mean(flow_data[(flow_data[:,3] > 50) & (flow_data[:,1]==9),3])
flow_mean3 = np.mean(flow_data[(flow_data[:,3] < 50) & (flow_data[:,1]==9),3])

print("Flow meets this critera", flow_count, " times")
print('And has an average value of', flow_mean, "when this is true")
print('flow_count2', flow_count2)
print('flow_mean2', flow_mean2)
print('flow_count3', flow_count3)
print('flow_mean3', flow_mean3)

# Make a histogram of data
# Use the linspace  funciton to create a set  of evenly spaced bins
mybins = np.linspace(0, 1000, num=15)
# another example using the max flow to set the upper limit for the bins
#mybins = np.linspace(0, np.max(flow_data[:,3]), num=15) 
#Plotting the histogram
plt.hist(flow_data[:,3], bins = mybins)
plt.title('Streamflow')
plt.xlabel('Flow [cfs]')
plt.ylabel('Count')

# Get the quantiles of flow
# Two different approaches ---  you should get the same answer
# just using the flow column
flow_quants1 = np.quantile(flow_data[:,3], q=[0,0.1, 0.5, 0.9])
print('Method one flow quantiles:', flow_quants1)
# Or computing on a colum by column basis 
flow_quants2 = np.quantile(flow_data, q=[0,0.1, 0.5, 0.9], axis=0)
# and then just printing out the values for the flow column
print('Method two flow quantiles:', flow_quants2[:,3])

# %%
print(flow_data.shape)
print(flow_data.dtype)
# %%
print(len(flow_data))
# %%
print(flow_data.size)
print(flow_data)

# %%
