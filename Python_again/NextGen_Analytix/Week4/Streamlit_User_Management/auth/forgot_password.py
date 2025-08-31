import streamlit as st
from auth import update_password

def forgot_password():
    update_password.update_password()