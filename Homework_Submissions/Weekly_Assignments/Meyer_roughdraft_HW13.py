#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_rows', 500)

#%%

# User inputs for streamgage site ID and forecast date

siteID = '09506000'
forecast_date = '2023-11-26'

# User inputs for different climatological date ranges
start_date = '1990-01-01'
end_date = '2020-12-31'

#%%
# Data retrieval and forecasts
def get_my_streamflow(siteID, start_date, end_date):
       '''
       Attain Streamflow Data From USGS via API
         
       Streamflow data is attained from the USGS website via API. The API is 
       broken down into several parts including a start date, end date, and
       site ID.
         
       Parameters
       ----------
       siteID : string '########'
              The site ID is the unique identifier for a streamgage site.
       start_date : string 'YYYY-MM-DD'
              The start date for the first day of the requested data.
       end_date : string 'YYYY-MM-DD'
              The end date for the last day of the requested data.
                       
       Returns
       -------
       Pandas dataframe of the requested USGS data for the entered site ID.
       '''
       url_base_1 = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no="
       url_base_2 = "&referred_module=sw&period=&begin_date="
       url_base_3 = "&end_date="
       url = url_base_1 + siteID + url_base_2 + start_date + url_base_3 + end_date
       dataframe = pd.read_table(url, skiprows=30, 
                                                   names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'],
                                                   parse_dates=['datetime'], index_col=['datetime']) 
       return dataframe

climatology_data = get_my_streamflow(siteID, start_date, end_date)

def input_date(forecast_date):
       '''
       Separate the Forecast String 
       
       Forecast_date string is separated into month and day integers.
       
       Parameters
       ----------
       forecast_date : string 'YYYY-MM-DD'
              The forecast date entered by the user for the first day of the week 1 forecast.
              
       Returns
       -------
       integer values
              The month and the day of the forecast date.
       '''
       date_df = pd.DataFrame([forecast_date])
       date_df[['year', 'month', 'day']] = forecast_date.split("-")
       date_df['year'] = date_df['year'].astype(int)
       date_df['month'] = date_df['month'].astype(int)
       date_df['day'] = date_df['day'].astype(int)
       date_df.drop(columns=[0], inplace=True)
       month_parse = date_df['month']
       day_parse = date_df['day']
       return month_parse[0].astype(int), day_parse[0].astype(int)

month, day = input_date(forecast_date)  

def get_my_1_week_dates(month, day):
       '''
       1 Week Forecast Dates

       The 1 week forecast start month and day are attained from the input_date 
       function. The end month and day are then calculated using the user
       forecast_date input. For forecast dates that end within the same month,
       the end month is the same as the start month and the end day is 7 days
       after the start day. For forecast dates that end within the next month,
       the end month is the next month and the difference is calculated between
       the end day and the number of days within the start month. The stop day
       is then equivalent to the aforementioned difference. The number of days
       per calendar month is adjusted depending upon the forecast date user 
       input.

       Parameters
       ----------
       month : integer
              The month of the user input forecast date.
       day : integer
              The day of the user input forecast date.
       
       Returns
       -------
       integer values
              The forecast date start month, forecast date start day, forecast
              date end month, and the forecast date end day.
       '''
       start_day = day
       stop_day = (day + 6).astype(int)
       if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) & (stop_day > 31):
              stop_day2 = stop_day - 31
              month2 = month + 1
       elif month == [2] & (stop_day > 28):
              stop_day2 = stop_day - 28
              month2 = month + 1
       elif (month == 4 or month == 6 or month == 9 or month == 11) & (stop_day > 30):
              stop_day2 = stop_day - 30
              month2 = month + 1
       else:
              stop_day2 = stop_day
              month2 = month
       import matplotlib.pyplot as plt
       import matplotlib.dates as mdates
       import json
       import urllib.request as req
       import matplotlib.patches as mpatches
       import matplotlib.lines as mlines

       # Define a class
       class MyClass:
              
              def __init__(self):
                     pass
              
              def my_method(self):
                     pass

       # Define another class
       class AnotherClass:
              
              def __init__(self):
                     pass
              
              def another_method(self):
                     pass

       # Remove unused imports
       # import os
       # import matplotlib.dates as mdates
       # import json
       # import urllib.request as req
       # import urllib
       # import matplotlib.patches as mpatches
       # import matplotlib.lines as mlines
       # from matplotlib.patches import Arrow

       # Add a '#' before the block comments
       # Block comment 1
       # Block comment 2

       # Fix indentation errors
       start_day = 1
       end_day = 30

       # Split long lines into multiple lines
       x = [i for i in range(start_day, end_day)]
       y = [i**2 for i in range(start_day, end_day)]

       # Remove unused variables
       # start_day = 1

       # Remove extra blank lines
       # Remove extra blank lines

       # Remove unexpected spaces around keyword/parameter equals
       # def my_function(param1=1, param2=2):
       #     pass

       # Add indentation to the expected indented blocks
       # if condition:
       #     statement1
       #     statement2
       # else:
       #     statement3
       #     statement4

       # Expected indented block
       # for i in range(10):
       #     statement1
       #     statement2

       # Expected indented block
       # while condition:
       #     statement1
       #     statement2

