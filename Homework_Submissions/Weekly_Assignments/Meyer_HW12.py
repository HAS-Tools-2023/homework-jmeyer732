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
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import json 
import urllib.request as req
import urllib
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from matplotlib.patches import Arrow as Arrow
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
# -----------------------SUBSETTING STREAMFLOW BY INDEX------------------------

# ----------------------------PREVIOUS TWO MONTHS------------------------------
# -------------------------SEPTEMBER 18 TO NOVEMBER 18--------------------------- 

flow_2023 = pd.DataFrame(
                  df[((df.index.year == 2023) & (df.index.month == 9) 
                  & (df.index.day >= 18) & (df.index.day <= 31)) + 
                  ((df.index.year == 2023) & (df.index.month == 10) 
                  & (df.index.day >= 1) & (df.index.day <= 31)) +
                  ((df.index.year == 2023)& (df.index.month == 11)
                  & (df.index.day <= 18))])

recent_flow = pd.DataFrame(
                        df[((df.index.year >= 2020))])

# --------------------TWO WEEK FORECASTS USING CLIMATOLOGIES-------------------
# ---------------------------NOVEMBER 19 TO NOVEMBER 25-------------------------
# --------------------------------------&--------------------------------------
# --------------------------NOVEMBER 26 TO DECEMBER 2-------------------------

nov19_25 = pd.DataFrame(
                        df[(df.index.year >= 1991) & (df.index.year <= 2020) 
                        & (df.index.month == 11) & (df.index.day >= 19) 
                        & (df.index.day <= 25)])

nov26_dec2 = pd.DataFrame(
                        df[((df.index.year == 2023) 
                        & (df.index.month == 11) & (df.index.day >= 26)) 
                        + ((df.index.year >= 1991) 
                        & (df.index.year <= 2020) & (df.index.month == 12) 
                        & (df.index.day <=2))])

#%% ---------------------BASIC CHECKS BEFORE PROCEEDING------------------------
#       .describe() : displays the min, max, mean, standard deviation, and
#                     quantiles of the dataframe

nov19_25.describe()
nov26_dec2.describe()
print(nov19_25)
print(nov26_dec2)

# %%
# -------------------PRINTING STREAMFLOW FORECAST VALUES-----------------------
#       .flow.mean() : take the 'flow' column values within dataframe and
#                      calculate the mean

print(nov19_25.flow.describe())


# %%
print(nov26_dec2.flow.describe())


#%%


two_weeks_ago_actual = pd.DataFrame(
                        df[((df.index.year == 2023) 
                        & (df.index.month == 11) & (df.index.day >= 5) 
                        & (df.index.day <= 11))])

two_weeks_ago_climatology = pd.DataFrame(
                        df[((df.index.year >= 1991) & (df.index.year <=2020)
                        & (df.index.month == 11) & (df.index.day >= 5) 
                        & (df.index.day <= 11))])

one_week_ago_actual = pd.DataFrame(
                        df[(df.index.year == 2023) 
                        & (df.index.month == 11) & (df.index.day >= 12) 
                        & (df.index.day <= 18)])

one_week_ago_climatology = pd.DataFrame(
                        df[(df.index.year >= 1991) & (df.index.year <= 2020)
                        & (df.index.month == 11) & (df.index.day >= 12) 
                        & (df.index.day <= 18)])
#%%
# -------------------COMPARISONS OF CLIMATOLOGY VS RECORDED DATA---------------
print(two_weeks_ago_actual.describe())
#     Recorded Data
#           mean: 136.86
#           25% quantile: 133.00

print(two_weeks_ago_climatology.describe())
#     Climatology
#           mean: 190.75
#           25% quantile: 140.00

print(one_week_ago_actual.describe()) 
#     Recorded Data
#           mean: 156.57                     
#           25% quantile: 152.00               

print(one_week_ago_climatology.describe()) 
#     Climatology
#           mean: 188.85
#           25% quantile: 154.25

#%%
print("Week 1 forecast:", (np.quantile(nov19_25.flow, 0.25) + 5),'cfs')
print("Week 2 forecast:", (np.quantile(nov26_dec2.flow, 0.25) + 5),'cfs')

