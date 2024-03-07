
#st.write function  writes a statement for every image  on the view for its predicted labels 
import streamlit as st 
import numpy as np 
import pandas as pd 
import plotly.express as px
from tensorflow.keras.models import load_model
from PIL import Image
from src.data_management import load_pkl_file 

# plot_predictions_probabilities function plots the probabilistic result of any image as infected or not infected using a bargraoh using hte plotly package  which pltos the probability  per class healthy and fungal-infected and using plotly_chart to render the plot in the dashboard
def plot_predictions_probabilities(pred_proba, pred_class):

    prob_per_class= pd.DataFrame(
        data=[0,0],
        index={'healthy': 0, 'powdery_mildew': 1}.keys(),
        columns=['Probability']
    )
    prob_per_class.loc[pred_class] = pred_proba
    for x in prob_per_class.index.to_list():
        if x not in pred_class: prob_per_class.loc[x] = 1 - pred_proba
    prob_per_class = prob_per_class.round(3)
    prob_per_class["Diagnostic"] = prob_per_class.index

    fig = px.bar(
        prob_per_class,
        x = 'Diagnostic',
        y = prob_per_class['Probability'],
        range_y=[0,1],
        width=600, height=300, template='seaborn'
    )
    st.plotly_chart(fig) #function used to plot the image onthe dashboard

#used to rezise the shape of the shape of the input image to the average image size of 129x129 px.abs
#we load the average images from the embedded pickle file we cretated
def resize_input_image(img, version):
    image_shape = load_pkl_file(file_path=f"outputs/{version}/image_shape.pkl")
    img_resized = img.resize((image_shape[1], image_shape[0]),Image.LANCZOS)# change method to match compatibility 
    my_image = np.expand_dims(img_resized, axis=0)/255

    return my_image

#3rd function: load_model_and_predict function loads the trained ML model and predicts the live image data. function predicts a value between 0 and 1 and maps it with its key as a fungal contained leaf or a healthy one, it also calculates the prediction  probability value 
#for both the classes and the returns  it into the view along with the predicted class label 
def load_model_and_predict(my_image, version):
    
    model = load_model(f'outputs/{version}/powdery_mildew_detector_model.h5')
# check for the acurracy of the labels. if healthy means 0 and vice versa

    pred_proba = model.predict(my_image)[0,0]

    target_map = {v: k for k, v in {'healthy': 0, 'powdery_mildew': 1}.items()}
    pred_class = target_map[pred_proba > 0.5]
    if pred_class == target_map[0]: pred_proba = 1 - pred_proba

    st.write(
        f'The predictive analysis indicates the leaf image is '
        f'**{pred_class.lower()}** from Powderly Mildew.'
    )

    return pred_proba, pred_class
