import streamlit as st 
import matplotlib.pyplot as plt
import pandas as pd 
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation

#create function to render  the perfromance metrics of the ML model 

def page_ml_performance_metrics():
    version = 'v1'

    st.write('### Train, Validation and Test Set: Labels Frequencies')

    labels_distribution = plt.imread(f'outputs/{version}/labels_distribution.png')
    st.image(labels_distribution, caption='Model Training Acurracy')
    st.write("---")


    st.write('### Model History')
    col1, col2 = st.beta_columns(2)
    with col1:
        model_acc = plt.imread('outputs/{version}/model_training_acc.png')
        st.image(model_acc, caption='Model Training Accuracy')

    with col2:
        model_loss = plt.imread('outputs/{version}/model_training_losses.png')# this one is still not rendered 
        st.image(model_loss, caption="Model Training Losses")
        st.write('---')




    st.write('### Generalized Performamce on Test Set')
    st.dataframe(pd.DataFrame(load_test_evaluation(version), index=['Loss', 'Accuracy']))
    