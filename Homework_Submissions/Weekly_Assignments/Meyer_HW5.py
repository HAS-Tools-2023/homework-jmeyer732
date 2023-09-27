#%%
#### Assignment - Meyer
#  1. Copy the top of your starter code from week 4 to read in your streamflow file 
#     and create a numpy array called `flow_data` that has four columns (year, month, 
#     day, flow) and a row for every day. 

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week5.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)

# %%
# DON'T change this part -- this creates the lists you 
# should use for the rest of the assignment
# no need to worry about how this is being done now we will cover
# this in later sections. 

#Read the data into a pandas dataframe
data = pd.read_table(filepath, sep = '\t', skiprows=31,
        names = ['agency_cd', 'site_no', 'datetime', 'flow', 'code']
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
print("flow_data:", flow_data)

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

#%%
# FORECAST code
# Starter Code
# Count the number of values with flow > 600 and month ==7
flow_countsepttotal = np.sum((flow_data[:,3] < 75) & (flow_data[:,1]==9))
flow_count_day1to10 = np.sum((flow_data[:, 3] <75) & (flow_data[:,1]==9) & (flow_data[:,2] < 10))
flow_count_day11to20 = np.sum((flow_data[:, 3] <75) & (flow_data[:,1]==9) & ((flow_data[:,2] < 21) & (flow_data[:,2] > 10)))
flow_count_day21to30_75 = np.sum((flow_data[:, 3] <75) & (flow_data[:,1]==9) & ((flow_data[:,2] < 31) & (flow_data[:,2] > 21)))
flow_count_day21to30_50 = np.sum((flow_data[:, 3] <50) & (flow_data[:,1]==9) & ((flow_data[:,2] < 31) & (flow_data[:,2] > 21)))
flow_count_day21to30_71to75 = np.sum(((flow_data[:, 3] > 70) & (flow_data[:,3] < 76)) & (flow_data[:,1]==9) & ((flow_data[:,2] < 31) & (flow_data[:,2] > 21)))
flow_count_day21to30_66to70 = np.sum(((flow_data[:, 3]  > 65) & (flow_data[:,3] < 71)) & (flow_data[:,1]==9) & ((flow_data[:,2] < 31) & (flow_data[:,2] > 21)))
flow_count_day21to30_61to65 = np.sum(((flow_data[:, 3]  > 60) & (flow_data[:,3] < 66)) & (flow_data[:,1]==9) & ((flow_data[:,2] < 31) & (flow_data[:,2] > 21)))
flow_count_day21to30_56to60 = np.sum(((flow_data[:, 3]  > 55) & (flow_data[:,3] < 61)) & (flow_data[:,1]==9) & ((flow_data[:,2] < 31) & (flow_data[:,2] > 21)))
flow_count_day21to30_50to55 = np.sum(((flow_data[:, 3]  > 49) & (flow_data[:,3] < 56)) & (flow_data[:,1]==9) & ((flow_data[:,2] < 31) & (flow_data[:,2] > 21)))
flow_current = np.sum((flow_data[:, 3] <75) & (flow_data[:,1]==9) & (flow_data[:,0]==2023) & ((flow_data[:,2] < 31) & (flow_data[:,2] > 21)))
currentdailydata = flow_data[(flow_data[:,1]==9) & (flow_data[:,0]==2023) & ((flow_data[:,2]>16) & (flow_data[:,2]<24)),3]

print("flow_countsepttotal", flow_countsepttotal)
print("sept 0 to 10:", flow_count_day1to10)
print("sept 11 to 20:", flow_count_day11to20)
print("sept 21 to 30 below 75:", flow_count_day21to30_75)
print("sept 21 to 30 below 50:", flow_count_day21to30_50)
print("sept 21 to 30 from 71 to 75 cfs:", flow_count_day21to30_71to75)
print("sept 21 to 30 from 66 to 70 cfs:", flow_count_day21to30_66to70)
print("sept 21 to 30 from  60 to 65 cfs:", flow_count_day21to30_61to65)
print("sept 21 to 30 from 55 to 60 cfs:", flow_count_day21to30_56to60)
print("sept 21 to 30 from 50 to 54 cfs:", flow_count_day21to30_50to55)
print("flow_current:", flow_current)
print("currentdailydata:",("S:", currentdailydata[0]),
      ("M:", currentdailydata[1]), ("T:", currentdailydata[2]), ("W:", currentdailydata[3]),
      ("R:", currentdailydata[4]), ("F:", currentdailydata[5]), ("S:", currentdailydata[6]))
#%%
for i in range(len(flow_data[:,0])):
      if flow_data[i,0] > 2010:
           if flow_data[i,1] == 9:
                if flow_data[i,2] < 24:
                        if flow_data[i,2] > 16:
                                if flow_data[i,3] > 200 or flow_data[i,3] < 100:
                                         print(flow_data[i])

#%%
for i in range(len(flow_data[:,0])):
      if flow_data[i,0] > 2010:
           if flow_data[i,1] == 9:
                if flow_data[i,2] < 31:
                        if flow_data[i,2] > 23:
                                if flow_data[i,3] > 200 or flow_data[i,3] < 100:
                                         print(flow_data[i])

#%%
for i in range(len(flow_data[:,0])):
      if flow_data[i,0] > 2010:
           if flow_data[i,1] == 10:
                if flow_data[i,2] < 8:
                        if flow_data[i,2] > 1:
                                if flow_data[i,3] > 200 or flow_data[i,3] < 100:
                                         print(flow_data[i])
#%%
criteria1 = (flow_data[:, 3] < 75) & (flow_data[:, 1] == 9)
pick_data1 = flow_data[criteria1, 3]
flow_mean1 = np.mean(pick_data1)

criteria2 = (flow_data[:, 3] < 60) & (flow_data[:, 1] == 9)
pick_data2 = flow_data[criteria2, 3]
flow_mean2 = np.mean(pick_data2)

criteria3 = (flow_data[:, 3] < 45) & (flow_data[:, 1] == 9)
pick_data3 = flow_data[criteria3, 3]
flow_mean3 = np.mean(pick_data3)

print('flow_mean1.1', flow_mean1)
print('flow_mean2.1', flow_mean2)
print('flow_mean3.1', flow_mean3)
#%%
# Calculate the average flow for these same criteria 

flow_mean1_2 = np.mean(flow_data[((flow_data[:,3] < 70) & (flow_data[:,1]==9) & (flow_data[:,2]>23) & (flow_data[:,2]<31)),3])
flow_mean2_2 = np.mean(flow_data[((flow_data[:,3] < 60) & (flow_data[:,1]==9) & (flow_data[:,2]>23) & (flow_data[:,2]<31)),3])
flow_mean3_2 = np.mean(flow_data[((flow_data[:,3] < 50) & (flow_data[:,1]==9) & (flow_data[:,2]>23) & (flow_data[:,2]<31)),3])
current_mean_flow = np.mean(flow_data[((flow_data[:,1]==9) & (flow_data[:,0]==2023) & (flow_data[:,2]>16) & (flow_data[:,2]<24)),3])

print('flow_mean1_2', flow_mean2)
print('flow_mean2_2', flow_mean2_2)
print('flow_mean3_2', flow_mean3_2)
print("current_mean_flow", current_mean_flow)
#%%
# ASSIGNMENT code
# 2. Create a new numpy array that has the same four columns as flow_data  
#     but includes only the data for the five year period from 
#     **1/1/2015-12/31/2019**. Call your new array `flow_5yr`. For all subsequent 
#     questions we will just use `flow_5yr` for our analysis. Print out the 
#     dimensions of `flow_5yr` along with the average flow in this five year 
#     period (i.e. just one number averaged across the entire timeseries). Provide 
#     both these values in your markdown write up. 
#     **BONUS:** Show how you can do this with 1 line of code, 2 lines of code 
#     and using a for loop

#%%
flow_5yr = flow_data[(flow_data[:,0] >= 2015) & (flow_data[:,0] <= 2019),:]
print(flow_5yr)
print(flow_5yr.shape)

print("Dimensions of 5 year array:", flow_5yr.shape)
print("Average 5 year daily flow:", np.mean(flow_5yr[:,3]), "cfs")

# %%
#  3. Convert the daily average flow from cubic feet per second to cubic feet. Do 
#     this two ways, (1) without using a for loop,  and (2) with using a for loop. 
#     Save this a a variable called `flow_daily`.  Report the first 5 daily flow 
#     values in your markdown as well as the total flow in cubic feet over the 
#     entire time period. 

# 3.1 Without using a loop
method1 = flow_5yr[:,3] * 86400
print(method1)

#%%
# 3.2 Using a loop
flow_daily = []
for i in range(len(flow_5yr[:, 1])): #the length of any column you want
         temp = flow_5yr[i,3] * 86400
         flow_daily = np.append(flow_daily,temp)
         print(flow_daily)
         print(np.sum(flow_daily))
#%%
#   4. Create a time series of monthly average flow from the daily flow values 
#       (i.e. I'm looking for a timeseries that is 60 months long). You should store 
#       this in a numpy array called `flow_monthly` that has 60 rows and three 
#       columns. The first column should be year, the second month and the third 
#       should be flow. Print out the first five rows of this array and report them 
#       in your markdown file. **HINT**: To fill in the year and month columns I 
#       recommend you use the functions `np.arange`, `np.tile` and `np.repeat`. 

#%%
flow_monthly = np.zeros((60, 3))
flow_monthly[:12,0] = np.tile(np.arange(2015,2016,1),12)
flow_monthly[12:24,0] = np.tile(np.arange(2016,2017,1),12)
flow_monthly[24:36,0] = np.tile(np.arange(2017,2018,1),12)
flow_monthly[36:48,0] = np.tile(np.arange(2018,2019,1),12)
flow_monthly[48:60,0] = np.tile(np.arange(2019,2020,1),12)
flow_monthly[:,1] = np.tile(np.arange(1, 13, 1), 5)
#flow_monthly[:,2] = np.tile(np.arange(1, 61, 1), 1)
print(flow_monthly)

#%%
for i in range(60):
        ytemp = flow_monthly[i,0]
        mtemp = flow_monthly[i,1]
        #print(ytemp,mtemp)
        ilist = (flow_5yr[:,0] == ytemp) & (flow_5yr[:,1] == mtemp)
        mean = np.mean(flow_5yr[ilist,3])
        #flow = flow_monthly[i,2]
        flow_monthly[i,2] = mean
        print(flow)
# %%
print(flow_monthly)

# %%
