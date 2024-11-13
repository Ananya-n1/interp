import streamlit as st
import pandas as pd


st.title("Torque Value Finder at t = 5 seconds")
uploaded_file = 'InterpolationTest.xlsx'

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)
        df.columns = ["time", "Powertrain 1 - torque MZ (torque) (N⋅m)"] 
        st.write("Data from uploaded file:")
        st.write(df)
        if df.isnull().values.any():
            st.warning("Warning: The data contains missing values. Please check your data.")
        else:
            df.set_index("time", inplace=True)
            df = df.reindex(df.index.union([5])).sort_index() 
            df_interpolated = df.interpolate(method='index')

            torque_at_5 = df_interpolated.loc[5, "Powertrain 1 - torque MZ (torque) (N⋅m)"]

            # Display the result
            if not pd.isna(torque_at_5):
                st.success(f"The estimated torque value at time = 5 seconds is: {torque_at_5:.2f} N⋅m")
            else:
                st.error("Could not estimate a torque value at time = 5 seconds.")
    except Exception as e:
        st.error(f"An error occurred: {e}") 