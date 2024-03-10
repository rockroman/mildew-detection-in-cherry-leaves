import streamlit as st
import matplotlib as plt 

# Defining the page 'Quick Sumary' format and information 

def page_summary_body():

    st.image('images/cherryblossomcover.jpg')
    st.write('## Project Summary')
    st.write('### General Information ')
    st.write('#### Powdery Mildew on Cherry Trees')
    

   
    st.write(

        f'Powdery Mildew is a common fungus, that affects a wide array of plants,'
        f'manifesting as light grey or white powdery spots primarily on leaves but '
        f'also on stems, flowers, fruits, and vegetables. The spread of these spots '
        f'progressively covers most leaves, particularly impacting new plant growth.\n\n'


        f'While seldomly fatal, unchecked powdery mildew can inflict serious harm '
        f'by depriving plants of water and nutrients. Typical effects include '
        f'yellowing, withering, or distortion of leaves, along with weakened growth,'
        f'reduced blooming, and slower development.\n\n'


        f'Currently, manual inspection of each **cherry tree** requires approximately 30 minutes,'
        f' with an additional minute per tree for treatment application if necessary. '
        f'This process, given the multitude of trees across various farms, lacks scalability. '
        f'To address this, the IT team proposed implementing a machine learning (ML) system '
        f'for instant powdery mildew detection in **cherry tree** images, with potential '
        f'application to other crops if successful.\n\n'
    )
    

    # Define the paths to the images
    image_paths = [
        'inputs/cherry-leaves_dataset/cherry-leaves/healthy/00a8e886-d172-4261-85e2-780b3c50ad4d___JR_HL 4156.JPG',
        'inputs/cherry-leaves_dataset/cherry-leaves/fungal-infected/0a283423-3a6d-43a4-92e5-267c8153ca45___FREC_Pwd.M 4921_flipLR.JPG'
    ]

    # Define the captions for the images
    captions = ["Healthy leaf image", "Fungal-infected leaf image"]

    # Display the images side by side
    st.image(image_paths, caption=captions)


    st.info(
        f'If additional information is needed:\n'
        f'* Visit and **read** the[ Project README file](https://github.com/FerchaPombo/mildew-detection-in-cherry-leaves/blob/main/README.md).\n'
        f'* [Wikipedia](https://en.wikipedia.org/wiki/Powdery_mildew)\n'
    )
    st.write(
        f'## Project has 2 business requirements:\n\n'
        f'* 1- Conduct a study to visually differentiate healthy cherry leaves from'
        f'those with powdery mildew.\n'
        f'* 2- Predict whether a cherry tree is healthy or afflicted with powdery mildew.'
    )


    st.write('### Project Dataset:')
    st.write(
        
        f'The dataset, comprising cherry tree leaf images provided by Farmy & Foods, '
        f'forms the basis for model training and evaluation.\n\n'
        f'This dataset, sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves) and '
        f'consists of over 4,000 images, with a subset of over 4k images chosen for expedited model training.'
    )
