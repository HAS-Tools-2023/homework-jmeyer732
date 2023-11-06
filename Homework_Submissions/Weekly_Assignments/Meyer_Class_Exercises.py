#------------------------------------------------------------------------------
#----------------------TUESDAY NOV 2 IN-CLASS EXERCISES------------------------
#------------------------------------------------------------------------------
#%%
import pandas as pd
import numpy as np
import urllib
import matplotlib
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LinearRegression

#%%
### Exercise 1: 
# Given the following dataframe:
data = np.random.rand(4, 5)

# Write a function and use it to calculate the mean of every column of the dataframe
# If you have time try doing it with and without a for loop (You can either use the 
#           function inside your fo loop or put a for loop inside your function)

def column_mean(data, col_1 = 0, col_2 = 1, col_3 = 2, col_4 = 3, col_5 = 4):
      a = data[:, col_1].mean()
      b = data[:, col_2].mean()
      c = data[:, col_3].mean()
      d = data[:, col_4].mean()
      e = data[:, col_5].mean()
      return([[a,b,c,d,e]])

print(column_mean(data))

#%%
# Another function
def mean_columns(my_array):
      calc_mean = np.mean(data, axis = 0)
      return(calc_mean)

mean_columns(data)

#%%
# Another function
def column_averages(my_array):
      ncol = my_array.shape[1]  # the number of columns in my array
      col_mean = np.zeros(5) #creating a single empty array with 5 zeros
      for i in range(ncol):
            col_mean[i] = np.mean(my_array[:,i]) 
      return(col_mean)

column_averages(data)

#%%
# --------------PSEUDOCODE---------------
# define a function that can take the mean of a set of numbers and return one value
def take_mean(some_numbers):
      np.mean(some_numbers)
      return one number

# write a for loop that will loop over each column of data, take the mean and store 
#           in array that has a number for each column
for i in variable:
      make 5 zeros
      take mean and store it in the right location

#%%
# Another example and notes

def col_means(numbers): #col_means is the function name and numbers is the parameter
      means = np.mean(numbers) # variable is equal to the mean of the parameter
      return(means) # return the variable

array = np.zeros(5) # creating an array

for i in range(data.shape[1]): # for a value in the range of 1 row of data (1 row has 5 values)
      array[i] = col_means(data[:,i]) # for each value place in the created array, input the
                                      # data from all rows for each column and use the defined 
                                      # function
    
print(array)

#%% Exercise two: regression analysis
# For this exercise we will work with the
# iris dataset which is a classic and very easy
# multi-class classification dataset. 
# This dataset comes with the sklearn pacakge so we can just load it in directly. 
# It describes measurements of sepal & petal width/length for three different species of iris
d = datasets.load_iris()
iris_df = pd.DataFrame(d['data'], columns=d['feature_names'])
iris_df.index = pd.Series(
    pd.Categorical.from_codes(d.target, d.target_names),
    name='species'
)
iris_df.head()

# %%
# 1. How do you view the "unique" species in the `iris_df` index?

unique = np.unique(iris_df.index)
print(unique)

# %%
# 2. How do you "locate" only rows for the `versicolor` species?

versicolor = iris_df.loc['versicolor']
setosa = iris_df.loc['setosa']
virginica = iris_df.loc['virginica']

print(versicolor)
# %%
# 3. Calculate the mean for every column of the dataframe grouped by species. 

# One way
iris_df.groupby(['species']).mean()

# Another way
iris_df.groupby(iris_df.index).mean()

# %%
# 4. Make a scatter plot of the `sepal length (cm)` versus the `petal length (cm)` 
#           for the `versicolor`` species?

# first grab out just the rows you want to plot then use scatter plot function 
#           to plot the columns you want (plotting notes)

ax = plt.figure(figsize=(10,10))

versicolor_df = pd.DataFrame(iris_df.loc['versicolor'])

ax = versicolor_df.plot.scatter(
      x ='sepal length (cm)',  y = 'petal length (cm)', marker = '*', 
      color = 'magenta', s = 50, grid = 'black')
plt.title('Versicolor sepal vs. petal length (cm)')

#%%
# Another version
plt.scatter(versicolor_df['sepal length (cm)'], versicolor_df['petal length (cm)'])

#%% 
# Laura's version of Question 4
ax = plt.axes()
ax.scatter(iris_df.loc['versicolor']['sepal length (cm)'], 
           iris_df.loc['versicolor']['petal length (cm)'], marker = 'o')
plt.ylabel('Petal Length (cm)')
plt.xlabel('Sepal Length (cm)')
plt.show()

