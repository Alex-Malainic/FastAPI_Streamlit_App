import streamlit as st

st.set_page_config(page_title = "Test Tool", page_icon = ':sun_small_cloud:', layout="wide")

from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
from streamlit_extras.chart_container import chart_container
from streamlit_extras.altex import line_chart
from streamlit_extras.colored_header import colored_header
from st_aggrid import AgGrid
import pandas as pd
import datetime
from streamlit_modal import Modal
import streamlit.components.v1 as components

st.title('Test app - demo test app demo demo :sun_small_cloud:')

selected_subpage = option_menu(None, ['Settings', 'Rate Reasonability Check', 'History', 'Save and Load', 'Help'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

# ------------------------------------------------------ Settings ---------------------------------------------------------
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True


if selected_subpage == "Settings":
            with st.sidebar:
                st.write("## Initial Settings")
            
                d = st.date_input(
                    "Start and End Date",
                    (datetime.datetime.now(), datetime.datetime.now()),
                    format="DD/MM/YYYY",
                )   
                
                st.write("## Advanced Settings")

                RR_TRANS_QUERY = st.text_input('RR_TRANS_QUERY', " sqleuries/ratereasonabilityquery/ratereasoanbility sql. rar dw", help = 'Query to fetch the list of transactions conducted on FRM and OF instruments which breached the tolerance band defined in the TMS system')
                RR_TRANS_QUERY = st.text_input('RR_TRANS_QUERY', " sqleuries/ratereasonabilityquery/ratereasoanbilitys sql. rar dw")
                RR_TRANS_QUERY = st.text_input('RR_TRANS_QUERY', " sqleuries/ratereasonabilityquery/ratereasoanbilitye sql. rar dw")
                RR_TRANS_QUERY = st.text_input('RR_TRANS_QUERY', " sqleuries/ratereasonabilityquery/ratereasoanbilityf sql. rar dw")
                RR_TRANS_QUERY = st.text_input('RR_TRANS_QUERY', " sqleuries/ratereasonabilityquery/ratereasoanbilityd sql. rar dw")
                RR_TRANS_QUERY = st.text_input('RR_TRANS_QUERY', " sqleuries/ratereasonabilityquery/ratereasoanbilityr sql. rar dw")


                st.button("Restore Default Settings")
                st.write("#")
                st.write("#")
                st.write("#")
                st.write("#")
                st.write("#")
                st.write("#")


                run_button = st.button("#### Run Rate Reasonability Check", use_container_width = True, on_click=click_button)


example_df = pd.DataFrame({'index': [1,2,3], 'transaction_fk': ['345', '542', '887'], 'nominal': [3545, 7776, 4443]})

if st.session_state.clicked:
    st.data_editor(example_df)
    modal = Modal(
        "Demo Modal", 
        key="demo-modal",
        
        # Optional
        padding=20,    # default value
        max_width=744  # default value
    )


    open_modal = st.button("Open")

    if open_modal:
        modal.open()

    if modal.is_open():
        with modal.container():
            st.write("Text goes here")

            html_string = '''
            <h1>HTML string in RED</h1>

            <script language="javascript">
            document.querySelector("h1").style.color = "red";
            </script>
            '''
            components.html(html_string)
