import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Online Clipboard", page_icon="📋")
st.title("📋 Online Clipboard")

option = st.sidebar.selectbox("Select Action", ("Add Clip", "Get Clip"))

# ------------------ Add Clip ------------------ #
if option == "Add Clip":
    st.subheader("Add a New Clip")
    clip_id = st.text_input("Clip ID")
    content = st.text_area("Content")

    if st.button("Add Clip"):
        if clip_id and content:
            payload = {"clip_id": clip_id, "content": content}
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
            st.warning("Please enter both clip_id and content.")

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
