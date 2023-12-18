import streamlit as st

st.set_page_config(page_title = "Test Tool", page_icon = ':sun_small_cloud:', layout="wide")
st.title('Test app - demo test app demo demo :sun_small_cloud:')

import matplotlib.pyplot as plt
from streamlit_extras.chart_container import chart_container
from streamlit_extras.altex import line_chart
from streamlit_extras.colored_header import colored_header
import pandas as pd
import datetime
from streamlit_modal import Modal
import streamlit.components.v1 as components



# ------------------------------------------------------ Settings ---------------------------------------------------------

#functionality to add button to session state, so it remains clicked for the remainder of the session
if 'run_button' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

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


    run_button = st.button("#### Run Rate Reasonability Check", use_container_width = True, on_click=click_button, key = 'run_button')


example_df = pd.DataFrame({'index': [1,2,3], 'transaction_fk': ['345', '542', '887'], 'nominal': [3545, 7776, 4443]})

if st.session_state.clicked == True:
    #implemeent modal: if settings were not changed : do you want to run with the current defualt settings?
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
        st.write("haha")
    if modal.is_open():
        st.write("haha")
        with modal.container():
            html_string = '''
            <style>
                #firework-container {
                    position: relative;
                    width: 100%;
                    height: 300px; 
                    overflow: hidden;
                    background: black;
                }
                .firework {
                    position: absolute;
                    border-radius: 50%;
                    animation: firework-animation 3s ease-out forwards;
                }
                @keyframes firework-animation {
                    0% { transform: scale(0); opacity: 1; }
                    100% { transform: scale(1); opacity: 0; }
                }
                #message {
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    color: white;
                    font-size: 24px;
                    opacity: 0;
                    transition: opacity 2s;
                    transition-delay: 3s;
                }
            </style>
            <div id="firework-container">
                <div id="message">Streamlit is awesome</div>
            </div>
            <script language="javascript">
                function createFirework() {
                    const firework = document.createElement('div');
                    firework.className = 'firework';
                    firework.style.left = `${Math.random() * 100}%`;
                    firework.style.top = `${Math.random() * 100}%`;
                    firework.style.width = `${Math.random() * 5 + 4}px`;
                    firework.style.height = firework.style.width;
                    firework.style.backgroundColor = `rgb(${Math.random() * 255}, ${Math.random() * 255}, ${Math.random() * 255})`;

                    const container = document.getElementById('firework-container');
                    container.appendChild(firework);

                    setTimeout(() => {
                        firework.remove();
                    }, 3000); // Firework duration
                }

                setInterval(createFirework, 1); // Frequency of fireworks
                setTimeout(() => {
                    document.getElementById('message').style.opacity = 1;
                }, 3000); // Delay for the message to appear
            </script>
            '''
            components.html(html_string, height=300)  # Adjust height as needed