import streamlit as st
from db import queries
from auth import login, signup, forgot_password
import welcome
import time

queries.create_table_users()

st.html("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #2e003e, #1f1c2c, #3a0ca3);
            color: white;
        }
    </style>
""")

if "form_values" not in st.session_state:
    st.session_state.form_values = {
        "username": None,
        "password": None,
    }

if "page" not in st.session_state:
    st.session_state.page = "home"

if "login_success" not in st.session_state:
    st.session_state.login_success = False

if "user_session" not in st.session_state:
    st.session_state.user_session = False


def home_page():
    st.session_state.page = "home"
    clear_form_values()
    st.session_state.login_success = False
    st.session_state.update_success = False

def login_page():
    st.session_state.page = "login"

def signup_page():
    st.session_state.page = "signup"

def clear_form_values():
    st.session_state.form_values.clear()


if st.session_state.page == "home":
    st.html("<h1 style='text-align: center; font-size: 50px; color: #FF6F61'>WELCOME TO ONLYUSERS</h1>")

    st.divider()
    
    st.markdown("## Welcome User,  lets get you to :blue[Login] or a new user is here to :blue[SignUp]?")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("<h2 style='text-align:center; color: #4A90E2'>LOGIN</h1>", unsafe_allow_html=True)
        login_btn_container = st.container(horizontal=True, horizontal_alignment="center")
        login_btn_container.button("Login", 
                                    type="primary", 
                                    use_container_width=True,
                                    key="login-btn",
                                    on_click=login_page
                                    )

    with col3:
        st.write("<h2 style='text-align:center; color: #4A90E2'>SIGN UP</h1>", unsafe_allow_html=True)
        signup_btn_container = st.container(horizontal=True, horizontal_alignment="center")
        signup_btn_container.button("SignUp",
                                    type="primary",
                                    use_container_width=True,
                                    key="signup-btn",
                                    on_click=signup_page
                                    )
            

elif st.session_state.page == "login":
    st.write("<h1 style='text-align:center;'>LOGIN</h1>", unsafe_allow_html=True)
    login.login_form()

    def forgot_password():
        st.session_state.page = "forgot_password"
        print("checked")

    st.checkbox("Forgot Password?", on_change=forgot_password)
    
    st.button("Back", on_click=home_page)


elif st.session_state.page == "signup":
    st.write("<h1 style='text-align:center;'>SIGN UP</h1>", unsafe_allow_html=True)
    signup.signup_form()
    st.button("Back", on_click=home_page)

elif st.session_state.page == "forgot_password":
    st.write("<h1 style='text-align:center;'>FORGOT PASSWORD</h1>", unsafe_allow_html=True)
    forgot_password.forgot_password()
    st.button("Back", on_click=home_page)
    
elif st.session_state.user_session:

    if st.session_state.page == "welcome":
        
        placeholder = st.empty()
        if st.session_state.get("login_success", False):
            placeholder.success("Login successful!")
            st.balloons()
            st.session_state.login_success = False

        st.write("<h1 style='text-align:center;'>WELCOME</h1>", unsafe_allow_html=True)
        welcome.welcome_page()
        st.button("Logout", on_click=home_page)

else:
    st.warning("Please Login First")
    st.button("Home", on_click=home_page)