# %%
fig, (ax) = plt.subplots(2, 1, figsize=(10,7))
plt.suptitle('Climatological (1991 - 2020) Streamflows of Nov 18 - 25 & Nov 26 - Dec 2')
ax[0].plot(nov19_25['flow'], color = 'violet', linewidth = 2, label = 'Nov 19 - 25 Historical')
ax[0].plot(nov26_dec2['flow'], color = 'turquoise', linewidth = 2,label = 'Nov 26 - Dec 2 Historical')
ax[0].set_ylim(0,1400)
ax[0].set_facecolor(color='whitesmoke')
ax[0].set_ylabel('Streamflow (cfs)', fontsize = 11)
ax[0].grid(alpha = 0.75, color = 'gray')
ax[0].legend(loc='upper left')

ax[1].plot(flow_2023['flow'],color = 'lightgreen', linewidth = 2, label = 'Sept 18 - Nov 18, 2023')
ax[1].grid(alpha = 0.75, color = 'gray')
ax[1].set_facecolor(color='whitesmoke')
ax[1].set_xlabel('Date', fontsize=13)
ax[1].set_ylabel('Streamflow (cfs)', fontsize = 11)
ax[1].legend(loc='upper left')
ax[0].set_title('and Sept 18 - Nov 18, 2023 Streamflow')
date_form = DateFormatter("%m-%d")
ax[1].xaxis.set_major_formatter(date_form)

plt.tight_layout()
plt.savefig('Streamflow.jpg')


#%%
# Accessing data via API
url = 'https://api.synopticdata.com/v2/stations/timeseries' \
      '?&token=fdf6b5b3b2044f569a1a1f01e61c5090&start=' \
            '202212150000&end=202301150000&stid=KGTU'

url_open = req.urlopen(url)
dict = json.loads(url_open.read())
dict.keys()

#%%
dict['UNITS']

# %%
dict['STATION']

#%%
dict['STATION'][0]['OBSERVATIONS'].keys()

# %%
datetime = dict['STATION'][0]['OBSERVATIONS']['date_time']
temp = dict['STATION'][0]['OBSERVATIONS']['air_temp_set_1']
precip = dict['STATION'][0]['OBSERVATIONS']['precip_accum_one_hour_set_1']
wind_dir = dict['STATION'][0]['OBSERVATIONS']['wind_direction_set_1']
wind_speed = dict['STATION'][0]['OBSERVATIONS']['wind_speed_set_1']
pressure = dict['STATION'][0]['OBSERVATIONS']['pressure_set_1d']
wind_gust = dict['STATION'][0]['OBSERVATIONS']['wind_gust_set_1']
dew_point = dict['STATION'][0]['OBSERVATIONS']['dew_point_temperature_set_1d']
# %%
# Combining data into a pandas dataframe
austin_df = pd.DataFrame({'dew_point':dew_point, 'wind_gust':wind_gust,'precip':precip, 'temp' : temp,
                        'wind_dir': wind_dir, 'wind_speed':wind_speed, 'pres': pressure}, index=pd.to_datetime(datetime))
new_df = pd.DataFrame({'datetime':datetime, 'precip':precip, 'temp' : temp,
                        'wind_dir': wind_dir, 'wind_speed':wind_speed, 'pres': pressure})
new_df.set_index('datetime').asfreq('H').rolling(6)
#%%
wind_speed_array = (np.array(wind_speed)).astype(float)
wind_direction_array = (np.array(wind_dir)).astype(float)
temp_array = (np.array(temp)).astype(float)
pressure_array = (np.array(pressure)).astype(float)
dew_point_array = (np.array(dew_point)).astype(float)
#%%
u_wind = np.array([])
v_wind = np.array([])
f_temp = np.array([])
p_hpa = np.array([])
dpt = np.array([])
for i in range(len(austin_df[:])):
      u = np.cos(np.radians(wind_direction_array[i])) * wind_speed_array[i]
      v = np.sin(np.radians(wind_direction_array[i])) * wind_speed_array[i]
      f = (temp_array[i] * 1.8) + 32
      d = (dew_point_array[i] * 1.8) + 32
      p = pressure_array[i] / 100
      u_wind = np.append(u_wind, u)
      v_wind = np.append(v_wind, v)
      f_temp = np.append(f_temp, f)
      p_hpa = np.append(p_hpa, p)
      dpt = np.append(dpt, d)

