import streamlit as st
import pandas as pd


# year and filepath
file_path = {
    '2018': 'data/2018-v269-16052023-EU MRV Publication of information.csv',
    '2019': 'data/2019-v215-30062023-EU MRV Publication of information.csv',
    '2020': 'data/2020-v191-20072023-EU MRV Publication of information.csv',
    '2021': 'data/2021-v169-02082023-EU MRV Publication of information.csv',
    '2022': 'data/2022-v35-05082023-EU MRV Publication of information.csv',
}

# Calculate the pivot table and return it as a DataFrame
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

# Streamlit UI
st.title("EU MRV Data Analysis")


# Slider for year
selected_year = st.select_slider('Select a range of years', options=['2018', '2019', '2020', '2021', '2022'])

# Show the plot for the selected year
st.header(selected_year)

# Read the CSV file
df = pd.read_csv(file_path[selected_year])

# Calculate the pivot table
pivoted_df = calculate_pivot_table(df)

# Show the pivoted data is checkbox is ticked
if st.checkbox('Show pivoted tabular data for ' + selected_year + ''):
    # Display the pivoted data
    st.dataframe(pivoted_df)

# Bar chart
st.bar_chart(pivoted_df)

