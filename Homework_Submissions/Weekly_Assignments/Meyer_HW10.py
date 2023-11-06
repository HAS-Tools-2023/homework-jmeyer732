# %% 
# ------------------------IMPORT ALL RELEVANT LIBRARIES -----------------------
#        .set_option : specifies a display attribute
# 'display.max_rows' : tells pandas to display a maximum number of rows in the
#                      interactive terminal

import os
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
pd.set_option('display.max_rows', 500)


# %%
# ----------IDENTIFY THE FILE NAME AND TELL PYTHON WHERE TO FIND IT------------
# os.path.join() : tells the operating system the pathway to join/link/find a 
#                  specific file. In this code, the data file I want to use 
#                  is within the same directory, thus, there is no directed 
#                  pathway. If the data file was in a different directory, the
#                  code would read: 
#                       filepath = os.path.join('../datastoredhere', filename)
#    os.getcwd() : tells python to print the 'current working directory' of the
#                  operating system in which you are working

filename = 'streamflow_data.txt'
filepath = os.path.join(filename) 
print(os.getcwd())
print(filepath)


#%%
# ------------------READ THE DATA INTO A PANDAS DATAFRAME---------------------
#  .read_table : a pandas function that breaks down and processes the given 
#                data file into chuncks
#     filepath : where to find the data
#          sep : tells pandas how to read data; here it is by tab separation
#     skiprows : within a .txt or .csv file, the number of rows within data 
#                file to skip
#      usecols : tells pandas which columns within the given data to use 
#                within the pandas dataframe
#        names : tells pandas the identifying name of the columns for reference
#  parse_dates : a function that converts a scalar, array-like, series, 
#                dataframe, or dictionary to a pandas dataframe date-time object
#    .dropna() : removes/drops missing value rows from the pandas dataframe
# .set_index() : sets the pandas dataframe index as a specified object; for 
#                this code .set_index('datetime') sets/identifies the index as
#                a date-time object

df = pd.read_table(
                  filename, sep = '\t', skiprows=31,
                  names = ['agency_cd', 'site_no', 'datetime', 'flow', 'code'], 
                  parse_dates = ['datetime'])

df = df.set_index('datetime')


#%% 
# ----------------------BASIC CHECKS BEFORE PROCEEDING-------------------------
#     df.index : prints the index of the pandas dataframe
#     print()  : prints the dataframe

print(df.index)
print(df)
print(df.dtypes)


#%%
# -----------------------SUBSETTING STREAMFLOW BY INDEX------------------------

# ----------------------------PREVIOUS TWO MONTHS------------------------------
# -------------------------SEPTEMBER 4 TO NOVEMBER 4--------------------------- 

flow_2023 = pd.DataFrame(
                  df[((df.index.year == 2023) & (df.index.month == 9) 
                  & (df.index.day >= 5) & (df.index.day <= 31)) + 
                  ((df.index.year == 2023) & (df.index.month == 10) 
                  & (df.index.day >= 1) & (df.index.day <= 31)) +
                  ((df.index.year == 2023)& (df.index.month == 11)
                  & (df.index.day <= 4))])

recent_flow = pd.DataFrame(
                        df[((df.index.year >= 2020))])

# --------------------TWO WEEK FORECASTS USING CLIMATOLOGIES-------------------
# ---------------------------NOVEMBER 5 TO NOVEMBER 11-------------------------
# --------------------------------------&--------------------------------------
# --------------------------NOVEMBER 12 TO NOVEMBER 18-------------------------

nov5_11 = pd.DataFrame(
                        df[((df.index.year >= 1991) & (df.index.year <= 2020) 
                        & (df.index.month == 11) & (df.index.day >= 5) 
                        & (df.index.day <= 11))])

nov12_18 = pd.DataFrame(
                        df[(df.index.year >= 1991) & (df.index.year <= 2020) 
                        & (df.index.month == 11) & (df.index.day >= 12) 
                        & (df.index.day <= 18)])


#%% ---------------------BASIC CHECKS BEFORE PROCEEDING------------------------
#       .describe() : displays the min, max, mean, standard deviation, and
#                     quantiles of the dataframe

nov5_11.describe()
print(nov5_11)
print(nov12_18)

# %%
# -------------------PRINTING STREAMFLOW FORECAST VALUES-----------------------
#       .flow.mean() : take the 'flow' column values within dataframe and
#                      calculate the mean

print(nov5_11.flow.describe())
print(79.7 / 100 * 140.5)

# %%
print(nov12_18.flow.describe())
print(79.7 / 100 * 154.25)

#%%
two_weeks_ago_actual = pd.DataFrame(
                        df[(df.index.year == 2023) 
                        & (df.index.month == 10) & (df.index.day >= 22) 
                        & (df.index.day <= 28)])
