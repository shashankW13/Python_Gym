import streamlit as st
from db import queries
from auth import validators

def update_username(username):
    st.subheader("Update Username")
    with st.form(key="update-username"):
        st.markdown(f"### Current username: {username}")
        st.markdown(f"### New username:")
        new_username = st.text_input("### Username").strip()

        feedback = st.empty()

        result_status, user_id = queries.select_data(column="userid", 
                                      condition="username",
                                      value=st.session_state.form_values["username"]
                                      )
        


        updated = st.form_submit_button("Update Username")

        if updated and result_status:
            validate_status, validation_msg = validators.validate_username(new_username)
  
            if validate_status:
                update_status, update_msg = queries.update_data("username", new_username, user_id)

                if update_status:
                    st.session_state.form_values["username"] = new_username
                    st.session_state.update_success_msg = "Username updated successfully! ✅"
                    st.rerun()
                else:
                    st.error(update_msg)
            else:
                st.warning(validation_msg)

        if "update_success_msg" in st.session_state:
            feedback.success(st.session_state.update_success_msg)
            del st.session_state.update_success_msg