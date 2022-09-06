import streamlit as st
import pandas as pd
import numpy as np
from src import Random_Number

st.title('Raffle Winners Today!!!')

try:
    r, s = Random_Number.run_app()
    st.subheader(r)
    st.subheader(s)
except:
    pass

