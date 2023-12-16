import pandas as pd
import mysql.connector

# Define MySQL connection settings
# Define MySQL connection settings
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "123",
    "database": "Phonepe"
}

# Define the path to your CSV file
csv_file_path = "D:/phonepe_csv_output1/converted_data-aggregated_transaction.csv"

# Define the MySQL table name
table_name = 'New_Aggregated_transaction'

# Create a MySQL table based on the CSV structure
create_table_query = f'''
CREATE TABLE {table_name} (
    year INT,
    state VARCHAR(255),
    from_date DOUBLE,
    to_date DOUBLE,
    name VARCHAR(255),
    type VARCHAR(255),
    count INT,
    amount DECIMAL(12, 2),
    responseTimestamp DOUBLE
);
'''

# Load CSV data into a DataFrame
df = pd.read_csv(csv_file_path)

# Establish a MySQL database connection
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Execute the CREATE TABLE query
cursor.execute(create_table_query)

# Insert data from the DataFrame into the MySQL table
for row in df.itertuples(index=False):
    if row.amount <= 9999999999.99:  # Adjust the limit as needed
        insert_query = f'''
        INSERT INTO {table_name} (year, state, from_date, to_date, name, type, count, amount, responseTimestamp)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        '''
        cursor.execute(insert_query, row)
    else:
        print(f"Skipping row with out-of-range 'amount': {row}")

# Commit the changes and close the connection
conn.commit()
conn.close()

import pandas as pd
import mysql.connector

# Define MySQL connection settings
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "123",
    "database": "Phonepe"
}

# Define the path to your new CSV file
csv_file_path = "D:\phonepe_csv_map_transaction\converted_data_map_transaction.csv"

# Define the MySQL table name
table_name = 'map_transaction'

# Create a MySQL table based on the new CSV structure
create_table_query = f'''
CREATE TABLE {table_name} (
    year INT,
    state VARCHAR(255),
    name VARCHAR(255),
    type VARCHAR(255),
    count INT,
    amount DECIMAL(18, 4),  # Adjusted precision and scale
    responseTimestamp DOUBLE
);
'''

# Load CSV data into a DataFrame
df = pd.read_csv(csv_file_path)

# Establish a MySQL database connection
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Execute the CREATE TABLE query
cursor.execute(create_table_query)

# Insert data from the DataFrame into the MySQL table
for row in df.itertuples(index=False):
    # Convert the 'amount' value from scientific notation to decimal and round to 4 decimal places
    amount_decimal = round(float(row.amount), 4)

    insert_query = f'''
    INSERT INTO {table_name} (year, state, name, type, count, amount, responseTimestamp)
    VALUES (%s, %s, %s, %s, %s, %s, %s);
    '''
    cursor.execute(insert_query, (row.year, row.state, row.name, row.type, row.count, amount_decimal, row.responseTimestamp))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data inserted into the MySQL table successfully.")

import pandas as pd
import mysql.connector

# Define MySQL connection settings
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "123",
    "database": "Phonepe"
}

# Define the path to your new CSV file
csv_file_path = "D:/phonepe_csv_map_user/converted_data map user.csv"

# Define the MySQL table name
table_name = 'map_user'

# Create a MySQL table based on the new CSV structure
create_table_query = f'''
CREATE TABLE {table_name} (
    year INT,
    state VARCHAR(255),
    hoverData VARCHAR(255),  -- Changed data type to VARCHAR(255)
    registeredUser INT,
    appOpens INT,
    responseTimestamp DOUBLE
);
'''

# Load CSV data into a DataFrame
df = pd.read_csv(csv_file_path)

# Establish a MySQL database connection
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Execute the CREATE TABLE query
cursor.execute(create_table_query)

# Insert data from the DataFrame into the MySQL table
for row in df.itertuples(index=False):
    year, state, hoverData, registeredUser, appOpens, responseTimestamp = row

    insert_query = f'''
    INSERT INTO {table_name} (year, state, hoverData, registeredUser, appOpens, responseTimestamp)
    VALUES (%s, %s, %s, %s, %s, %s);
    '''
    cursor.execute(insert_query, (year, state, hoverData, registeredUser, appOpens, responseTimestamp))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data inserted into the MySQL table successfully.")

import pandas as pd
import mysql.connector

# Define MySQL connection settings
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "123",
    "database": "Phonepe"
}

# Define the path to your new CSV file
csv_file_path = "D:\phonepe_csv_top_transaction1\converted_data_top_transaction.csv"

# Define the MySQL table name
table_name = 'top_transaction'

# Load CSV data into a DataFrame
df = pd.read_csv(csv_file_path)

# Replace NaN values with None for SQL
df = df.where(pd.notna(df), None)

# Find the maximum length of 'amount' in the DataFrame
max_amount_length = df['amount'].apply(lambda x: len(str(x))).max()

# Establish a MySQL database connection
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Create a MySQL table with 'amount' column adjusted based on the maximum length
create_table_query = f'''
CREATE TABLE {table_name} (
    year INT,
    state VARCHAR(255),
    entityName VARCHAR(255),
    type VARCHAR(255),
    count INT,
    amount DECIMAL({max_amount_length + 3}, 2),
    responseTimestamp DOUBLE
);
'''

# Execute the CREATE TABLE query
cursor.execute(create_table_query)

# Insert data from the DataFrame into the MySQL table
for row in df.itertuples(index=False):
    insert_query = f'''
    INSERT INTO {table_name} (year, state, entityName, type, count, amount, responseTimestamp)
    VALUES (%s, %s, %s, %s, %s, %s, %s);
    '''
    cursor.execute(insert_query, (
        row.year,
        row.state,
        row.entityName,
        row.type,
        row.count,
        row.amount,
        row.responseTimestamp
    ))

# Commit the changes and close the connection
conn.commit()
conn.close()

import pandas as pd
import mysql.connector

# Define MySQL connection settings
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "123",
    "database": "Phonepe"
}

# Define the path to your new CSV file
csv_file_path = "D:/phonepe_csv_aggregated_user/converted_data_agg_user.csv"

# Define the MySQL table name
table_name = 'New_Aggregated_user'

# Create a MySQL table based on the new CSV structure
create_table_query = f'''
CREATE TABLE {table_name} (
    year INT,
    state VARCHAR(255),
    registeredUser INT,
    appOpens DECIMAL(10, 2),  -- Updated data type for appOpens
    brand VARCHAR(255),
    count INT,
    percentage DECIMAL(10, 6),
    responseTimestamp DOUBLE
);
'''

# Load CSV data into a DataFrame
df = pd.read_csv(csv_file_path)

# Establish a MySQL database connection
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Execute the CREATE TABLE query
cursor.execute(create_table_query)

# Insert data from the DataFrame into the MySQL table with error handling
for row in df.itertuples(index=False):
    try:
        insert_query = f'''
        INSERT INTO {table_name} (year, state, registeredUser, appOpens, brand, count, percentage, responseTimestamp)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        '''
        cursor.execute(insert_query, row)
    except mysql.connector.Error as err:
        print(f"Error inserting data: {err}")
        print(f"Problematic row: {row}")

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data inserted into the MySQL table successfully.")
