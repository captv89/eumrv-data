import plotly.express as px
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="EU MRV Data Analysis by Ship Type",
    page_icon="💭",
)

# year and filepath
file_path = {
    '2018': 'data/2018-v269-16052023-EU MRV Publication of information.csv',
    '2019': 'data/2019-v215-30062023-EU MRV Publication of information.csv',
    '2020': 'data/2020-v191-20072023-EU MRV Publication of information.csv',
    '2021': 'data/2021-v169-02082023-EU MRV Publication of information.csv',
    '2022': 'data/2022-v35-05082023-EU MRV Publication of information.csv',
}

# Combine all the data into one DataFrame
all_data = pd.DataFrame()
for year in file_path:
    data = pd.read_csv(file_path[year])
    data['Year'] = year
    all_data = pd.concat([all_data, data])


# Main Page
# Title and description
st.title('EU MRV Data Analysis by Ship Type')
st.write('Total figures per year by Ship Type.')

# Create a sidebar filter for vessel types
selected_vessel_types = st.multiselect(
    'Select Vessel Type(s)', data['Ship type'].unique())


# Filter the data based on selected vessel types
filtered_data = all_data[all_data['Ship type'].isin(selected_vessel_types)]

# Divider
st.divider()

# Header
st.header('Total CO₂ Emissions by Ship Type')
# Create a bar plot using plotly express
co2_fig = px.bar(filtered_data, 
                    x='Reporting Period', 
                    y='Total CO₂ emissions [m tonnes]',
                    color='Ship type')

# Display the plot
st.plotly_chart(co2_fig)

# Divider
st.divider()

# Header
st.header('Total Fuel Consumption by Ship Type')
# Create a area plot using plotly express
fuel_fig = px.bar(filtered_data,
                    x='Reporting Period',
                    y='Total fuel consumption [m tonnes]',
                    color='Ship type')

# Display the plot
st.plotly_chart(fuel_fig)

# Divider
st.divider()

# Header
st.header('Total Sailing Time by Ship Type')
# Create a area plot using plotly express
sailing_fig = px.bar(filtered_data,
                    x='Reporting Period',
                    y='Annual Total time spent at sea [hours]',
                    color='Ship type')

# Display the plot
st.plotly_chart(sailing_fig)