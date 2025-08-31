import streamlit as st
from auth import validators
from db import queries

form_values = {
    "username": None,
    "password": None,
    "password_again": None
}

def signup_form():
    with st.form(key="signup-form"):

        form_values["username"] = st.text_input("Username").strip()
        form_values["password"] = st.text_input("Password", type="password").strip()
        form_values["password_again"] = st.text_input("Re-type Password", type="password").strip()

        st.html("<br>")
        col1, col2, col3 = st.columns([1, 0.7, 1])
        with col2:
            submitted = st.form_submit_button(
                "SignUp",
                type="primary",
                use_container_width=True
            )


        if submitted:
            if not all(form_values.values()):
                st.warning("⚠️ Please fill all the fields!")
                return

            if form_values["password"] != form_values["password_again"]:
                st.warning("Passwords don't match")
                return

            
            check_username, username_msg = validators.validate_username(form_values["username"])
            if not check_username:
                st.warning(username_msg)
                return
            
            check_password, password_msg = validators.validate_password(form_values["password"])
            if not check_password:
                st.warning(password_msg)
                return
            
            
            insert_data = queries.insert(form_values["username"], form_values["password"])
        
            if insert_data:
                st.balloons()
                st.success("SignUp successfull!")
            else:
                st.warning("Try again!")


            