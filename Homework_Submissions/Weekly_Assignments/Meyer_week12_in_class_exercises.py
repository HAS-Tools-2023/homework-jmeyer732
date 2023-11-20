# %%
# Jessica Meyer
# Week 12 in-class exercises

#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
import dataretrieval.nwis as nwis
import json 
import urllib.request as req
import urllib
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter

# %%
# Exercise 1: 
# 1. Write a function that takes the following arguments as inputs: 
# - USGS Station ID
# - Start Date of desired observations
# - End Date of desired observations
# And returns a dataframe with the USGS streamflow for the desired location and date range. 

def get_my_streamflow(siteID, start, end):
      url_base_1 = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb&site_no="
      url_base_2 = "&referred_module=sw&period=&begin_date="
      url_base_3 = "&end_date="
      url = url_base_1 + siteID + url_base_2 + start + url_base_3 + end
      df = pd.read_table(url, skiprows=30, 
                         names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'], 
                         parse_dates=['datetime'], index_col=['datetime']) 
      return df

#%%
# 2. Select two other gauges on the Verde River (https://maps.waterdata.usgs.gov/mapper/index.html) 
            # and use your function to download the data for all three gauges for the past year 
            # (The two you select plus 09506000). 
start = '1990-01-01'
end = '2023-11-18'

above_verde_river_siteID = '09504950'
camp_verde_siteID = '09506000'
sycamore_creek_siteID = '09503990'

above_verde_river = get_my_streamflow(siteID=above_verde_river_siteID, start=start, end=end)
camp_verde = get_my_streamflow(siteID=camp_verde_siteID, start=start, end=end)
sycamore_creek = get_my_streamflow(sycamore_creek_siteID, start=start, end=end)

#%%
#3. Make a timeseries plot showing the data from all 3 gauges. 

fig, ax = plt.subplots(1, 1, figsize=(10,7))

start='2023-10-18'
end = '2023-11-18'
ax.plot(above_verde_river['flow'][start:end], 
        color='purple', label = 'North of Verde River')
ax.plot(camp_verde['flow'][start:end], 
        color='green', label = 'Verde River')
ax.plot(sycamore_creek['flow'][start:end], 
        color='blue', label = 'Sycamore Creek')
ax.grid(alpha=0.5)
ax.legend(loc='upper left')

majorformattor = mdates.DateFormatter('%b-%d')
ax.get_xaxis().set_major_formatter(majorformattor)
fig.autofmt_xdate(rotation = 45, ha = 'center')
ax.get_xaxis().set_minor_locator(mdates.HourLocator(12))

plt.suptitle('Observed flow north of Verde River, at the Verde River,', fontsize=14)
plt.title(' and Sycamore Creek Oct 18 - Nov 18, 2023', fontsize=14)
# %%
# Exercise 2: 

#1. Download the dataset from the class notes and determine what 
      # (1) type of python object the station observations are and 
      # (2) what all variables are included in the observations. 
mytoken = 'fdf6b5b3b2044f569a1a1f01e61c5090'
base_url = "http://api.mesowest.net/v2/stations/timeseries"
args = {
    'start': '202301010000',
    'end': '202311150000',
    'obtimezone': 'UTC',
    'vars': 'air_temp',
    'stids': 'QVDA3',
    'units': 'temp|F,precip|mm',
    'token': mytoken} 

apiString = urllib.parse.urlencode(args)
api_url = base_url + '?' + apiString
url_open = req.urlopen(api_url)
dict = json.loads(url_open.read())

dict['STATION'][0]['OBSERVATIONS'].keys()
temp = dict['STATION'][0]['OBSERVATIONS']['air_temp_set_1']
date_time = dict['STATION'][0]['OBSERVATIONS']['date_time']

new_df = pd.DataFrame({'Temperature': temp}, index=pd.to_datetime(date_time))
new_df.info()
# ANSWER:
# The object is float64 and the variables included in the dataset are date-time and air temperature.

#%%
#2. Modify the API call to return accumulated precipitation instead (variable name = 'precip_accum', set the units to 'metric') and make a plot of the daily max accumulated precipitation

args = {
    'start': '202301010000',
    'end': '202311150000',
    'obtimezone': 'UTC',
    'vars': 'precip_accum',
    'stids': 'QVDA3',
    'units': 'metric',
    'token': mytoken} 

apiString = urllib.parse.urlencode(args)
api2_url = base_url + '?' + apiString
url_open2 = req.urlopen(api2_url)
dict2 = json.loads(url_open2.read())

date_time = dict2['STATION'][0]['OBSERVATIONS']['date_time']
precip = dict2['STATION'][0]['OBSERVATIONS']['precip_accum_set_1']

units = dict2['UNITS']

new2_df = pd.DataFrame({'Precip': precip}, index=pd.to_datetime(date_time))

resample_12hr = new2_df.resample('12H').max()
# %%
fig, ax = plt.subplots(1, 1, figsize=(12,5))

start='2023-10-18'
end = '2023-11-18'

ax.plot(resample_12hr, 
        color='purple', label = 'Precipitation (mm)')
ax.grid(alpha=0.5)
ax.legend(loc='upper left')

majorformattor = mdates.DateFormatter('%b-%d')
ax.get_xaxis().set_major_formatter(majorformattor)
fig.autofmt_xdate(rotation = 45, ha = 'center')
ax.get_xaxis().set_minor_locator(mdates.HourLocator(12))

plt.suptitle('Observed Precipitation at the Verde River gage', fontsize=14)
plt.title('Oct 18 - Nov 18, 2023', fontsize=14)
# %%
