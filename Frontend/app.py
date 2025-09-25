import streamlit as st
import requests

# Backend API base URL
BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Online Clipboard", page_icon="📋")

st.title("📋 Online Clipboard")

# Sidebar navigation
option = st.sidebar.selectbox(
    "Select Action",
    ("Add User", "Add Clip", "Get Clip")
)

# ------------------ Add User ------------------ #
if option == "Add User":
    st.subheader("Add a New User")
    username = st.text_input("Username")
    email = st.text_input("Email")

    if st.button("Add User"):
        if username and email:
            payload = {"username": username, "email": email}
            try:
                response = requests.post(f"{BASE_URL}/users/", json=payload)
                if response.status_code == 200:
                    st.success("✅ User added successfully!")
                    st.json(response.json())
                else:
                    st.error(f"❌ {response.json()['detail']}")
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter both username and email.")

# ------------------ Add Clip ------------------ #
elif option == "Add Clip":
    st.subheader("Add a New Clip")
    clip_id = st.text_input("Clip ID")
    user_id = st.number_input("User ID", min_value=1)
    content = st.text_area("Content")

    if st.button("Add Clip"):
        if clip_id and user_id and content:
            payload = {"clip_id": clip_id, "user_id": user_id, "content": content}
            try:
                response = requests.post(f"{BASE_URL}/clips/", json=payload)
                if response.status_code == 200:
                    st.success("✅ Clip added successfully!")
                    st.json(response.json())
                else:
                    st.error(f"❌ {response.json()['detail']}")
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please fill all fields.")

# ------------------ Get Clip ------------------ #
elif option == "Get Clip":
    st.subheader("Fetch Clip by ID")
    clip_id = st.text_input("Enter Clip ID to Fetch")

    if st.button("Fetch Clip"):
        if clip_id:
            try:
                response = requests.get(f"{BASE_URL}/clips/{clip_id}")
                if response.status_code == 200:
                    st.success("✅ Clip fetched successfully!")
                    st.json(response.json())
                else:
                    st.error(f"❌ {response.json()['detail']}")
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter a Clip ID.")
