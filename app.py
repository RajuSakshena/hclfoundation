import os
import streamlit as st
from hcl import run_hcl_scraper

st.set_page_config(
    page_title="HCL Foundation Opportunities Scraper",
    layout="centered"import os
import streamlit as st
import pandas as pd
from hcl import run_hcl_scraper

st.set_page_config(
    page_title="HCL Foundation Opportunities Scraper",
    layout="centered"
)

st.title("HCL Foundation – Opportunities Scraper")
st.write(
    "This app runs the existing HCL scraper and generates an Excel file "
    "based on keyword-matched verticals."
)

if st.button("Run Scraper"):
    with st.spinner("Running scraper..."):
        run_hcl_scraper()

    output_path = "output/hcl_opportunities.xlsx"

    if os.path.exists(output_path):
        st.success("Scraping completed successfully.")

        # Display Excel as table in Streamlit
        try:
            df = pd.read_excel(output_path)
            st.subheader("Preview of Scraped Data")
            st.dataframe(df)  # Interactive table
        except Exception as e:
            st.error(f"Error displaying Excel table: {e}")

        # Download button
        with open(output_path, "rb") as f:
            st.download_button(
                label="Download Excel File",
                data=f,
                file_name="hcl_opportunities.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    else:
        st.error("Scraper ran, but Excel file was not generated.")

)

st.title("HCL Foundation – Opportunities Scraper")
st.write(
    "This app runs the existing HCL scraper and generates an Excel file "
    "based on keyword-matched verticals."
)

if st.button("Run Scraper"):
    with st.spinner("Running scraper..."):
        run_hcl_scraper()

    output_path = "output/hcl_opportunities.xlsx"

    if os.path.exists(output_path):
        st.success("Scraping completed successfully.")

        with open(output_path, "rb") as f:
            st.download_button(
                label="Download Excel File",
                data=f,
                file_name="hcl_opportunities.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    else:
        st.error("Scraper ran, but Excel file was not generated.")
