import numpy as np
import pandas as pd
import streamlit as st

st.header("Parametrization using Groot De Warren")

st.text("This is supposed to be the parametrization for DPD models ")

with st.form("my_form"):
    st.write("Inside the form")
    number = st.text_input("Give the number of elements it must be an integer")
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

if 'number' in st.session_state:
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
    st.rerun()
