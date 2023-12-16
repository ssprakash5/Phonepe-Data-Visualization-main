import pandas as pd
import os
import json

# Specify the base directory containing state folders, each with year folders
base_dir = r"D:/phonepe data/data/aggregated/transaction/country/india/state"

# Specify the output directory for CSV files on the D drive
output_dir = r"D:/phonepe_csv_output1"  # Change this path to the desired output directory on the D drive

# Create an empty list to store the converted data
converted_data = []

# Loop through state folders
for state_folder in os.listdir(base_dir):
    state_dir = os.path.join(base_dir, state_folder)

    # Check if it's a directory
    if os.path.isdir(state_dir):
        # Loop through year folders (2018 to 2023)
        for year in range(2018, 2024):
            year_dir = os.path.join(state_dir, str(year))

            # Check if the year folder exists
            if os.path.exists(year_dir):
                # List all JSON files in the year folder
                json_files = [f for f in os.listdir(year_dir) if f.endswith('.json')]

                # Loop through JSON files and convert to CSV format
                for json_file in json_files:
                    # Load JSON data
                    with open(os.path.join(year_dir, json_file), 'r') as json_data:
                        data = json.load(json_data)
                        transaction_data = data['data']['transactionData']

                    # Extract required data and create rows in the desired format
                    for entry in transaction_data:
                        row = {
                            'year': year,
                            'state': state_folder,
                            'from': data['data']['from'],
                            'to': data['data']['to'],
                            'name': entry['name'],
                            'type': entry['paymentInstruments'][0]['type'],
                            'count': entry['paymentInstruments'][0]['count'],
                            'amount': entry['paymentInstruments'][0]['amount'],
                            'responseTimestamp': data['responseTimestamp']
                        }
                        converted_data.append(row)

# Create a DataFrame from the converted data
df = pd.DataFrame(converted_data)

# Create output directory for CSV files if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Specify the CSV output file path on the D drive (customize the filename)
csv_file = os.path.join(output_dir, "converted_data.csv")

# Save DataFrame as CSV
df.to_csv(csv_file, index=False)

print(f'Converted data saved to {csv_file}')

import pandas as pd
import os
import json

# Specify the base directory containing state folders, each with year folders
base_dir = r"D:/phonepe data/data/aggregated/transaction/country/india/state"

# Specify the output directory for CSV files on the D drive
output_dir = r"D:/phonepe_csv_output1"  # Change this path to the desired output directory on the D drive

# Create an empty list to store the converted data
converted_data = []

# Loop through state folders
for state_folder in os.listdir(base_dir):
    state_dir = os.path.join(base_dir, state_folder)

    # Check if it's a directory
    if os.path.isdir(state_dir):
        # Loop through year folders (2018 to 2023)
        for year in range(2018, 2024):
            year_dir = os.path.join(state_dir, str(year))

            # Check if the year folder exists
            if os.path.exists(year_dir):
                # List all JSON files in the year folder
                json_files = [f for f in os.listdir(year_dir) if f.endswith('.json')]

                # Loop through JSON files and convert to CSV format
                for json_file in json_files:
                    # Load JSON data
                    with open(os.path.join(year_dir, json_file), 'r') as json_data:
                        data = json.load(json_data)
                        transaction_data = data['data']['transactionData']

                    # Extract required data and create rows in the desired format
                    for entry in transaction_data:
                        row = {
                            'year': year,
                            'state': state_folder,
                            'from': data['data']['from'],
                            'to': data['data']['to'],
                            'name': entry['name'],
                            'type': entry['paymentInstruments'][0]['type'],
                            'count': entry['paymentInstruments'][0]['count'],
                            'amount': entry['paymentInstruments'][0]['amount'],
                            'responseTimestamp': data['responseTimestamp']
                        }
                        converted_data.append(row)

# Create a DataFrame from the converted data
df = pd.DataFrame(converted_data)

