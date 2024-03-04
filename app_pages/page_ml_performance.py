import streamlit as st 
import matplotlib.pyplot as plt
import pandas as pd 
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation

#create function to render  the perfromance metrics of the ML model 

def page_ml_performance_metrics():
    version = 'v1'

    st.write('### Train, Validation and Test Set: Labels Frequencies')




    st.write('### Model History')




    st.write('### Generalized Performamce on Test Set')
    