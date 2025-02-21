import numpy as np
import pandas as pd
import streamlit as st

submit = False

st.header("Parametrization of DPD models using the Groot - De Warren approach")

st.text("This is a WebApp for the parametrization of DPD models using the Groot De Warren methodology. "
        "The reference is 'Dissipative particle dynamics: "
        "Bridging the gap between atomistic and mesoscopic simulation' "
        "J. Chem. Phys. DOI:10.1063/1.474784")

st.text("This WebApp was created by Evangelos Voyiatzis.")

with st.form("my_form"):
    st.write("System Properties")
    temperature = st.text_input("Temperature in DPD units usually 1.0 [float]")
    density = st.text_input("Number density in DPD units usually 3.0 [float]")
    number = st.text_input("Number of DPD bead types in the system [integer]")
    selected_formula = st.radio("Choose formula for cross parameters:", [r"$\rho=3.0$", r"$\rho=5.0$"])
    submitted = st.form_submit_button("Submit")

    if submitted:
        try:
            temperature = float(temperature)
            if temperature > 0:
                st.write("The temperature is:", temperature)
                st.session_state['temperature'] = temperature
            else:
                st.write("The temperature should be greater than zero")
        except ValueError:
            st.write("You have not entered a valid temperature")

        try:
            density = float(density)
            if density > 0:
                st.write("The number density is:", density)
                st.session_state['density'] = density
            else:
                st.write("The density should be greater than zero")
        except ValueError:
            st.write("You have not entered a valid density")

        try:
            number = int(number)
            if number > 0:
                st.write("The number of DPD bead types is:", number)
                st.session_state['number'] = number
            else:
                st.write("The number of DPD bead types should be greater than zero")
        except ValueError:
            st.write("You have not entered a valid number of DPD bead types")

if all(x in st.session_state for x in ['number', 'temperature', 'density']):
    with st.form("second_form"):
        st.write("Flory–Huggins parameters")

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

if submit and all(x in st.session_state for x in ['number', 'temperature', 'density']):
    with st.form("third_form"):
        st.write("DPD interaction parameters")
        st.dataframe(edited_df)

if st.button("Reset"):
    if 'number' in st.session_state:
        del st.session_state['number']
    if 'temperature' in st.session_state:
        del st.session_state['temperature']
    if 'density' in st.session_state:
        del st.session_state['density']

    st.rerun()