#%%
austin_df.insert(5, 'u-wind', u_wind)
austin_df.insert(6, 'v-wind', v_wind)
austin_df.insert(7, 'temp (f)', f_temp)
austin_df.insert(8, 'pres (hpa)', p_hpa)
austin_df.insert(9, 'dew point (f)', dpt)
#%%
n = 10
y = [0] * 29

#%%
temp_resample_mean = austin_df['temp (f)'].resample('1H').mean()
temp_resample_min = austin_df['temp (f)'].resample('1H').min()
temp_resample_max = austin_df['temp (f)'].resample('1H').max()

wind_resample_max = austin_df['wind_speed'].resample('1H').max()
wind_resample_mean = austin_df['wind_speed'].resample('1H').mean()
wind_resample_min = austin_df['wind_speed'].resample('1H').min()

u_wind_resample = austin_df['u-wind'].resample('3H').max()
v_wind_resample = austin_df['v-wind'].resample('3H').max()

wind_gust_resample = austin_df['wind_gust'].resample('1H').max()

dpt_resample_min = austin_df['dew point (f)'].resample('1H').min()
dpt_resample_mean = austin_df['dew point (f)'].resample('1H').mean()
dpt_resample_max = austin_df['dew point (f)'].resample('1H').max()

pres_resample_mean = austin_df['pres (hpa)'].resample('1H').mean()
pres_resample_min = austin_df['pres (hpa)'].resample('1H').min()
pres_resample_max = austin_df['pres (hpa)'].resample('1H').max()
# %%

fig, (ax1, ax2) = plt.subplots(2, 1, figsize = (10,8), sharex = True)

plt.suptitle("Georgetown, TX Arctic Front December 2023: 1-Hour Temperature, Dewpoint Temperature,", fontsize = 14)

start = '2022-12-22 12:00:00+00:00'
end = '2022-12-26 00:00:00+00:00'

ax1.plot(temp_resample_min[start:end], color = 'deeppink', alpha = 0.35, linewidth = 1.5, label = 'Temperature 1-hour Mean')
ax1.plot(temp_resample_mean[start:end], color = 'deeppink', alpha = 0.65, linewidth = 1.5, label = 'Temperature 1-hour Mean')
ax1.plot(temp_resample_max[start:end], color = 'deeppink', alpha = 0.1, linewidth = 1.5, label = 'Temperature 1-hour Mean')
ax1.plot(dpt_resample_min[start:end], color = 'green', alpha = 0.35, linewidth = 1.5, label = 'Dewpoint Temp 1-hour Minimum')
ax1.plot(dpt_resample_mean[start:end], color = 'green', alpha = 0.65, linewidth = 1.5, label = 'Dewpoint Temp 1-hour Minimum')
ax1.plot(dpt_resample_max[start:end], color = 'green', alpha = 0.1, linewidth = 1.5, label = 'Dewpoint Temp 1-hour Minimum')
ax1.set_ylim(-5, 60)
ax1.grid(which = 'minor', linestyle = '-', alpha = 0.25)
ax1.grid(which = 'major', linestyle = '-', alpha = 0.5)
ax1.set_ylabel('Temperature [$\mathrm{F}$]', fontsize = 10)
ax1.grid(alpha=0.5)

ax7 = ax1.twinx()

ax7.plot(pres_resample_mean[start:end], color = 'dodgerblue', alpha = 0.5, linewidth = 1.5, label = 'Pressure 1-hour Mean')
ax7.set_title("Wind Gust, Wind Speed Averages, and 3-Hour Maximum Wind Vectors", fontsize = 14)
ax7.set_ylim(965,1030)
ax7.set_ylabel('Pressure (hPa)', fontsize = 10)


# Now for the second subplot
ax8 = ax2.twinx()

