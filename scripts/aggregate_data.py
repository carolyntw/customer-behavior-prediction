import os
import pandas as pd

# function to aggregate CSV files into one
def aggregate_csv_files(csv_dir):
    all_data = []
    
    for file_name in os.listdir(csv_dir):
        if file_name.endswith(".csv"):
            file_path = os.path.join(csv_dir, file_name)
            df = pd.read_csv(file_path)
            all_data.append(df)

    combined_df = pd.concat(all_data, ignore_index=True)
    return combined_df

# aggregate the processed CSV files
combined_data = aggregate_csv_files("./data/processed")
combined_data.to_csv("./data/aggregated_flight_data.csv", index=False)
