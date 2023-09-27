### Forecast 5
### Jessica Meyer
due Sept 27

**Forecast Explanation:**
The forecast values for this week and the following week were determined using several methods and my best estimate based on such methods. Initially, I found the number of occurances in which the flow was less than 75 cfs through the period of record (1989 to present - my preference since the new climatological range is from 1990 through 2020) to determine frequency vs our current year. Then I looked at the monthly trend of frequency, i.e. how many of the prior occurrances were within the first ten days of the month, the second ten day block, and then the third ten day block of september. From there I became a bit more specific, using 5cfs ranges, beginning at 75cfs and decreasing until a 'nan' appeared. I printed all of these values and the daily data for the previous week (sept 17 - sept 23) to compare them. 


I also made several forloops for flow that was less than 100 or greater than 200:
1. sept 17 through sept 24 after 2010
1. sept 25 through sept 30 after 2010
2. oct 1 through oct 7 after 2010
   
      *...and used numpy to find the means of several conditional statements from sept 24 through sept 30:*

1. flow was less than 70
2. flow was less than 60
3. flow was less than 50
   
      *...lastly, I used numpy to find the mean of this past week from sept 17 through sept 23.*

#### Reflection
The homework was a bit challenging this week but managed to make it through. I am a bit confused how to create an empty array or how to use the append method. I understand the concept of what im doing but the syntax is a bit confusing, i.e., when x = np.append() is useful vs np.append(previousarray, newarray).

#### Assignment
##### Question 2
Dimensions of the 5 year array: (1826, 4)
Average daily flow over the 5 year period: 325.19 cfs

##### Question 3
The first 5 daily values within the flow_daily array:
1. 19,353,600 cubic feet
2. 19,008,000 cubic feet
3. 18,748,800 cubic feet
4. 18,316,800 cubic feet
5. 18,316,800 cubic feet
Total flow during 5 year period: 51,303,464,640 cubic feet

##### Question 4
[2.01500000e+03 1.00000000e+00 3.03451613e+02]
 [2.01500000e+03 2.00000000e+00 4.29500000e+02]
 [2.01500000e+03 3.00000000e+00 1.41806452e+03]
 [2.01500000e+03 4.00000000e+00 9.86966667e+01]
 [2.01500000e+03 5.00000000e+00 1.21548387e+02]

##### Question 5
I really struggled with the last for loop of the assignment. I also was unsure of what time the markdown file and code were due today, Wed sept 27. 