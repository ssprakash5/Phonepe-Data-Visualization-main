# Phonepe-Data-Visualization
![Phonepe data visualization](https://github.com/srisuryaprakash55/Phonepe-Data-Visualization/assets/139371882/a363f4c4-8c0c-4e77-b811-fc8aafa648f8)

Phonepe Pulse Data Visualization and Exploration
Project Overview
The Phonepe Pulse Data Visualization and Exploration project aim to extract, transform, and visualize data from the Phonepe Pulse Github repository. The solution involves scripting for data extraction, data transformation using Python and Pandas, storing transformed data in a MySQL database, and creating an interactive dashboard using Streamlit and Plotly for insightful data visualization.

Technologies Used
GitHub Cloning
Python
Pandas
MySQL
mysql-connector-python
Streamlit
Plotly
Domain
Fintech

Problem Statement
The Phonepe Pulse Github repository contains a vast amount of data related to various metrics and statistics. The goal is to extract, process, and visualize this data in a user-friendly manner. The solution should include data extraction, transformation, database insertion, and the creation of a live geo visualization dashboard using Streamlit and Plotly. The dashboard should provide valuable insights and allow users to interact with different facts and figures.

Approach
Data Extraction:

Clone the GitHub repository using scripting to fetch the data.
Store the data in a suitable format, such as CSV or JSON.
Data Transformation:

Use Python and Pandas to manipulate and preprocess the data.
Clean the data, handle missing values, and transform it into a suitable format.
Database Insertion:

Use the "mysql-connector-python" library to connect to a MySQL database.
Insert the transformed data into the database using SQL commands.
Dashboard Creation:

Utilize Streamlit and Plotly to create an interactive and visually appealing dashboard.
Use Plotly's geo map functions for displaying data on a map.
Implement multiple dropdown options for users to select different facts and figures.
Data Retrieval:

Connect to the MySQL database using "mysql-connector-python."
Fetch data into a Pandas dataframe for dynamic updates to the dashboard.
Deployment:

Ensure the solution is secure, efficient, and user-friendly.
Thoroughly test the solution and deploy the dashboard publicly.
Results
The result of this project will be a live geo visualization dashboard displaying insights from the Phonepe Pulse Github repository. The dashboard will feature at least 10 dropdown options for users to select different facts and figures. Data will be stored in a MySQL database for efficient retrieval, and the dashboard will dynamically update with the latest data. Users can access the dashboard from a web browser, facilitating easy navigation and providing valuable insights for data analysis and decision-making.

Getting Started
Follow these steps to set up and run the project:

Clone the GitHub repository.
Install required Python libraries using pip install -r requirements.txt.
Set up a MySQL database and update connection details in the code.
Run the data extraction and transformation scripts.
Insert the transformed data into the MySQL database.
Run the Streamlit app for the live geo visualization dashboard.
For detailed instructions, refer to the documentation in the repository.