# Create output directory for CSV files if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Specify the CSV output file path on the D drive (customize the filename)
csv_file = os.path.join(output_dir, "converted_data.csv")

# Save DataFrame as CSV
df.to_csv(csv_file, index=False)

print(f'Converted data saved to {csv_file}')

import pandas as pd
import os
import json

# Specify the base directory containing state folders, each with year folders
base_dir = r"D:/phonepe data/data/map/transaction/hover/country/india/state"

# Specify the output directory for CSV files on the D drive
output_dir = r"D:/phonepe_csv_map_transaction"  # Change this path to the desired output directory on the D drive

# Create an empty list to store the converted data
converted_data = []

# Loop through state folders
for state_folder in os.listdir(base_dir):
    state_dir = os.path.join(base_dir, state_folder)

    # Check if it's a directory
    if os.path.isdir(state_dir):
        # Loop through year folders (2018 to 2023)
        for year in range(2018, 2024):
            year_dir = os.path.join(state_dir, str(year))

            # Check if the year folder exists
            if os.path.exists(year_dir):
                # List all JSON files in the year folder
                json_files = [f for f in os.listdir(year_dir) if f.endswith('.json')]

                # Loop through JSON files and convert to CSV format
                for json_file in json_files:
                    # Load JSON data
                    with open(os.path.join(year_dir, json_file), 'r') as json_data:
                        data = json.load(json_data)
                        hover_data_list = data['data']['hoverDataList']

                        # Extract data and create rows in the desired format
                        for entry in hover_data_list:
                            name = entry['name']
                            metrics = entry['metric']
                            for metric in metrics:
                                row = {
                                    'year': year,
                                    'state': state_folder,
                                    'name': name,
                                    'type': metric['type'],
                                    'count': metric['count'],
                                    'amount': metric['amount'],
                                    'responseTimestamp': data['responseTimestamp']
                                }
                                converted_data.append(row)

# Create a DataFrame from the converted data
df = pd.DataFrame(converted_data)

# Create output directory for CSV files if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Specify the CSV output file path on the D drive (customize the filename)
csv_file = os.path.join(output_dir, "converted_data.csv")

# Save DataFrame as CSV
df.to_csv(csv_file, index=False)

print(f'Converted data saved to {csv_file}')

import pandas as pd
import os
import json

# Specify the base directory containing state folders, each with year folders
base_dir = r"D:/phonepe data/data/top/transaction/country/india/state"

# Specify the output directory for CSV files on the D drive
output_dir = r"D:/phonepe_csv_top_transaction1"  # Change this path to the desired output directory on the D drive

# Create an empty list to store the converted data
converted_data = []

# Loop through state folders
for state_folder in os.listdir(base_dir):
    state_dir = os.path.join(base_dir, state_folder)

    # Check if it's a directory
    if os.path.isdir(state_dir):
        # Loop through year folders (2018 to 2023)
        for year in range(2018, 2024):
            year_dir = os.path.join(state_dir, str(year))

            # Check if the year folder exists
            if os.path.exists(year_dir):
                # List all JSON files in the year folder
                json_files = [f for f in os.listdir(year_dir) if f.endswith('.json')]

                # Loop through JSON files and convert to CSV format
                for json_file in json_files:
                    # Load JSON data
                    with open(os.path.join(year_dir, json_file), 'r') as json_data:
                        data = json.load(json_data)

                        # Extract data from 'districts' and create rows in the desired format
                        for district_entry in data['data']['districts']:
                            row = {
                                'year': year,
                                'state': state_folder,
                                'entityName': district_entry['entityName'],
                                'type': district_entry['metric']['type'],
                                'count': district_entry['metric']['count'],
                                'amount': district_entry['metric']['amount'],
                                'responseTimestamp': data['responseTimestamp']
                            }
                            converted_data.append(row)

                        # Extract data from 'pincodes' and create rows in the desired format
                        for pincode_entry in data['data']['pincodes']:
                            row = {
                                'year': year,
                                'state': state_folder,
                                'entityName': pincode_entry['entityName'],
                                'type': pincode_entry['metric']['type'],
                                'count': pincode_entry['metric']['count'],
                                'amount': pincode_entry['metric']['amount'],
                                'responseTimestamp': data['responseTimestamp']
                            }
                            converted_data.append(row)

