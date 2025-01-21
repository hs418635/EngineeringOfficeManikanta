# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 18:00:43 2025

@author: himan
"""
###15.1

import pandas as pd
import numpy as np

df=pd.read_excel(r"E:\RevoQuant\SAP_config_EDA\EDA15_inputFile.xlsx")
df.columns
df = df.rename(columns=lambda x: x.strip())

df['AKTIV'].unique()
df['AKTIV'].isna().sum()
df['ERDAT']

df=df[df['AKTIV'].isna()==False]


# Calculate the Date_Difference as the difference in days
df['Date_Difference'] = (df['AKTIV'] - df['ERDAT']).dt.days

# Use np.where to classify as Exception or Not an Exception based on Date_Difference
# Initialize 'Exception_Bucket' column with NaN or any default value
df['Exception_Bucket'] = np.nan

# Update rows where 'Date_Difference' < 0
df.loc[df['Date_Difference'] < 0, 'Exception_Bucket'] = 'Exception'


df=df[["/BEV1/CLANZVP", "ANLN1", "ERDAT", "AEDAT","ZUGDT","AKTIV","MCOA1","Date_Difference","Exception_Bucket"]]

df.to_csv("E:\RevoQuant\SAP_config_EDA\EDA_15_1_Execption_updated.csv",index=False)

#############################################################################################################


### 15.2
# Read the Excel file
data = pd.read_excel(r"E:\RevoQuant\SAP_config_EDA\EDA15_inputFile.xlsx")

data['Date_Difference'] = (data['AKTIV'] - data['ERDAT']).dt.days
# Filter and assign the 'Exception_Bucket' column based on whether 'AKTIV' is 

#data['Exception_Bucket'] = np.where(data['AKTIV'].isna(), "Capitalization Date Not Available", np.nan)
data['Exception_Bucket'] = data['AKTIV'].apply(lambda x: 'Capitalization Date Not Available' if pd.isnull(x) else None)

data=data[data['Exception_Bucket']=='Capitalization Date Not Available']

data=data[["/BEV1/CLANZVP", "ANLN1", "ERDAT", "AEDAT","ZUGDT","AKTIV","MCOA1","Exception_Bucket"]]

# Save the resulting DataFrame to a CSV file
data.to_csv(r"E:\RevoQuant\SAP_config_EDA\EDA_15_2_Exception_updated.csv", index=False)

###########################################################################################################

# Read the two CSV files
df1 = pd.read_csv("E:\RevoQuant\SAP_config_EDA\EDA_15_1_Execption_updated.csv")  # Replace with your first CSV file path
df2 = pd.read_csv("E:\RevoQuant\SAP_config_EDA\EDA_15_2_Exception_updated.csv")  # Replace with your second CSV file path

# Create an Excel writer object and write the DataFrames to separate sheets
with pd.ExcelWriter("E:\RevoQuant\SAP_config_EDA\EDA_15_combined_file.xlsx") as writer:
    df1.to_excel(writer, sheet_name='Exception_15.1', index=False)  # Write df1 to Sheet1
    df2.to_excel(writer, sheet_name='Exception_15.2', index=False)  # Write df2 to Sheet2

print("CSV files have been combined into an Excel file with two sheets.")














