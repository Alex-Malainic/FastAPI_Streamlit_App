import streamlit as st
import matplotlib.pyplot as plt
import streamlit_extras
import pandas as pd
import datetime
import streamlit_modal
import streamlit.components.v1 as components


# These imports are needed for the streamlit execution below.
import streamlit.web.cli as stcli
import sys
import os, sys


def resolve_path(path):
    resolved_path = os.path.abspath(os.path.join(os.getcwd(), path))
    return resolved_path

if __name__ == "__main__":
    sys.argv=["streamlit", "run", resolve_path("test_app_no_menu.py"), "--global.developmentMode=false"]
    sys.exit(stcli.main())