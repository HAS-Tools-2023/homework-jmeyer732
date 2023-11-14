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
from datetime import date
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

filename = 'streamflow_week10.txt'
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
# --------------------------AUGUST 28 TO OCTOBER 28---------------------------- 

flow_2023 = pd.DataFrame(
                  df[((df.index.year == 2023) & (df.index.month == 8) 
                  & (df.index.day >= 29) & (df.index.day <= 31)) + 
                  ((df.index.year == 2023) & (df.index.month == 9)) +
                  ((df.index.year == 2023) & (df.index.month == 10) 
                  & (df.index.day <= 28))])

#LC Here is an example of how look for dates between the start and end date more simply.
# Also note you don't need to convert it to a dataframe, it already is one 

flow_2023 = df[(df.index >='2023-08-28') & (df.index <='2023-10-28')]


## LC I like that you have headers but having multiple headers like this actually makes your comments a bit harder to read  I would just have one line with the --- and then provide more details below it without the ---
# Also your comments are really short so its hard to follow exactly what you are doing. You are actually getting each of these date ranges out for a range of years. 

# --------------------TWO WEEK FORECASTS USING CLIMATOLOGIES-------------------
# ---------------------------OCTOBER 29 TO NOVEMBER 4--------------------------
# --------------------------------------&--------------------------------------
# ---------------------------NOVEMBER 5 TO NOVEMBER 11-------------------------

#LC see comment above for how to shorten this. 
# LC -- also since this is something you are doing frequently you could make it a function liek this
def get_daterange(mydataframe, start_date, end_date):
        subset_data=df[(mydataframe.index >=start_date) & (mydataframe.index <=end_date)]  
        return subset_data



# LC This is a lot ot parse to see what you are doing definitely needs a comment
clim_week1 = pd.DataFrame(
                        df[((df.index.year >= 1991) & (df.index.year <= 2020) 
                        & (df.index.month == 10) & (df.index.day >= 29) 
                        & (df.index.day <= 31)) + ((df.index.year >= 1991) 
                        & (df.index.year <= 2020) & (df.index.month == 11) 
                        & (df.index.day >= 1) & (df.index.day <= 4))])

clim_week2 = pd.DataFrame(
                        df[(df.index.year >= 1991) & (df.index.year <= 2020) 
                        & (df.index.month == 11) & (df.index.day >= 5) 
                        & (df.index.day <= 11)])


#%% ---------------------BASIC CHECKS BEFORE PROCEEDING------------------------
#       .describe() : displays the min, max, mean, standard deviation, and
#                     quantiles of the dataframe

clim_week1.describe()
print(clim_week1)
print(clim_week2)

# %%
# -------------------PRINTING STREAMFLOW FORECAST VALUES-----------------------
#       .flow.mean() : take the 'flow' column values within dataframe and
#                      calculate the mean
#LC -- You dont need to define what the functions are in your comments. The reader can see that by looking at the help functions what you need to explain is what you are doing with the functions and why eg:
# Calculating the 1 week forecast as 60% of the average flow for the preceeding week 1991-2023 

print("1 week forecast:", (clim_week1.flow.mean() * 0.6))
print("2 week forecast:", (clim_week2.flow.mean() * 0.6))
print(flow_2023.index)

#%%
# -----------------------------DEFINING FUNCTIONS------------------------------
# LC Nice functions!
#LC : each function needs a comment (preferably a doc string) to explain its purpose and what the inputs and outputs are
def extremes1(clim_week1, month, day):
          vals1 = clim_week1[(clim_week1.index.month == month) 
                             & (clim_week1.index.day == day)]
          extremeflow1max = np.max(vals1['flow'])
          extremeflow1min = np.min(vals1['flow'])
          return(extremeflow1max, extremeflow1min)

def extremes2(clim_week2, month, day):
          vals2 = clim_week2[(clim_week2.index.month == month) 
                             & (clim_week2.index.day == day)]
          extremeflow2max = np.max(vals2['flow'])
          extremeflow2min = np.min(vals2['flow'])
          return(extremeflow2max, extremeflow2min)


extremes_week1 = extremes1(clim_week1, month = (10 or 11), 
                           day = (29 or 30 or 31 or 1 or 2 or 3 or 4))
extremes_week2 = extremes2(clim_week2, month = 11,
                           day = (5 or 6 or 7 or 8 or 9 or 10 or 11))

print("week 1:", extremes_week1,"week 2:", extremes_week2)


#%%
# ------------------CALCULATING THE MEAN OF THE COLUMN 'FLOW'------------------
# -----------------------IDENTIFYING EXTREMES MANUALLY-------------------------
clim_flow1 = clim_week1['flow'].mean()
clim_flow2 = clim_week2['flow'].mean()
recentflow = flow_2023['flow'].mean()

# LC confused about this -- what is the purpose of your functions in tis case? 
extremes_week1_max = 891.0
extremes_week1_min = 97.1
extremes_week2_max = 395
extremes_week2_min = 123

clim_flow1, clim_flow2, extremes_week1, extremes_week2

#%% ----------------------BASIC CHECK BEFORE PROCEEDING------------------------

print(clim_week1.index)
print(clim_week2.index)
print(flow_2023.index)

# %%
# ---------------------------CREATING SUBPLOTS---------------------------------
# plt.subplots : plot subplots within the figure of 2 by 2 plots that do not
#                share an x-axis, with a figure size of 15 by 14 
#     .uptitle : a 'super' title or 'supreme' overall, figure title
# ax[0,0].plot : in position [0,0] or upper left of subplots, plot ...
#    linestyle : style of line to plot
#       marker : the symbol to mark a variable within the plot
#        alpha : transparency of the plotted color (0 is 100% transparent)
#    .set_y_lim : sets the y axis limit for that subplot
#       .legend : plots a relevent legend within the subplot
#        .grid : defining gridlines within a subplot
# .xaxis.set_major_formatter : have a set date-time formatting along
#                the x-axis for the subplot
#   .linewidth : thickness of plotted line
#     .axhline : plots a horizontal line at the designated variable
# plt.tight_layout() : makes all plots within the figure tighter or closer

