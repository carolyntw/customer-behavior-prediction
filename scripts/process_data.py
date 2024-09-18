import os
import pandas as pd

# function to process .asc files and convert to CSV
def process_asc_files(download_dir, processed_dir):
    # ensure the processed directory exists
    if not os.path.exists(processed_dir):
        os.makedirs(processed_dir)

    # loop through all files in the directory
    for file_name in os.listdir(download_dir):
        if file_name.endswith(".asc"):  # ensure we only process .asc files
            file_path = os.path.join(download_dir, file_name)
            print(f"Processing {file_name}")

            # load the .asc file into a pandas DataFrame, using '|' as the delimiter
            df = pd.read_csv(file_path, sep="|", header=None)

            # check how many columns the file has
            num_columns = len(df.columns)
            print(f"Number of columns in {file_name}: {num_columns}")

            # handle 28-column files
            if num_columns == 28:
                df.columns = [
                    "Carrier Reported Date of Data: Year", 
                    "Carrier Reported Date of Data: Month", 
                    "Carrier Reported Origin Airport: Alpha Code", 
                    "Origin Airport: Unique Numeric Code", 
                    "Origin Airport: World Area Code", 
                    "Origin Airport: City Name", 
                    "Carrier Reported Destination Airport: Alpha Code", 
                    "Destination Airport: Numeric Code", 
                    "Destination Airport: World Area Code", 
                    "Destination Airport: City Name", 
                    "Carrier Reported Carrier: Alpha Code", 
                    "Carrier Reported Carrier: Entity Code", 
                    "Carrier Group Code", 
                    "Distance", 
                    "Service Class", 
                    "Aircraft Type: Group", 
                    "Aircraft Type: Type", 
                    "Aircraft Type: Configuration", 
                    "Departures Performed", 
                    "Departures Scheduled", 
                    "Available Capacity: Payload Pounds", 
                    "Available Seats", 
                    "Passengers Transported", 
                    "Freight Transported", 
                    "Mail Transported", 
                    "Ramp – Ramp in minutes", 
                    "Airborne – in minutes", 
                    "Carrier’s World Area Code"
                ]
                print(f"{file_name} has 28 columns.")
                
            # handle 29-column files
            elif num_columns == 29:
                df.columns = [
                    "Carrier Reported Date of Data: Year", 
                    "Carrier Reported Date of Data: Month", 
                    "Carrier Reported Origin Airport: Alpha Code", 
                    "Origin Airport: Unique Numeric Code", 
                    "Origin Airport: World Area Code", 
                    "Origin Airport: City Name", 
                    "Carrier Reported Destination Airport: Alpha Code", 
                    "Destination Airport: Numeric Code", 
                    "Destination Airport: World Area Code", 
                    "Destination Airport: City Name", 
                    "Carrier Reported Carrier: Alpha Code", 
                    "Carrier Reported Carrier: Entity Code", 
                    "Carrier Group Code", 
                    "Distance", 
                    "Service Class", 
                    "Aircraft Type: Group", 
                    "Aircraft Type: Type", 
                    "Aircraft Type: Configuration", 
                    "Departures Performed", 
                    "Departures Scheduled", 
                    "Available Capacity: Payload Pounds", 
                    "Available Seats", 
                    "Passengers Transported", 
                    "Freight Transported", 
                    "Mail Transported", 
                    "Ramp – Ramp in minutes", 
                    "Airborne – in minutes", 
                    "Carrier’s World Area Code", 
                    "Carrier’s World Area Code (Duplicate)"
                ]
                print(f"{file_name} has 29 columns.")

            else:
                print(f"Unexpected number of columns ({num_columns}) in {file_name}, skipping.")
                continue  # Skip this file if the column count doesn't match 28 or 29

            # filter data for American Airlines ('AA')
            df_filtered = df[df['Carrier Reported Carrier: Alpha Code'] == 'AA']

            if df_filtered.empty:
                print(f"No data found for Carrier_Alpha == 'AA' in {file_name}")
            else:
                # calculate load factor (assuming available seats are not zero)
                df_filtered['Load_Factor_Calculated'] = df_filtered.apply(
                    lambda row: row['Passengers Transported'] / row['Available Seats'] if row['Available Seats'] > 0 else None,
                    axis=1
                )

            # save the processed data
            processed_file_path = os.path.join(processed_dir, f"processed_{file_name.replace('.asc', '.csv')}")
            df_filtered.to_csv(processed_file_path, index=False)
            print(f"Processed data saved to {processed_file_path}")

# specify the download and processed directories
download_dir = "./data/downloads"
processed_dir = "./data/processed"

# call the function to process the .asc files and save them to the processed directory
process_asc_files(download_dir, processed_dir)
