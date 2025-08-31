import streamlit as st
from db import queries
from auth import validators

def delete_account(username):
    st.subheader("Delete Account")
    with st.form(key="delete-account"):
        st.markdown(f"### Enter your password")
        current_password = st.text_input("Password", type="password").strip()

        delete_feedback = st.empty()

        deleted = st.form_submit_button("Delete Account", type="primary")

        auth_status, auth_msg = queries.check_login_credentials(st.session_state.form_values["username"], current_password)

        if deleted:
            if auth_status:
                delete_status, delete_msg = queries.delete_user(username)
            
                if delete_status:
                    st.session_state.update_success_msg = "Account deleted successfully! ✅"
                    st.session_state.user_session = False
                else:
                    st.error(delete_msg)
                    return

            else:
                st.error(auth_msg)

        if "update_success_msg" in st.session_state:
                delete_feedback.success(st.session_state.update_success_msg)
                del st.session_state.update_success_msg

        