# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 11:15:23 2024

@author: IST221.1
"""

import pandas as pd
import os

# Directory path containing the CSV files
directory = "C:/Users/IST221.1/Downloads"

# List all CSV files in the specified directory
csv_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.csv')]

# Combine all CSV files into one DataFrame
combined_df = pd.concat([pd.read_csv(file) for file in csv_files], ignore_index=True)

# Write the combined DataFrame to a new CSV file
combined_df.to_csv(os.path.join(directory, 'combined_data.csv'), index=False)

print("CSV files have been successfully combined into 'combined_data.csv'")