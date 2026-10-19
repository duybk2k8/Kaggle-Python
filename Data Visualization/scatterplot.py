import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns
print("Setup Complete")

# Path of the file to read
insurance_filepath = "../input/insurance.csv"

# Read the file into a variable insurance_data
insurance_data = pd.read_csv(insurance_filepath)

sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'])

#regression line (line that best fits the data)
sns.regplot(x=insurance_data['bmi'], y=insurance_data['charges'])
#add third variable by color
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'], hue=insurance_data['smoker'])

#2 regression lines
sns.lmplot(x="bmi", y="charges", hue="smoker", data=insurance_data)

#categorical scatter plot
#chia smoker thành 2 loại luôn
sns.swarmplot(x=insurance_data['smoker'],
              y=insurance_data['charges'])
