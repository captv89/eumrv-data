import streamlit as st

st.set_page_config(
    page_title="Welcome!",
    page_icon="👋",
)

st.write("# Lets Explore EU MRV data! 📈")


st.markdown(
    """
    This is a [Streamlit](https://streamlit.io/) powered app showing the analysis of the EU MRV dataset. \n
    Data sourced directly from the European Union's official website. \n
    Data is available from 2018 to 2022. *(collected on 4th August 2023)* \n

    Data source: [European Union's official website](https://data.europa.eu/data/datasets/co2-emissions-data?locale=en) \n
    Source code: [GitHub](https://github.com/captv89/eumrv-data/) \n
    Portfolio: [@CaptV89](https://captv.ovh/) \n
    """
)
