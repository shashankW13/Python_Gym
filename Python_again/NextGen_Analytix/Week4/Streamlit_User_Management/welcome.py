import streamlit as st
from db import queries
from auth import validators, update_password, update_username, delete_account


def welcome_page():

    current_username = st.session_state.form_values.get("username", "User")
    st.title(f"Hello {current_username},")

    st.divider()

    st.markdown("## **PROFILE:**")
    st.subheader(f"Your username: {current_username}")

    st.divider()

    update_username.update_username(current_username)

    st.divider()

    update_password.update_password()

    st.divider()

    delete_account.delete_account(current_username)

        
            




    

