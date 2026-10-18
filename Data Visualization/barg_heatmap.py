import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns
print("Setup Complete")

# Path of the file to read
flight_filepath = "../input/flight_delays.csv"

# Read the file into a variable flight_data
flight_data = pd.read_csv(flight_filepath, index_col="Month")

# Set the width and height of the figure
plt.figure(figsize=(10,6))

# Add title
plt.title("Average Arrival Delay for Spirit Airlines Flights, by Month")

# Bar chart showing average arrival delay for Spirit Airlines flights by month
sns.barplot(x=flight_data.index, y=flight_data['NK']) #flight_data.index chính là month 
# k dc dùng flight_data['Month'] => cột month dùng để index (đã dc tách và k ph cột thường nữa)
# Add label for vertical axis
plt.ylabel("Arrival delay (in minutes)")


# Set the width and height of the figure
plt.figure(figsize=(14,7))

# Add title
plt.title("Average Arrival Delay for Each Airline, by Month")

# Heatmap showing average arrival delay for each airline by month
sns.heatmap(data=flight_data, annot=True)
# This ensures that the values for each cell appear on the chart
# bỏ ra thì sẽ bỏ hết số từ các ô (annot điền số vào các ô)
# Add label for horizontal axis
plt.xlabel("Airline")