ax2.quiver(austin_df[start:end][0::38].index, y, u_wind_resample[start:end], v_wind_resample[start:end], width=.002, label='Wind Vectors')
ax2.grid(which = 'major', linestyle = '-', alpha = 0.5)
ax2.grid(which = 'minor', linestyle = '-', alpha = 0.25)
ax2.set_ylabel('Predominent 3-Hour Winds', fontsize = 10)
ax2.tick_params(left = False, labelleft=False)
ax2.set_xlabel('Date')
majorformattor = mdates.DateFormatter('%H:%M %b-%d')
ax2.get_xaxis().set_major_formatter(majorformattor)
fig.autofmt_xdate(rotation = 45, ha = 'center')
ax2.get_xaxis().set_minor_locator(mdates.HourLocator(12))

ax8.plot(wind_gust_resample[start:end], "c^", alpha = 0.9, label = 'Max Wind Gust')
ax8.plot(wind_resample_max[start:end], color = 'purple', alpha = 0.5, linewidth=1, label = 'Max 3H Wind Speed')
ax8.plot(wind_resample_mean[start:end], color = 'mediumspringgreen', alpha = 0.5, linewidth=1, label = 'Mean 3H Wind Speed')
ax8.set_ylabel('Wind Speed (m/s)')

# Making my own legend
t_min = mlines.Line2D([], [], color='deeppink', alpha=0.35, 
                           linestyle='-', linewidth=3,
                           label='Temperature Minimum                 ')
t_mean = mlines.Line2D([], [], color='deeppink', alpha=0.65, 
                           linestyle='-', linewidth=3, 
                           label='Temperature Mean                ')
t_max = mlines.Line2D([], [], color='deeppink', alpha=1, 
                           linestyle='-', linewidth=3,
                           label='Temperature Maximum                ')
dpt_min = mlines.Line2D([], [], color='green', alpha=0.35, 
                           linestyle='-', linewidth=3,
                           label='Dewpoint Temperature Minimum ')
dpt_mean = mlines.Line2D([], [], color='green', alpha=0.65, 
                           linestyle='-', linewidth=3,
                           label='Dewpoint Temperature Mean ')
dpt_max = mlines.Line2D([], [], color='green', alpha=1, 
                           linestyle='-', linewidth=3,
                           label='Dewpoint Temperature Maximum')
pres_mean = mlines.Line2D([], [], color='dodgerblue', alpha=0.35, 
                           linestyle='-', linewidth=3,
                           label='Pressure Mean                             ')
wind_spd_max = mlines.Line2D([], [], color='purple', alpha=1, 
                           linestyle='-', linewidth=3,
                           label='Wind Speed Maximum           ')
wind_spd_mean = mlines.Line2D([], [], color='mediumspringgreen', alpha=0.65, 
                           linestyle='-', linewidth=3,
                           label='Wind Speed Mean                        ')
wind_gust = mlines.Line2D([], [], marker='^', color='c', linestyle='None', alpha = 0.9,
                          markersize=6, label = 'Max Wind Gust                            ')
wind_vectors = mlines.Line2D([], [], marker='>', color='black', linestyle='None', alpha = 1,
                          markersize=6, label = 'Wind Vectors                               ')
space = mlines.Line2D([], [],color='None', linestyle='-', alpha = 1, label = '                                               ')

# Formatting my legend
fig.legend(bbox_to_anchor=(0.1, 0.015), framealpha=1, edgecolor='white', fontsize = 9,
           facecolor='white',handles=[t_max, t_mean, t_min], 
           loc='upper left',ncols=3) 
fig.legend(bbox_to_anchor=(0.1, -0.01), framealpha=1, edgecolor='None', fontsize = 9,
           facecolor='white',handles=[dpt_max, dpt_mean, dpt_min], 
           loc='upper left',ncols=4)
fig.legend(bbox_to_anchor=(0.1, -0.035), framealpha=1, edgecolor='white', fontsize = 9,
           facecolor='white',handles=[pres_mean, wind_spd_max, wind_spd_mean], 
           loc='upper left',ncols=3)
fig.legend(bbox_to_anchor=(0.1, -0.060), framealpha=1, edgecolor='white', fontsize = 9,
           facecolor='white',handles=[wind_gust, wind_vectors, space], 
           loc='upper left',ncols=3)


fig.set_facecolor('lightgray')
plt.tight_layout()
# %%
