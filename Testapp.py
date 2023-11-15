import streamlit as st          #Streamlit module/package
import numpy as np
import pandas as pd             #pandas module/package
import pydeck as pdk            #PyDeck used for Geographic Street Maps
import plotly.express as px     #Used for Pie Charts
from PIL import Image           #Used to display the CBRE UK Logo
from datetime import datetime   #Used for datetime functions
import snowflake.connector      #Used for Snowflake Connectivity
from snowflake.snowpark import Session
#Setup streamlit to use wide layout
st.set_page_config(page_title="Streamlit Visualization Demo", page_icon="CBRE_UK.jpg", layout="wide")

#Initialize Snowflake connection.
@st.cache_resource
def init_conn():
    return snowflake.connector.connect(**st.secrets["snowflake"])
conn = init_conn()
st.success("Connected to Snowflake!")

def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()
run_query("USE WAREHOUSE dev_dedm_data_engineer_whs")
rows = run_query("""SELECT table_name
                      FROM information_schema.tables 
                     WHERE table_type = 'BASE TABLE'
                       AND table_schema = 'LANDING_ZONE'
                  ORDER BY table_name;""")

# Print results.
#st.dataframe(rows)
#recrds = rows.replace(")",'')
Tab_name = st.selectbox('Source Table Name',rows)
#recrds = Tab_name.replace(")",'')
st.write("""Selected --> """,Tab_name)

# Load data table
@st.cache_data
#Get Excel Data and Cache it
def get_data_from_csv():
    pd.options.display.max_rows = 9999
    df = pd.read_csv("main_office.csv")
    return df
df = get_data_from_csv()
#today = datetime.today()
#st.sidebar.write("This CCC is for: ", Tab_name)
#st.sidebar.write(today)
#Write a Title and subtitle on main page
st.write("""
# Main Office Table Count Info
""")
st.write(f"""
There are **{df.shape[0]} Properties** in this dataset
""")
#Setup Streamlit Sidebar
image = Image.open("CBRE_UK.jpg")
st.sidebar.image(image, caption="***CBRE GDP Data visualization***", use_column_width="auto")


