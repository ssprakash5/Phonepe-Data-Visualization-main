import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
df_indian_states = pd.read_csv("/content/statedf1.csv")
# Read the District vs. Amount CSV file
district_data = pd.read_csv("/content/namedf.csv")

# Read additional CSV files
data_district = pd.read_csv("/content/namedf.csv")
data_state = pd.read_csv("/content/statedf1.csv")

# Streamlit App
st.title('Phonepe Visualization: Indian States and Districts vs. Amount')

# Indian States vs. Amount visualization
st.subheader('Indian States vs. Amount')
fig_states = px.scatter_geo(
    df_indian_states,
    lat='Latitude',
    lon='Longitude',
    size='amount',
    color='amount',
    color_continuous_scale='Viridis',
    projection='natural earth',
    title='Indian States vs. Amount',
    size_max=50,
    template='plotly_dark',
    hover_name='state',
    opacity=0.8,
    labels={'amount': 'Amount (in Billions)'}
)
fig_states.update_geos(
    showcountries=True,
    countrycolor='black',
    countrywidth=1.5
)
st.plotly_chart(fig_states)

# District vs. Amount visualization
st.subheader('District vs. Amount')
fig_districts = px.scatter_geo(
    district_data,
    lat='Latitude',
    lon='Longitude',
    size='count',
    color='count',
    color_continuous_scale='Viridis',
    projection='natural earth',
    title='District vs. Amount',
    size_max=50,
    template='plotly_dark',
    hover_name='name',
    opacity=0.8,
    labels={'count': 'count (in Billions)'}
)
fig_districts.update_geos(
    showcountries=True,
    countrycolor='black',
    countrywidth=1.5
)
st.plotly_chart(fig_districts)

# Plotly Bubble Box Chart for Districts
st.subheader("District vs. count")
fig_district = px.scatter_geo(
    data_district,
    lat='Latitude',
    lon='Longitude',
    size='count',
    color='count',
    color_continuous_scale='Viridis',
    projection='natural earth',
    title='District vs. Amount',
    size_max=50,
    template='plotly_dark',
    hover_name='name',
    opacity=0.8,
    labels={'count'}
)

fig_district.update_geos(
    showcountries=True,
    countrycolor='black',
    countrywidth=1.5
)

st.plotly_chart(fig_district)

# Plotly Bubble Box Chart for States
st.subheader("Indian States vs. count")
fig_state = px.scatter_geo(
    data_state,
    lat='Latitude',
    lon='Longitude',
    size='count',
    text='state',
    color='count',
    color_continuous_scale='Viridis',
    projection='natural earth',
    title='Indian States vs. Amount',
    size_max=50,
    template='plotly_dark',
    hover_name='state',
    opacity=0.8,
    labels={'count': 'count'}
)

fig_state.update_geos(
    showcountries=True,
    countrycolor='black',
    countrywidth=1.5
)

st.plotly_chart(fig_state)

#Read the CSV file
district_data = pd.read_csv("/content/converted_data_map_transaction.csv")

# Streamlit App Title
st.title("District Visualization")

# State selection dropdown
states = district_data['state'].unique()
selected_state = st.selectbox("Select a State", states)

# Filter data based on selected state
filtered_data = district_data[district_data['state'] == selected_state]

# Plot bar graph for selected state's districts
st.subheader(f"Bar Graph for {selected_state}")
fig_selected_state = px.bar(
    filtered_data,
    x='name',
    y='amount',
    title=f"Amount for {selected_state} Districts",
    labels={'amount': 'Amount'}
)
st.plotly_chart(fig_selected_state)

# Example 4: Name vs Amount Bar Plot
df1=pd.read_csv("/content/converted_data-aggregated_transaction.csv")

# Streamlit App Title
st.title("Name vs Amount Visualization")

# Bar Plot
st.subheader("Name vs Amount")
fig_name_amount = plt.figure()
x = df1['name']
y = df1['amount']
plt.bar(x, y)
plt.xlabel('Name')
plt.ylabel('Amount')
plt.title('Name vs Amount')

# Rotate x-axis labels
plt.xticks(rotation=45, ha='right')

# Display legend with smaller font size
plt.legend(['Amount'], fontsize='small')

# Show the plot in Streamlit app
st.pyplot(fig_name_amount)

df2=pd.read_csv("/content/converted_data_agg_user.csv")

# Streamlit App Title
st.title("Brand vs User Aggregation Visualization")

# Brand vs Percentage Horizontal Bar Plot
st.subheader("Brand vs Percentage")
fig_brand_percentage = plt.figure()
X_percentage = df2['percentage']
Y_brand = df2['brand']
plt.barh(Y_brand, X_percentage)
plt.xlabel('Percentage')
plt.ylabel('Brand')
plt.title('Brand vs Percentage')

