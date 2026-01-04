import os
import streamlit as st
import pandas as pd
from hcl import run_hcl_scraper

st.set_page_config(
    page_title="HCL Foundation Opportunities Scraper",
    layout="centered"
)

st.title("HCL Foundation – Opportunities Scraper")
st.write(
    "This app runs the existing HCL scraper, displays the results in a table, "
    "and allows downloading the Excel file."
)

output_path = "output/hcl_opportunities.xlsx"

if st.button("Run Scraper"):
    with st.spinner("Running scraper..."):
        run_hcl_scraper()

    if os.path.exists(output_path):
        st.success("Scraping completed successfully.")

        # READ EXCEL
        df = pd.read_excel(output_path)

        # SHOW TABLE
        st.subheader("Scraped Opportunities")
        st.dataframe(df, use_container_width=True)

        # DOWNLOAD OPTION
        with open(output_path, "rb") as f:
            st.download_button(
                label="Download Excel File",
                data=f,
                file_name="hcl_opportunities.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    else:
        st.error("Scraper ran, but Excel file was not generated.")
