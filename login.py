import streamlit as st          #Streamlit module/package
from PIL import Image           #Used to display the CBRE UK Logo
from datetime import datetime   #Used for datetime functions
import snowflake.connector      #Used for Snowflake Connectivity
from snowflake.snowpark import Session

#Setup streamlit to use wide layout
st.set_page_config(page_title="Streamlit Visualization Demo", page_icon="CBRE_UK.jpg", layout="wide")
# Create an empty container
placeholder = st.empty()

actual_email = "email"
actual_password = "password"

# Insert a form in the container
with placeholder.form("login"):
    st.markdown("#### GDP Data validation Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")

if submit and email != '' and password == actual_password:
    # If the form is submitted and the email and password are correct,
    # clear the form/container and display a success message
    placeholder.empty()
    st.success("Login successful")
elif submit and email != actual_email and password != actual_password:
    st.error("Login failed")
else:
    pass
#Setup Streamlit Sidebar
image = Image.open("CBRE_UK.jpg")
st.sidebar.image(image, caption="***CBRE GDP Data visualization***", use_column_width="auto")