#%%
# An extra trial scatter plot of Question 4 to see if I could do it differently
ax = plt.figure(figsize=(5,5))
x = (versicolor_df[0:25]['sepal length (cm)'])
y = (versicolor_df[0:25]['petal length (cm)'])
plt.scatter(x, y, marker = '*', color ='blue')

x = (versicolor_df[26:50]['sepal length (cm)'])
y = (versicolor_df[26:50]['petal length (cm)'])
plt.scatter(x, y, marker = '*', color ='magenta')

plt.grid(alpha = 0.5)
plt.xlim(4.5,7.5, 0.5)
plt.ylim(2.5,5.5,0.5)
plt.legend()
plt.show()

#%%
# 5.  Do the same plot for `setosa` and `virginica` all on the same figure. Color 
#           them 'tomato', 'darkcyan', and 'darkviolet', respectively. 
#           (BONUS: Try to write the code so you only need to type each iris name 
#           one time)

# repeat what you did in question 4, three times

ax = iris_df.loc['versicolor'].plot(kind="scatter", x="sepal length (cm)",y="petal length (cm)", color='tomato', label='Versicolor', marker='*',s=40)
iris_df.loc['setosa'].plot(kind = 'scatter', x="sepal length (cm)",y="petal length (cm)", color='darkcyan', label = 'Setosa',marker='*',s=40, ax=ax)
iris_df.loc['virginica'].plot(kind = 'scatter', x="sepal length (cm)",y="petal length (cm)", color='darkviolet', label='Virginica',marker='*',s=40, ax=ax)
ax.set_xlabel("Sepal Length (cm)")
ax.set_ylabel("Petal Length (cm)")
ax.set_xlim(4,8)
ax.set_ylim(0.8,7.1)
ax.grid(alpha=0.5)
ax.legend(loc='lower right')
ax.set_title('Sepal vs. Petal Length of Versicolor, Setosa, & Virginica')
plt.show()

#%%
# Laura's version of Question 5
ax = plt.axes()
iris_type='versicolor'
ax.scatter(
      iris_df.loc[iris_type]['sepal length (cm)'],
iris_df.loc[iris_type]['petal length (cm)'], marker = 'o', 
color = 'tomato', label = 'versicolor')

iris_type = 'setosa'
ax.scatter(
      iris_df.loc[iris_type]['sepal length (cm)'],
iris_df.loc[iris_type]['petal length (cm)'], marker = 'o', 
color = 'darkcyan', label = iris_type)

iris_type = 'virginica'
ax.scatter(
      iris_df.loc[iris_type]['sepal length (cm)'],
iris_df.loc[iris_type]['petal length (cm)'], marker = 'o', 
color = 'darkviolet', label = iris_type)

ax.set_xlabel('sepal length (cm)')
ax.set_ylabel('petal length (cm)')
ax.set_title(iris_type)
ax.legend()

#%%
# 6. Write a function that will do 'ax.scatter' for a given iris type and desired 
#           color and use this to function to modify the code you make in 5

# no for loop is needed, the function should have two arguments and you will call 
#           it 3 times. copy your code from question 5 down here and replace your
#           ax.scatter calls with your function.

def my_function(species_type, species_color):
      ax = iris_df.loc[species_type].plot(
            kind='scatter', x="sepal length (cm)",y="petal length (cm)", 
            color = species_color, label = species_type)

ax = plt.axes()
my_function(species_type = 'versicolor', species_color = 'tomato')
my_function(species_type = 'setosa', species_color = 'darkcyan')
my_function(species_type = 'virginica', species_color = 'darkviolet')
ax.set_xlabel('Sepal Length (cm)', fontsize=12)
ax.set_ylabel('Petal Length (cm)', fontsize=12)
ax.legend()


# %%
# -----------------------------------------------------------------------------
# --------------------------THURSDAY IN-CLASS EXERCISES------------------------
# -----------------------------------------------------------------------------

#%%
# Exercise 1
# modify the following to create a pandas dataframe where the column 'datetime' is a 
#           datetime object. You should do this two ways: 
# 
# (1) by modifying the read.table function arguments directly. 
# (2) keeping the read.table line I have below the same and modifying the dataframe 
#           after the fact. 
# How can you check to confirm that what you did worked? 

# PART 1
data = pd.read_table(
      'streamflow_demo.txt', sep = '\t', skiprows = 30, 
      names = ['agency_cd','site_no','datetime', 'flow', 'code'], 
      parse_dates = ['datetime'], index_col = 'datetime')

# PART 2
data['datetime'] = pd.to_datetime(data['datetime'])
data = data.set_index('datetime')

