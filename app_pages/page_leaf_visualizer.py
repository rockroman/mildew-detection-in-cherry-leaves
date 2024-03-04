import streamlit as st
import os
import pandas as pd
import numpy as numpy
import seaborn as sns 
import matplotlib.pyplot as plt

import itertools 
import random 

#Function that carries the logic on what happens when the checkbox button is clicked, goes 
#through the options to display , and what happens when each option is selected 

def page_leaf_visualizer_body():
    st.write('### Cells Visualizer')
    st.info(
        f'As a business requirement, the client is interested to have a study to visually differentiate'
        f'a fungal-infected leaf and a healthy one.')

    version = 'v1'
    #When this option is chosen,if compares the difference between average and variability in the dataset
    # displaying the embedded plots created in the notebooks.
    if st.checkbox('Difference between average and variability image'):

        av_powdery_mildew = plt.imread(f'outputs,{version}/avg_var_powdery_mildew.png')
        av_healthy = plt.imread(f'outputs/{version}/avg_var_healthy.png')
        
        #check texts based on outputs further on the development of the app.
        st.warning(
            f'* We noticed the average and variability images did not show'
            f'any patterns where we could intuitively differentiate one to another.'
            f'However, a small difference in color and texture of the average images is seen for both labels'
        )

        st.image(av_powdery_mildew, caption='Fungal-infected leaf - Average Variability')
        st.image(av_healthy, caption='Healthy Leaf - Average and Variability')
        st.write('---')

        if st.checkbox('Differences between average fungal-infected and healthy leaves'):
            diff_between_avgs = plt.imread(f'outputs/{version}/avg_diff.png')

            st.warning(
                f'* We notice this study did not show patterns where we could intuitively '
                f'differentiate one to another.')
            st.image(diff_between_avgs, caption='Difference between average images')
        # Creates an image montage of random images from the Validation set for gallery display 
        if st.checkbox('Image Montage'):
            st.write(f'* To refresh the montage, click on "Create Montage" button')
            my_data_dir = 'inputs/cherry-leaves_dataset/cherry-leaves'
            labels = os.listdir(my_data_dir+ '/validation')
            label_to_display = st.selectbox(label='Select Label', options=labels, index=0)
            if st.button("Create Montage"):
                image_montage(dir_path= my_data_dir + '/validation',
                                label_to_display=label_to_display,
                                nrows=8, ncols=3, figsize=(10,25))
            st.write('---')

#create function to display the imges of the montage 
def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15,10)):
    sns.set_style("dark")
    labels = os.listdir(dir_path)

    #Indicate which class you are interested to display 
    if label_to_display in labels:
        #function that checks how many images are there in the folder and if the space of your 
        # montsge is grater than the the subset size
        images_list = os.listdir(dir_path+ '/'+ label_to_display)
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            print(
                f'Decrease nrown and ncols to create your montage. \n'
                f'There are {len(images_list)} in your subset. '
                f'You requested a montage with {nrows * ncols} spaces'
            )
            return

        # Create a list of axes indeices based on nrows and ncols
        list_rows = range(0,nrows)
        list_cols = rande(0,ncols)
        plot_idx = list(itertools.product(list_rows,list_cols))

        #create the figure for this plot and display the images 

        fig, axes = plt.subplot(nrows= nrows, ncols= ncols, figsize= figsize)
        for x in range(0,nrows*ncols):
            img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
            img_shape = img_shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0], plot_idx[x][1]].set_title(f"Width {img_shape[1]}px x Height {img_shape[0]}px")
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()

        st.pyplot(fig=fig)
        plt.show()

        else:
            print('The label you selected does not exist.')
            print('The existing options are: {labels}')





