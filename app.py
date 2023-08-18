

import numpy as np
import streamlit as st
import pandas as pd
st.title("1-Chi square test")

df = pd.read_excel("./Goodness Of Fit Test(ChiSquare).xlsx", sheet_name="Sheet2")
st.write(df)



