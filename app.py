import streamlit as st
import pandas as pd
import numpy as np
from src import Random_Number

st.title('Raffle Winners Today!!!')

r, s = Random_Number.run_app()
st.write(r)
st.write(s)


