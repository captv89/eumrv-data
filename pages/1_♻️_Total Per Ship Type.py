import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="EU MRV Data Analysis by Year",
    page_icon="🚢",
)

# year and filepath
file_path = {
    '2018': 'data/2018-v269-16052023-EU MRV Publication of information.csv',
    '2019': 'data/2019-v215-30062023-EU MRV Publication of information.csv',
    '2020': 'data/2020-v191-20072023-EU MRV Publication of information.csv',
    '2021': 'data/2021-v169-02082023-EU MRV Publication of information.csv',
    '2022': 'data/2022-v35-05082023-EU MRV Publication of information.csv',
}

# Calculate the pivot table and return it as a DataFrame
@st.cache_data
def calculate_pivot_table(df):
    # Create a new DataFrame to store the counts
    vessel_counts = pd.DataFrame(columns=['vessel_type', 'category', 'count'])

    # Iterate through the CII Rating categories
    for category in ['A', 'B', 'C', 'D']:
        category_counts = df[df[category] == 'Yes'].groupby('Ship type').size().reset_index()
        category_counts.columns = ['vessel_type', 'count']
        category_counts['category'] = category
        # Add the counts to the vessel_counts DataFrame
        vessel_counts = pd.concat([vessel_counts, category_counts])
        # print(result)
        
    # Sort the DataFrame by vessel type
    vessel_counts = vessel_counts.sort_values('vessel_type')

    # Pivot the data
    pivoted_df = vessel_counts.pivot_table(index='vessel_type', columns='category', values='count', aggfunc='sum', fill_value=0)
    return pivoted_df

# Calculate the co2 emission and return it as a DataFrame
@st.cache_data
def calculate_co2_emission(df):
    co2EmissionPerShipType = df.groupby('Ship type')['Total CO₂ emissions [m tonnes]'].sum()
    return co2EmissionPerShipType


# Calculate the fuel consumption and return it as a DataFrame
@st.cache_data
def calculate_fuel_consumption(df):
    fuelConsumptionPerShipType = df.groupby('Ship type')['Total fuel consumption [m tonnes]'].sum()
    return fuelConsumptionPerShipType


# Streamlit UI
st.title("EU MRV Data Analysis by Year")
st.write('Total figures per ship type by year.')

# Slider for year
selected_year = st.select_slider('Select a range of years', options=['2018', '2019', '2020', '2021', '2022'])
st.divider()

# Show the plot for the selected year
st.header(selected_year)

# Read the CSV file
df = pd.read_csv(file_path[selected_year])


# CII Ratings
st.subheader('CII Ratings')
# Calculate the pivot table
pivoted_df = calculate_pivot_table(df)

tab1_cii, tab2_cii = st.tabs(["📈 Chart", "🗃 Data"])
tab1_cii.bar_chart(pivoted_df)
tab2_cii.dataframe(pivoted_df)

# Divider
st.divider()

# Co2 Emissions
st.subheader('Co2 Emissions')

# Calculate the co2 emission
co2_emission_df = calculate_co2_emission(df)

tab1_co2, tab2_co2 = st.tabs(["📈 Chart", "🗃 Data"])
tab1_co2.bar_chart(co2_emission_df)
tab2_co2.dataframe(co2_emission_df)

# Divider
st.divider()

# Co2 Emissions
st.subheader('Fuel Consumption')

# Calculate the co2 emission
fuel_consumption_df = calculate_fuel_consumption(df)

tab1_fuel, tab2_fuel = st.tabs(["📈 Chart", "🗃 Data"])
tab1_fuel.bar_chart(fuel_consumption_df)
tab2_fuel.dataframe(fuel_consumption_df)
