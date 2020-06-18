# Surf's Up
## Project Overview

W. Avy is a potential investor for a potential new ice cream shop on Oahu. Using weather data from Oahu, pulled from nine different stations from January 1st 2010 to August 23rd 2017, we will try to provide W. Avy with all the information we can, and hopefully convince him that this investment would be a good opportunity.

NOTE: All code for the project can be found in [climate_analysis.ipynb](https://github.com/Alyssa-CG/Module9-surfs_up/blob/master/climate_analysis.ipynb)

## Resources
* Data
    * [SQLite database](https://github.com/Alyssa-CG/Module9-surfs_up/blob/master/hawaii.sqlite)

* Software
    * Python 3.7
    * Jupyter Notebook 6.0.3
    * pandas v 1.0.1
    * matplotlib v 3.1.3
    * sqlalchemy v 1.3.13

## Findings

We have found that June generally has less rainfall and higer temperatures than December. There is also slightly less spread in these values for June, as shown by the lower standard deviations. The images below show the summary statistics pulled for June and December, across the years 2010 to 2017.

#### June 2010-2017 Precipitation (Units) and Temperatures (Farenheit)
![June weather](https://github.com/Alyssa-CG/Module9-surfs_up/blob/master/Figures/june_weather.png)

#### December 2010-2016* Precipitation (Units) and Temperatures (Farenheit)
###### * Note that weather data ends August 2017
![December weather](https://github.com/Alyssa-CG/Module9-surfs_up/blob/master/Figures/december_weather.png)

This information suggests that an ice cream shop on Oahu may do better in June than in December.

## Recommendations

* It would be valuable to conduct further analyses as it is worth considering:  
    * Average precipitation throughout the year
    * Average temperatures throughout the year
    * Whether the stations are located in different areas of Oahu and represent any differences in rainfall and temperature in those areas
        * This is potentially feasible as the database does include columns for latitude, longtitude and elevation
    * Frequency of tropical storms, hurricanes and other potential natural disasters.
    * How different rain and weather conditions on the other Hawaiian islands can influence the location (does it have to be on Oahu? If on Oahu are there times of the year when persons are more likely to visit the other islands? Does that affect tourism to all islands including Oahu? Can we consider a location near to a means of inter-island travel?)
    * Any data on locations of other successful businesses on Oahu (are there high traffic local areas or are tourist locations like Waikiki beach more likely to be successful?)

For further visualization, precipitation scores and temperatures were each grouped by month, averaged, and plotted on line graphs to quickly and easily show W. Avy the averages throughout the year, based on the January 2010 to August 2017 data he provided. 

![Precipitation chart](https://github.com/Alyssa-CG/Module9-surfs_up/blob/master/Figures/Average%20Precipitation.png)

![Temperatures chart](https://github.com/Alyssa-CG/Module9-surfs_up/blob/master/Figures/Average%20Temperatures.png)

These charts above show the spikes that occur in rainfall in March and December when the temperatures are also at some of their lowest values. These may be the most difficult times to sell ice cream. The second chart also shows that July to September are the warmest months, so, despite a small increase in rainfall in July, these months may be the most likely to be sucessful or profitable for the ice cream shop. 

Based on theses analyses only, I would recommend that W. Avy agree to open the ice cream shop with an opening date between April to June, immediately before peak ice-cream selling season, but be prepared for some fluctuations in ice cream sales throughout the year.