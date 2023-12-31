## Homework 9
### Jessica Meyer
### due Oct 30

### Grade 8.25/9
**Code Review**
- I left comments in your code with some suggestions they all start with #LC 
Readability: 2.5/3 
    - I like the way you broke up your code into sections. Your documentation is a bit uneven though. In many cases you are lacking comments to explain what your code is doing and why. 
    - No need to write comments that document the parameters of functions. THis the reader can find for themselves. 
    - For every function you need a comment explaining what its doing. 
    - YOur variable naming conventions were good. 
Style: 3/3
    - Generally easy to follow but the big --- lines made the comments a bit hard to read. Its fine to use these to break things up at the top of a code block but I would not have multiple lines in a row this way.
Code:  2.75/3
    - Nice work your code ran perfectly for me!
    - I made some suggestions for how you could streamline things a bit. 
    - Also it was unclear to me why you had to hardcode the max and min values.

### Assignment
#### Forecast Summary
*How you generated your forecast*
      I generated my forecast by assessing the mean flow within a few days timespan for each week and multiplying the mean by 0.6 because
      the recent 2023 streamflow values have been closer in value to the 50% quantile than the 75% quantile. However, it should be noted that the quantiles I am using are with respect to the same dates but during drier years, such as 2020.

### Script Edits
*How you made your script better this week*
      I improved my script by utilizing my classmate's suggestions for organization and methods to extract dates from pandas. I also began labeling my variables with clear names so that I was not lost, nor confused, when going through my script. Lastly, I added many notes as I fixed the code so I could reference it later, and established a distinguisher for each cell because my eyes often become tired.

### Function
*What you chose to put in a function and why*
      What I chose to put into my function was attributed to the extremes within the week 1 forecast dates and the week 2 forecast dates within the recently updated climatological period of 1991 - 2020, thus, viewing more recent and relevent extremes such as drought-likely years/seasons.

### Remaining Questions
*Remaining questions you have or things you think could be better about your script but you dont know how*
      Things that could definitely be better but I am unsure how include formatting the date for each subplot so that each is rotated. I would also like to know how to plot a simple mark or star without it being a time series, or how to plot a single date marker within a time series. Lastly, I am rather confused on PEP 8 style and when to abide by what rules.