# Parsing the climatological data frames from the 1 week and 2 week forecast dates.
# The index is parsed by month and day according to the function outputs from 
# above and subset into a new data frame for each given forecast period.
climatology_data_1week = pd.DataFrame(climatology_data[((climatology_data.index.month == week1_dates[0]) & 
                                                                         (climatology_data.index.day >= week1_dates[1])) +
                                                                             ((climatology_data.index.month == week1_dates[2]) &
                                                                              (climatology_data.index.day <= week1_dates[3]))])
climatology_data_2week = pd.DataFrame(climatology_data[((climatology_data.index.month == week2_dates[0]) & 
                                                                         (climatology_data.index.day >= week2_dates[1])) +
                                                                             ((climatology_data.index.month == week2_dates[2]) &
                                                                              (climatology_data.index.day <= week2_dates[3]))])

# Forecasts are calculated using the numpy quantile function and adding 3 to the flow value. 
print('1 week forecast:', np.quantile(climatology_data_1week.flow, 0.25) + 3, 'cfs')
print('2 week forecast:', np.quantile(climatology_data_2week.flow, 0.25) + 3, 'cfs')

# Plotting
fig, ax = plt.subplots(figsize=(7,5))

myweek1 = np.quantile(climatology_data_1week.flow, 0.25) + 3
myweek2 = np.quantile(climatology_data_2week.flow, 0.25) + 3

ax.scatter(x = climatology_data_1week.index, y = climatology_data_1week.flow, color='fuchsia', s=25, marker = '*', linewidth=0.5, label='1 Week Forecast Daily Flow')
ax.axhline(y=myweek1, color='fuchsia', linestyle='--', linewidth=0.5, label = myweek1)
ax1 = ax.twinx()
ax1.scatter(x = climatology_data_2week.index, y = climatology_data_2week.flow,color='green', s=30, marker = '+', linewidth=0.5, label='2 Week Forecast Daily Flow')
ax1.axhline(y=myweek2, color='green', linestyle='--', linewidth=0.5, label=myweek2)
ax.set_xlabel('Date', fontsize=10)
ax.set_ylabel('1 Week Flow (cfs)', fontsize=10)
ax1.set_ylabel('2 Week Flow (cfs)', fontsize=10)
fig.legend(loc = 'upper left', bbox_to_anchor=(0.125,0.875), fontsize=6)
ax.set_title('1 Week and 2 Week Historical Daily Flows and My Forecasts', fontsize=12)
ax.set_ylim(0,1000)
ax1.set_ylim(0,5000)
# %%
