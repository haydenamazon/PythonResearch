import pandas as pd
import os

directory = "C:/Users/IST221.1/Downloads"
csv_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.csv')]
combined_df = pd.concat([pd.read_csv(file) for file in csv_files], ignore_index=True)

#Writes combined csv files as "combined_data"
combined_df.to_csv(os.path.join(directory, 'combined_data.csv'), index=False)

print("CSV files have been successfully combined into 'combined_data.csv'")
