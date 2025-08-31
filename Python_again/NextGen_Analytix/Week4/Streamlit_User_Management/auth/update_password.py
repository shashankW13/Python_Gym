import streamlit as st
from db import queries
from auth import validators

def update_password():
    form_key = "forgot-password" if st.session_state.page == "forgot_password" else "update-password"

    st.subheader("Update Password")
    with st.form(key=form_key):

        username = None
        if form_key == "forgot-password":
            st.markdown("### Enter your Username")
            username = st.text_input("Username").strip()

        st.markdown("### Enter your current password")
        current_password = st.text_input("Old Password", type="password").strip()

        st.markdown("### New Password:")
        new_password = st.text_input("New Password", type="password").strip()

        feedback = st.empty()
        updated_pass = st.form_submit_button("Update Password")

        # ✅ Check empty fields
        if updated_pass:
            required = [current_password, new_password] if form_key != "forgot-password" else [username, current_password, new_password]
            if not all(required):
                st.warning("⚠️ Please fill in all fields before submitting.")
                return

            # ✅ Fetch user info
            result_id_status, user_id = queries.select_data(
                column="userid",
                condition="username",
                value=username if form_key == "forgot-password" else st.session_state.form_values["username"]
            )
            result_pass_status, actual_pass = queries.select_data(
                column="password",
                condition="userid",
                value=user_id
            )

            if not (result_id_status and result_pass_status):
                st.warning("No account found!")
                return

            # ✅ Password check
            if current_password != actual_pass:
                st.error("Incorrect current password!")
                return

            # ✅ Validate new password
            validate_status, validation_msg = validators.validate_password(new_password)
            if not validate_status:
                st.warning(validation_msg)
                return

            # ✅ Extra auth check for forgot-password
            if form_key == "forgot-password":
                auth_status, auth_msg = queries.check_login_credentials(username, current_password)
                if not auth_status:
                    st.warning(auth_msg)
                    return

            # ✅ Update password
            update_status, update_msg = queries.update_data("password", new_password, user_id)
            if update_status:
                st.session_state.form_values["password"] = new_password
                st.session_state.update_success_msg = "Password updated successfully! ✅"
                feedback.success(st.session_state.update_success_msg)
                del st.session_state.update_success_msg
            else:
                st.error(update_msg)
