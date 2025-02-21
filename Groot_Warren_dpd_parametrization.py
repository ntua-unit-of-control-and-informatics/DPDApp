import numpy as np
import pandas as pd
import streamlit as st

st.header("Parametrization using Groot De Warren")

st.text("This is supposed to be the parametrization for DPD models"
        "The reference is 'Dissipative particle dynamics: "
        "Bridging the gap between atomistic and mesoscopic simulation'"
        "J. Chem. Phys. DOI:10.1063/1.474784")

with st.form("my_form"):
    st.write("System Properties")
    temperature = st.text_input("System temperature in DPD units usually 1.0 [float]")
    density = st.text_input("System number density in DPD units usually 3.0 [float]")
    number = st.text_input("Number of DPD bead types in the system [integer]")
    submitted = st.form_submit_button("Submit")

    if submitted:
        try:
            number = int(number)
            if number > 0:
                st.write("You have given the integer", number)
                st.session_state['number'] = number
            else:
                st.write("The integer should be greater than zero")
        except ValueError:
            st.write("This is not an integer")

        try:
            temperature = float(temperature)
            if temperature > 0:
                st.write("You have given the float", temperature)
                st.session_state['temperature'] = temperature
            else:
                st.write("The temperature should be greater than zero")
        except ValueError:
            st.write("This is not a temperature")

        try:
            density = float(density)
            if density > 0:
                st.write("You have given the float", density)
                st.session_state['density'] = density
            else:
                st.write("The density should be greater than zero")
        except ValueError:
            st.write("This is not a density")

if 'number' in st.session_state and 'temperature' in st.session_state and 'density' in st.session_state:
    with st.form("second_form"):

        df = pd.DataFrame(
            [
                {"command": "st.selectbox", "rating": 4, "is_widget": True},
                {"command": "st.balloons", "rating": 5, "is_widget": False},
                {"command": "st.time_input", "rating": 3, "is_widget": True},
            ]
        )

        edited_df = st.data_editor(df)
        #st.dataframe(df)
        submit = st.form_submit_button("Submit")

        if submit:
            st.dataframe(edited_df)

if st.button("Reset"):
    if 'number' in st.session_state:
        del st.session_state['number']
    if 'temperature' in st.session_state:
        del st.session_state['temperature']
    if 'density' in st.session_state:
        del st.session_state['density']

    st.rerun()