# Create a DataFrame from the converted data
df = pd.DataFrame(converted_data)

# Create output directory for CSV files if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Specify the CSV output file path on the D drive (customize the filename)
csv_file = os.path.join(output_dir, "converted_data.csv")

# Save DataFrame as CSV
df.to_csv(csv_file, index=False)

print(f'Converted data saved to {csv_file}')

import pandas as pd
import os
import json

# Specify the base directory containing state folders, each with year folders
base_dir = r"D:/phonepe data/data/top/transaction/country/india/state"

# Specify the output directory for CSV files on the D drive
output_dir = r"D:/phonepe_csv_top_transaction1"  # Change this path to the desired output directory on the D drive

# Create an empty list to store the converted data
converted_data = []

# Loop through state folders
for state_folder in os.listdir(base_dir):
    state_dir = os.path.join(base_dir, state_folder)

    # Check if it's a directory
    if os.path.isdir(state_dir):
        # Loop through year folders (2018 to 2023)
        for year in range(2018, 2024):
            year_dir = os.path.join(state_dir, str(year))

            # Check if the year folder exists
            if os.path.exists(year_dir):
                # List all JSON files in the year folder
                json_files = [f for f in os.listdir(year_dir) if f.endswith('.json')]

                # Loop through JSON files and convert to CSV format
                for json_file in json_files:
                    # Load JSON data
                    with open(os.path.join(year_dir, json_file), 'r') as json_data:
                        data = json.load(json_data)

                        # Extract data from 'districts' and create rows in the desired format
                        for district_entry in data['data']['districts']:
                            row = {
                                'year': year,
                                'state': state_folder,
                                'entityName': district_entry['entityName'],
                                'type': district_entry['metric']['type'],
                                'count': district_entry['metric']['count'],
                                'amount': district_entry['metric']['amount'],
                                'responseTimestamp': data['responseTimestamp']
                            }
                            converted_data.append(row)

                        # Extract data from 'pincodes' and create rows in the desired format
                        for pincode_entry in data['data']['pincodes']:
                            row = {
                                'year': year,
                                'state': state_folder,
                                'entityName': pincode_entry['entityName'],
                                'type': pincode_entry['metric']['type'],
                                'count': pincode_entry['metric']['count'],
                                'amount': pincode_entry['metric']['amount'],
                                'responseTimestamp': data['responseTimestamp']
                            }
                            converted_data.append(row)

# Create a DataFrame from the converted data
df = pd.DataFrame(converted_data)

# Create output directory for CSV files if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Specify the CSV output file path on the D drive (customize the filename)
csv_file = os.path.join(output_dir, "converted_data.csv")

# Save DataFrame as CSV
df.to_csv(csv_file, index=False)

print(f'Converted data saved to {csv_file}')

import pandas as pd
import os
import json

# Specify the base directory containing state folders, each with year folders
base_dir = r"D:/phonepe data/data/top/transaction/country/india/state"

# Specify the output directory for CSV files on the D drive
output_dir = r"D:/phonepe_csv_top_transaction1"  # Change this path to the desired output directory on the D drive

# Create an empty list to store the converted data
converted_data = []

