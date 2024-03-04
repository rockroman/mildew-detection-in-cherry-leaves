import streamlit as st
import os
import pandas as pd
import numpy as numpy
import seaborn as sns 
import matplotlib.pyplot as plt

import itertools 
import random 

def page_leaf_visualizer_body():
    st.write('### Cells Visualizer')
    st.info(
        f'As a business requirement, the client is interested to have a study to visually differentiate'
        f'a fungal-infected leaf and a healthy one.')

    #version = 'v1'

