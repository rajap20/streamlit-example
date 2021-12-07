! pip install category_encoders
!pip install -q pyngrok
!pip install -q streamlit
!pip install -q streamlit_ace

import pickle
import streamlit as st

import pandas as pd
pickle_in = pd.read_pickle('classifier.pkl')