# PART 3
print(data.info())
print(data.index())
print(data.head())

#%%
# Exercise 2: 

#2.1: Read the 'daymet.csv' file in as a data frame using the 'date' column as 
#           the index and making sure to treat that column as a datetime object. 

data = pd.read_csv('daymet.csv', sep=',',skiprows=1, 
                   names=['date', 'year', 'yday', 'dayl (s)', 'prcp (mm/day)', 
                          'srad(W/m^2)', 'swe (kg/m^2)', 'tmax (deg c)', 
                          'tmin (deg c)', 'vp (Pa)'], 
                          parse_dates =['date'], index_col=['date'])

print(data)

#%%
# Laura's example of reading in data
data1 = pd.read_csv('daymet.csv', index_col='date')
print(data1)

#%%
#2.2: Explore this dataset and report what variables it contains, what date ranges 
#           are covered and the frequency of the data. 

print(data.columns)
# The variables include (objects):
#      year 
#     day of year in seconds
#     precipitation per day in millimeters
#     shortwave radiation in watts per meter squared
#     swe (kg/m^2)  --> im not sure what this variable was
#     maximum temperature in Celsius
#     minimum temperature in Celsius
#     vapor pressure in Pascals

print(data.index.min())
print(data.index.max())
# The date ranges it contains are:   1992-09-25 00:00:00 to 2022-09-25 00:00:00

print(data.max().describe)
print(data)
# The frequency of collected data was daily.

#%%
#2.3  Make a scatter plot of day length (dayl) vs maximum temperature. Fit a 
#           trend line 

# Making a scatterplot of day length vs maximum temperature
ax = plt.axes(facecolor = 'lightgray')
x = data['dayl (s)']/ (60*60)
y = data['tmax (deg c)'] * (9/5) + 32
ax.scatter(x, y, color = 'red', s = 5, marker = '+')
plt.xlabel('Day Length (Hours)')
plt.ylabel('Maximum Temperature (Fahrenheit)')

# Fitting a trendline
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), color = 'yellow')

plt.legend()
plt.show()

#%%
#2.4 Make a plot with lines for the monthly average of `tmax` for all 
#           months after Jan 2015.  Add shading to the plot extending 
#           to the monthly minimum and maximum of `tmax` for the same 
#           period.

# Hint - Use the pandas resample function for datetime objects and the
#            plt.fill type for the shading. 

# Dataframe for data after Jan 2015
data_after_2015 = (data[(data.year >= 2015)])

import datetime as dt
date1 = pd.Series(pd.date_range('1992-09-25', periods = 10950)) 
df = pd.DataFrame(dict(date_given = date1)) 
df['month'] = df['date_given'].dt.month
print(df)

array = np.asarray(df['month'])
data.insert(1, 'month_of_date', array)
print(data)

#%%
data_after_2015 = (data[(data.year >= 2015)])

# (1) average SWR
average_swr = pd.DataFrame(data_after_2015.groupby(['month_of_date']).mean('srad(W/m^2)'))

# (2) min SWR
min_swr = pd.DataFrame(data_after_2015.groupby(['month_of_date']).min('srad(W/m^2)'))

# (3) max SWR
max_swr = pd.DataFrame(data_after_2015.groupby(['month_of_date']).max('srad(W/m^2)'))

# Making the plot
fig, (ax) = plt.subplots(1, 1, figsize=(10,10))

max_swr['srad(W/m^2)'].plot(label = 'Maximum SWR', color = 'darkviolet', linewidth = 2)
average_swr['srad(W/m^2)'].plot(label = 'Mean SWR', color = 'darkturquoise', linewidth = 2)
min_swr['srad(W/m^2)'].plot(label = 'Minimum SWR', color = 'deeppink', linewidth = 2)

plt.fill_between(max_swr.index, max_swr['srad(W/m^2)'], average_swr['srad(W/m^2)'],
    color = 'darkviolet', alpha = 0.3)
plt.fill_between(average_swr.index, average_swr['srad(W/m^2)'], min_swr['srad(W/m^2)'],
    color = 'darkturquoise', alpha = 0.3)
plt.fill_between(min_swr.index, min_swr['srad(W/m^2)'], average_swr['srad(W/m^2)']==0,
    color = 'deeppink', alpha = 0.4)

plt.xlabel('Month', fontsize=13)
plt.ylabel('Shortwave Radiation (W/m$^2$)', fontsize = 13)
plt.grid(alpha = 0.5, color = 'gray')
plt.legend()
plt.title('Average Monthly Incoming Shortwave Radiation (W/m$^2$)', fontsize = 15)



# %%
