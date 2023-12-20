import streamlit as st
import matplotlib.pyplot as plt
import streamlit_extras
import pandas as pd
import datetime
import streamlit_modal
import streamlit.components.v1 as components
import requests
import streamlit.web.cli as stcli
import sys
import os
import subprocess
import threading

# Function to determine the path of resources at runtime
def resource_path(relative_path):
    """ Get absolute path to resource for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def run_streamlit():
    # Running Streamlit app
    streamlit_app_path = resource_path("test_app_no_menu.py")
    sys.argv = ["streamlit", "run", streamlit_app_path, "--global.developmentMode=false"]
    sys.exit(stcli.main())

def run_fastapi():
    # Modify the Python path to include the directory of 'client.py'
    client_path = resource_path("")  # Get the root directory of the executable
    # Get the parent directory of the executable's directory
    parent_dir = os.path.dirname(client_path)

    os.chdir(parent_dir)
    
    # Running FastAPI app
    fastapi_command = ["uvicorn", "client:app", "--host", "0.0.0.0", "--port", "8000"]
    subprocess.run(fastapi_command)

if __name__ == "__main__":
    # Running FastAPI in a separate thread
    fastapi_thread = threading.Thread(target=run_fastapi)
    fastapi_thread.start()

    # Running Streamlit in the main thread
    run_streamlit()