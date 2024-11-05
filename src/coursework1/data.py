# Data preparation and understanding code
import pandas as pd

# Option 1: Load .csv file into a pandas dataframe variable and skip the first line which is blank
file = pd.read_csv("src/coursework1/dataset.csv")

# Print the first 5 rows of data
print("\nFirst 5 rows:\n")
print(file.head(5))

# Print the last 3 rows of data
print("\nLast 3 rows:\n")
print(file.tail(3))

# Print the column labels
print("\nColumn labels:\n")
print(file.columns)

# Print the column labels and data types
print("\nColumn labels, datatypes and value counts:\n")
print(file.info(verbose=True))

# Describe the data using statistical information
print("\nGeneral Statistics:\n")
print(file.describe())
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# set the display to the size of the original dataframe
pd.set_option('display.max_rows', len(file.index))
pd.set_option('display.max_columns', len(file.columns))

# Remove unnecessary columns
#Remove the column 'Request Received (Quarter)' because it can be referred by the (month) column
file=file.drop(['Request Received (Quarter)'], axis=1)
print(file.head(5))

#Remove the column 'Request Closed (Quarter)', (same reason as above)
file=file.drop(['Request Closed (Quarter)'], axis=1)
print(file.head(5))

#Merging data is not required for this dataset as all information is sufficient
#Based on the provided dataset, it appears that there are no explicit missing values or NaN entries.
#Identifying null values
#The following code is to see a count of None and NaN values in each column
print(file.isnull().sum())

#isna() to select all rows with NaN in an entire DataFrame:
nulls = file[file[['Request Closed (Year)','Request Closed (Month)']].isna()]

#Drop null values and replace null values
print(file.shape)
file['Request Closed (Year)'].fillna(0, inplace=True)
file['Request Closed (Month)'].fillna(0, inplace=True)
print(file.shape)

#Handling inconsistent values 
for col in ['Case Type', 'Status', 'Request Received (Year)', 'Request Received (Month)', 'Request Closed (Year)', 'Request Closed (Month)', 'Case Active Days at Closure', 'Case Active Days (grouped)', 'Closed on Time?', 'Reason (grouped)', 'Number of Records']:
    print(file[col].unique())

#no unique values 
#finding and dropping duplicates
file = file.drop_duplicates()
print(file.duplicated())

#Remove blank spaces
for col in ['Case Type', 'Status', 'Request Received (Year)', 'Request Received (Month)', 'Request Closed (Year)', 'Request Closed (Month)', 'Case Active Days (grouped)', 'Closed on Time?', 'Reason (grouped)']:
    print(file[col].str.strip())

#No classified data
#Check the data types of columns 
print(file.info(verbose=True))

#Simplify and clean up table
file['Closed on Time?'] = file['Closed on Time?'].replace({'Closed on Time': 'on time', 'Closed Late': 'late', 0: 'on time'})

# Save the DataFrame back to a new csv. 
file.to_csv("file_cleaned.csv", index=False)
#Exploring and understanding the data
#Create a boxplot for 'Case Active Days at Closure' because it has the most randomised data out of the other columns 
import matplotlib.pyplot as plt 
file.boxplot(column=['Case Active Days at Closure'])
plt.show()
#No need to drop or remove any of the outliers because the data is already quite spread out
#create a Histogram for 'Case Active Days at Closure'
plt.hist(file['Case Active Days at Closure'])
plt.show()
#Code challenges
#Check for outliers in other columns 
#Create a bocplot for the column 'Number of Records'
file.boxplot(column=['Number of Records'])
plt.show()
#From the boxplot we can see that there is no outliers identified as all the numbers are at 1
#Create a histogram for other columns 
#Create a histogram for the column 'Number of Records'
plt.hist(file['Number of Records'])
plt.show()
#Create a histogram for the column 'Request Received (year)'
plt.hist(file['Request Received (Year)'])
plt.show()
#Create a histogram for the column 'Request Received (Month)'
plt.hist(file['Request Received (Month)'])
plt.show()
#Create a bar chart
# Filter data for the month of May
may_data = file[file['Request Closed (Month)'] == 'May']

# Create a bar chart
plt.figure(figsize=(12, 6))
may_data.plot(x='Request Closed (Month)', y='Case Active Days at Closure', kind='bar', color='skyblue')
plt.xlabel('Request Closed (Month)', fontsize=12)
plt.ylabel('Case Active Days at Closure', fontsize=12)
plt.title('Bar Chart of Case Active Days at Closure in May', fontsize=14)
plt.show()

#Python fucntions that can be applied to other datasets 
import pandas as pd
import matplotlib.pyplot as plt

# Function to load a .csv file into a pandas dataframe variable and skip the first line which is blank
def load_data(file_path):
    return pd.read_csv(file_path)

# Function to print the first n rows of data
def print_first_n_rows(df, n):
    print(df.head(n))

# Function to print the last n rows of data
def print_last_n_rows(df, n):
    print(df.tail(n))

# Function to print the column labels
def print_column_labels(df):
    print(df.columns)

# Function to print the column labels, datatypes, and value counts
def print_column_info(df):
    print(df.info(verbose=True))

# Function to describe the data using statistical information
def describe_data(df):
    print(df.describe())

# Function to remove unnecessary columns
def remove_columns(df, columns_to_drop):
    return df.drop(columns_to_drop, axis=1)

# Function to handle null values
def handle_null_values(df, column_names, replace_value):
    for col in column_names:
        df[col].fillna(replace_value, inplace=True)
    return df

# Function to clean up table by removing blank spaces
def clean_table(df, column_names):
    for col in column_names:
        df[col] = df[col].str.strip()
    return df

# Function to simplify and clean up 'Closed on Time?' column
def clean_closed_on_time(df):
    df['Closed on Time?'] = df['Closed on Time?'].replace({'Closed on Time': 'on time', 'Closed Late': 'late', 0: 'on time'})
    return df

# Function to save the DataFrame to a new csv
def save_to_csv(df, output_file):
    df.to_csv(output_file, index=False)

# Function to create a boxplot for a specified column
def create_boxplot(df, column_name):
    df.boxplot(column=[column_name])
    plt.show()

# Function to create a histogram for a specified column
def create_histogram(df, column_name):
    plt.hist(df[column_name])
    plt.show()

# Function to create a bar chart
def create_bar_chart(df, x_column, y_column, chart_title):
    plt.bar(df[x_column], df[y_column])
    plt.xlabel(x_column, fontsize=12)
    plt.ylabel(y_column, fontsize=12)
    plt.title(chart_title, fontsize=14)
    plt.show()

# Function calls

# Load data
file_path = "/Users/tommy/github-classroom/ucl-comp0035/comp0035-cwi-TommyLau-bit/src/coursework1/FOIA Requests Performance Data.csv"
data = load_data(file_path)