two_weeks_ago_climatology = pd.DataFrame(
                        df[(df.index.year >= 1991) & (df.index.year<=2020)
                        & (df.index.month == 10) & (df.index.day >= 22) 
                        & (df.index.day <= 28)])

one_week_ago_actual = pd.DataFrame(
                        df[((df.index.year == 2023) 
                        & (df.index.month == 10) & (df.index.day >= 29) 
                        & (df.index.day <= 31)) + ((df.index.year >= 1991) 
                        & (df.index.year <= 2020) & (df.index.month == 11) 
                        & (df.index.day >= 1) & (df.index.day <= 4))])
one_week_ago_climatology = pd.DataFrame(
                        df[((df.index.year >= 1991) & (df.index.year <=2020)
                        & (df.index.month == 10) & (df.index.day >= 29) 
                        & (df.index.day <= 31)) + ((df.index.year >= 1991) 
                        & (df.index.year <= 2020) & (df.index.month == 11) 
                        & (df.index.day >= 1) & (df.index.day <= 4))])

#%%
# -------------------COMPARISONS OF CLIMATOLOGY VS RECORDED DATA---------------
print(two_weeks_ago_actual.describe())
#     Recorded Data
#           mean: 105.157
#           25% quantile: 100.75

print(two_weeks_ago_climatology.describe())
#     Climatology
#           mean: 158.322
#           25% quantile: 114

print(one_week_ago_actual.describe()) 
#     Recorded Data
#           mean: 173.821
#           25% quantile: 130

print(one_week_ago_climatology.describe()) 
#     Climatology
#           mean: 186.38
#           25% quantile: 130

#%%
# ------------------------------PAST CALCULATIONS------------------------------
# TWO WEEKS AGO
# Mean : 66.42%
print(105.157 / 158.322 * 100,'%')

# 25% Quantile : 88.38%
print(100.75 / 114 * 100,'%')



# ONE WEEK AGO                      
# Mean : 93.26%
print(173.821 / 186.38 * 100,'%')

# 25% Quantile : 100%            
print(130 / 130 * 100,'%')

#%%
# -----------------------------FUTURE CALCULATIONS-----------------------------

print(100 - 88.38) # = 11.62% difference 25% Quantile
print(93.26 - 66.42) # = 26.84% difference Mean


# ONE WEEK : NOV 5 - 11
print(100 + (11.62 / 4)) # = 102.905% 25% Quantile
print(93.26 + (26.84 / 4)) # = 99.97% Mean
print(nov5_11.flow.describe()) # Clim Mean: 190.75 and Clim 25% Quantile: 140.5

print(1.02905 * 140.5) # Calculated 25% Quantile: 147.29cfs
print(0.9997 * 190.75) # Calculated Mean: 192.49cfs


# TWO WEEK : NOV 12 - 18
print(100 + (11.62 / 2)) # = 105.81% 25% Quantile
print(93.26 + (26.84 / 2)) # = 106.68% Mean

print(nov12_18.flow.describe()) # Clim Mean: 188.85 and Clim 25% Quantile: 154.25
print(1.0581 * 154.25) # Calculated 25% Quantile: 163.21cfs
print(1.0668 * 188.85) # Calculated Mean: 201.47cfs


#%%
print("1 week forecast:", 192.49,'cfs')
print("2 week forecast:", 201.47,'cfs')

# %%
fig, (ax) = plt.subplots(1, 1, figsize=(10,10))
nov5_11['flow'].plot(color = 'violet', linewidth = 2, label = 'Nov 5 - 11 Historical')
nov12_18['flow'].plot(color = 'turquoise', linewidth = 2,label = 'Nov 12 - 18 Historical')
flow_2023['flow'].plot(color = 'lightgreen', linewidth = 2, label = 'Previous Two Months')

plt.xlabel('Month', fontsize=13)
plt.ylabel('Streamflow (cfs)', fontsize = 13)
plt.grid(alpha = 0.75, color = 'gray')
plt.ylim(0,1000)
ax.set_facecolor(color='whitesmoke')
ax.set_title('Historical Stream Flow')
plt.legend()
# %%
fig, (ax) = plt.subplots(1, 1, figsize=(20,10))
recent_flow['flow'].plot(color = 'lightpink', linewidth = 2, label = 'Historical Streamflow')
flow_2023['flow'].plot(color = 'lightgreen', linewidth = 2, label='2023 Historical Streamflow')

plt.xlabel('Month', fontsize=20)
plt.ylabel('Stream Flow (cfs)', fontsize = 20)
plt.grid(alpha = 0.75, color = 'gray')
plt.ylim(0,1000)
ax.set_facecolor(color='whitesmoke')
ax.set_title('Historical Stream Flow', fontsize = 30)
plt.legend()
# %%
