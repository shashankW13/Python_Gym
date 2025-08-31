import streamlit as st
from auth import validators
from db import queries
import time


def login_form():
    with st.form(key="login-form"):

        st.session_state.form_values["username"] = st.text_input("Username").strip()
        st.session_state.form_values["password"] = st.text_input("Password", type="password").strip()
        st.html("<br>")
        col1, col2, col3 = st.columns([1, 0.7, 1])
        with col2:
            submitted = st.form_submit_button(
                "Login",
                type="primary",
                use_container_width=True
            )

        
        if submitted:
            if not all(st.session_state.form_values.values()):
                st.warning("Please fill all the fields!")
                return
            
            else:
                if queries.check_login_credentials(
                    st.session_state.form_values["username"], 
                    st.session_state.form_values["password"]):

                    st.balloons()
                    st.success("Login successfull!")
                    st.session_state.page = "welcome"
                    st.session_state.login_success = True
                    st.session_state.user_session = True
                    st.rerun()
                else:
                    st.error("Invalid Credentials!")

    