# Show the plot in Streamlit app
st.pyplot(fig_brand_percentage)

# Example 6: Brand vs Count Horizontal Bar Plot
st.subheader("Brand vs Count")
fig_brand_count = plt.figure()
X_count = df2['count']
plt.barh(Y_brand, X_count)
plt.xlabel('Count')
plt.ylabel('Brand')
plt.title('Brand vs Count')

# Show the plot in Streamlit app
st.pyplot(fig_brand_count)

# Example 7: State vs Registered User Horizontal Bar Plot
st.subheader("State vs Registered User")
fig_state_registered_user = plt.figure()
X_registered_user = df2['registeredUser']
Y_state = df2['state']
plt.barh(Y_state, X_registered_user)
plt.xlabel('Registered User')
plt.ylabel('State')
plt.tight_layout()
plt.legend(['Registered User'], fontsize='small')
plt.title('State vs Registered User')

# Show the plot in Streamlit app
st.pyplot(fig_state_registered_user)

df4=pd.read_csv("/content/converted_data map user.csv")

# Streamlit App Title
st.title("App Opens vs State Visualization")

# App Opens vs State Horizontal Bar Plot
st.subheader("App Opens vs State")
fig_app_opens_state = plt.figure()
X_app_opens = df4['appOpens']
Y_state_app_opens = df4['state']
plt.barh(Y_state_app_opens, X_app_opens)
plt.xlabel('App Opens')
plt.ylabel('State')
plt.title('App Opens vs State')

# Show the plot in Streamlit app
st.pyplot(fig_app_opens_state)

df5 = pd.read_csv("/content/converted_data_top_transaction.csv")

# Streamlit App Title
st.title("Top 10 Transaction Amounts by Entity Name")

# Group by entityName and sum the amounts
district = df5.groupby('entityName').sum()
district.reset_index(inplace=True)

# Check if 'state' and 'type' columns exist before dropping them
columns_to_drop = ['year', 'state', 'type', 'responseTimestamp']
columns_to_drop = [col for col in columns_to_drop if col in district.columns]
district = district.drop(columns_to_drop, axis=1)

# Select only rows with numeric entityName (assuming pincode)
pincode_rows = district[district['entityName'].str.match(r'^\d+$')]
top_10_rows = pincode_rows.nlargest(10, 'amount')

# Display the top 10 rows in Streamlit app
st.subheader("Top 10 Transaction Amounts by Entity Name")
st.table(top_10_rows)

import pandas as pd
import streamlit as st

df3 = pd.read_csv("/content/converted_data_top_transaction.csv")

# Print the column names to check the actual column names
print("Column Names:", df3.columns)

# Streamlit App Title
st.title("Top 10 Transaction Amounts by District Name")

# Check if 'entityName' column exists in the DataFrame
if 'entityName' in df3.columns:
    # Group by entityName and sum the amounts
    district = df3.groupby(['entityName']).sum()
    district.reset_index(inplace=True)

    # Check if the columns exist before dropping them
    columns_to_drop = ['year', 'state', 'type', 'responseTimestamp']
    columns_to_drop = [col for col in columns_to_drop if col in district.columns]
    district.drop(columns_to_drop, axis=1, inplace=True)

    # Check if 'level_0' and 'index' columns exist before dropping them
    if 'level_0' in district.columns:
        district.drop(['level_0'], axis=1, inplace=True)

    if 'index' in district.columns:
        district.drop(['index'], axis=1, inplace=True)

    # Display the top 10 rows in Streamlit app
    st.subheader("Top 10 Transaction Amounts by District Name")
    top_10_districts = district.nlargest(10, 'amount')
    st.table(top_10_districts)
else:
    st.error("Column 'entityName' not found in the DataFrame.")


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ... (your other data loading and processing code)

# Additional sections or information can be added as per your requirements.

# Example 11: Total Amount by State for Each Year in a Streamlit App
df3 = pd.read_csv("/content/converted_data_map_transaction.csv")

# Streamlit App Title
st.title("Total Amount by State for Each Year")

# Group the data by year and state, and calculate the total amount for each group
year_state_amount = df3.groupby(['year', 'state'])['amount'].sum().reset_index()

# Plot a bar graph for each year in the Streamlit app
years = df3['year'].unique()
for year in years:
    data_for_year = year_state_amount[year_state_amount['year'] == year]

    # Set seaborn style for better aesthetics
    sns.set(style="whitegrid")

    # Create a bar plot with different colors
    plt.figure(figsize=(10, 6))
    sns.barplot(x='state', y='amount', data=data_for_year, palette='viridis')

    plt.xlabel('State')
    plt.ylabel('Amount')
    plt.title(f'Total Amount by State for {year}')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.tight_layout()

    # Show the plot for each year in the Streamlit app
    st.pyplot(plt)