# LC -- NO need to repeat function parameters in your comments. This actually makes your code harder to follow because there is a bunch of documentation that is not really explaining to the reader what your code is doing. 

fig, (ax) = plt.subplots(2, 2, figsize = (15,14), sharex = False)
plt.suptitle(
      "Climatological Streamflow Values and Means of Oct 29 - Nov 4 and Nov 4 - Nov 11:",
      fontsize = 20)

start1 = '2015-10-28'
stop1 = '2020-10-28'
start2 = '2023-08-28'
stop2 = '2023-10-28'

ax[0,0].plot(clim_week1['flow'][start1:stop1], linestyle = ' ', marker = '*',
            color = 'green', alpha = 1, linewidth = 2,
            label = 'Oct 29 - Nov 4 Historic Streamflow: 186.4 cfs')
ax[0,0].plot(df['flow'][start1:stop1], linestyle = '-', color = 'black',
             alpha = 0.25)
ax[0,0].set_ylim(0,250)
ax[0,0].legend(fontsize = 8)
ax[0,0].set_ylabel('Streamflow (cf/s)', fontsize = 12)
ax[0,0].grid(which = 'major', linestyle = '-', alpha = 0.5)
ax[0,0].xaxis.set_major_formatter(mdates.DateFormatter('20%y'))

ax[1,0].plot(clim_week2['flow'][start1:stop1], linestyle = ' ', marker = '*',
            color = 'blue', alpha = 1, linewidth = 2,
            label = 'Nov 5 - Nov 11 Historic Streamflow: 190.8 cfs')
ax[1,0].plot(df['flow'][start1:stop1], linestyle = '-', color = 'black',
             alpha = 0.25)
ax[1,0].set_ylim(0,250)
ax[1,0].legend(fontsize = 8)
ax[1,0].set_ylabel('Streamflow (cf/s)', fontsize = 12)
ax[1,0].grid(which = 'major', linestyle = '-', alpha = 0.5)
ax[1,0].xaxis.set_major_formatter(mdates.DateFormatter('20%y'))

ax[0,1].plot(flow_2023['flow'][start2:stop2], linestyle = ' ', marker = '*',
             color = 'r', alpha = 1, linewidth = 2,
             label = 'Aug - Oct 2023 Historic Streamflow')
ax[0,1].plot(df['flow'][start2:stop2], linestyle = '-', color = 'black',
             alpha = 0.25)
ax[0,1].legend(fontsize = 8)
ax[0,1].set_ylabel('Streamflow (cf/s)', fontsize = 12)
ax[0,1].grid(which = 'major', linestyle = '-', alpha = 0.5)
ax[0,1].xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))

ax[1,1].axhline(clim_flow1, alpha = 1, color = 'green', linestyle = '-',
                linewidth = 1.5,
                label = 'Oct 29 - Nov 4, 1991 - 2020 Climatological Mean Flow')
ax[1,1].axhline(clim_flow2, alpha = 1, color = 'blue', linestyle = '-', 
                linewidth = 1.5,
                label = 'Nov 5 - Nov 11, 1991 - 2020 Climatological Mean Flow')
ax[1,1].axhline(recentflow, alpha = 1, color = 'r', linestyle = '-',
                linewidth = 1.5, label = 'Aug - Oct 2023 Mean Flow')
ax[1,1].set_ylim(0,900)
ax[1,1].set_ylabel('Streamflow (cf/s)', fontsize = 12)
ax[1,1].set_xlim(1991, 2020)
ax[1,1].axhline(extremes_week1_min, linestyle = '-', color = 'cyan',
                linewidth = 1.5, alpha = 0.5,
                label = '1991 - 2020 Oct 29 - Nov 4 Streamflow Extreme Min')
ax[1,1].axhline(extremes_week1_max, linestyle = '-', color = 'cyan',
                linewidth = 1.5, alpha = 1,
                label = '1991 - 2020 Oct 29 - Nov 4 Streamflow Extreme Max')
ax[1,1].axhline(extremes_week2_min, linestyle = '-', color = 'magenta',
                linewidth = 1.5, alpha = 0.5,
                label = '1991 - 2020 Nov 4 - Nov 11 Streamflow Extreme Min')
ax[1,1].axhline(extremes_week2_max, linestyle = '-', color = 'magenta',
                linewidth = 1.5, alpha = 1,
                label = '1991 - 2020 Nov 4 - Nov 11 Streamflow Extreme Max')
ax[1,1].legend(fontsize = 8)

plt.tight_layout()

#%%
# -------------------------CREATING A HISTOGRAM--------------------------------
#     .linspace : sets regular intervals within an alloted range
#      plt.hist : plots a histogram within the figure
#          bins : the number of bins or bars to use within the histogram
#         width : the width of each histogram bar

mybins = np.linspace(0, np.max(flow_2023['flow']), num=100) 
plt.hist(df['flow'][start1:stop1], bins = mybins, width = 1.25, alpha = 0.75,
         color = 'orange', label = 'Historic Streamflow')
plt.hist(flow_2023['flow'][start2:stop2], bins = mybins, width = 1.25,
         color = 'blue', label = '2023 Streamflow')
plt.title('Streamflow Occurrances from 2015 - 2020 & 2023')
plt.xlabel('Flow (cf/s)')
plt.ylabel('Number of Occurrances')
plt.grid(alpha = 0.5)
plt.legend()

# %%