# Loop through state folders
for state_folder in os.listdir(base_dir):
    state_dir = os.path.join(base_dir, state_folder)

    # Check if it's a directory
    if os.path.isdir(state_dir):
        # Loop through year folders (2018 to 2023)
        for year in range(2018, 2024):
            year_dir = os.path.join(state_dir, str(year))

            # Check if the year folder exists
            if os.path.exists(year_dir):
                # List all JSON files in the year folder
                json_files = [f for f in os.listdir(year_dir) if f.endswith('.json')]

                # Loop through JSON files and convert to CSV format
                for json_file in json_files:
                    # Load JSON data
                    with open(os.path.join(year_dir, json_file), 'r') as json_data:
                        data = json.load(json_data)

                        # Extract data from 'districts' and create rows in the desired format
                        for district_entry in data['data']['districts']:
                            row = {
                                'year': year,
                                'state': state_folder,
                                'entityName': district_entry['entityName'],
                                'type': district_entry['metric']['type'],
                                'count': district_entry['metric']['count'],
                                'amount': district_entry['metric']['amount'],
                                'responseTimestamp': data['responseTimestamp']
                            }
                            converted_data.append(row)

                        # Extract data from 'pincodes' and create rows in the desired format
                        for pincode_entry in data['data']['pincodes']:
                            row = {
                                'year': year,
                                'state': state_folder,
                                'entityName': pincode_entry['entityName'],
                                'type': pincode_entry['metric']['type'],
                                'count': pincode_entry['metric']['count'],
                                'amount': pincode_entry['metric']['amount'],
                                'responseTimestamp': data['responseTimestamp']
                            }
                            converted_data.append(row)

# Create a DataFrame from the converted data
df = pd.DataFrame(converted_data)

# Create output directory for CSV files if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Specify the CSV output file path on the D drive (customize the filename)
csv_file = os.path.join(output_dir, "converted_data.csv")

# Save DataFrame as CSV
df.to_csv(csv_file, index=False)

print(f'Converted data saved to {csv_file}')

import pandas as pd
import os
import json

# Specify the base directory containing state folders, each with year folders
base_dir = r"D:/phonepe data/data/top/user/country/india/state"

# Specify the output directory for CSV files on the D drive
output_dir = r"D:/phonepe_csv_top_user"  # Change this path to the desired output directory on the D drive

# Create an empty list to store the converted data
converted_data = []

# Loop through state folders
for state_folder in os.listdir(base_dir):
    state_dir = os.path.join(base_dir, state_folder)

    # Check if it's a directory
    if os.path.isdir(state_dir):
        # Loop through year folders (2018 to 2023)
        for year in range(2018, 2024):
            year_dir = os.path.join(state_dir, str(year))

            # Check if the year folder exists
            if os.path.exists(year_dir):
                # List all JSON files in the year folder
                json_files = [f for f in os.listdir(year_dir) if f.endswith('.json')]

                # Loop through JSON files and convert to CSV format
                for json_file in json_files:
                    # Load JSON data
                    with open(os.path.join(year_dir, json_file), 'r') as json_data:
                        data = json.load(json_data)

                        # Extract data from 'districts' and create rows in the desired format
                        for district_entry in data['data']['districts']:
                            row = {
                                'year': year,
                                'state': state_folder,
                                'name': district_entry['name'],
                                'registeredUsers': district_entry['registeredUsers'],
                                'responseTimestamp': data['responseTimestamp']
                            }
                            converted_data.append(row)

                        # Extract data from 'pincodes' and create rows in the desired format
                        for pincode_entry in data['data']['pincodes']:
                            row = {
                                'year': year,
                                'state': state_folder,
                                'name': pincode_entry['name'],
                                'registeredUsers': pincode_entry['registeredUsers'],
                                'responseTimestamp': data['responseTimestamp']
                            }
                            converted_data.append(row)

# Create a DataFrame from the converted data
df = pd.DataFrame(converted_data)

# Create output directory for CSV files if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Specify the CSV output file path on the D drive (customize the filename)
csv_file = os.path.join(output_dir, "converted_data.csv")

# Save DataFrame as CSV
df.to_csv(csv_file, index=False)

print(f'Converted data saved to {csv_file}')



