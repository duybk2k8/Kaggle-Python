# modules we'll use
import pandas as pd
import numpy as np
import seaborn as sns
import datetime

# read in our data
landslides = pd.read_csv("../input/landslide-events/catalog.csv")

# set seed for reproducibility
np.random.seed(0)

# print the first few rows of the date column
print(landslides['date'].head())

# check the data type of our date column
landslides['date'].dtype #dtype('O') => its in the object type, we have to change to datetime64 type
#==> use strftime directive => point out which parts of the date are where
# %y for 2 digit year, %Y for four digit year, %d for day, %m for month
#17-1-2007 has the format "%d-%m-%Y"
# create a new column, date_parsed, with the parsed dates
landslides['date_parsed'] = pd.to_datetime(landslides['date'], format="%m/%d/%y")
# print the first few rows
landslides['date_parsed'].head()
landslides['date_parsed'] = pd.to_datetime(landslides['Date'], infer_datetime_format=True) 
#let pd infer the arrangement
#not rcm cause inaccuracy + slow
# get the day of the month from the date_parsed column
day_of_month_landslides = landslides['date_parsed'].dt.day
day_of_month_landslides.head()

# remove na's
day_of_month_landslides = day_of_month_landslides.dropna()

# plot the day of the month
sns.distplot(day_of_month_landslides, kde=False, bins=31)
#kde là có vẽ đường cong k
#bins là số khoảng/số cột