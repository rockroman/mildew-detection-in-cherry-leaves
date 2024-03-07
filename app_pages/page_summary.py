import streamlit as st
import matplotlib as plt 

# Defining the page 'Quick Sumary' format and information 

def page_summary_body():

    st.image('assets/images/cherryblossomcover.jpg')
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
        f' with an additional minute per tree for treatment application if necessary.'
        f'This process, given the multitude of trees across various farms, lacks scalability.'
        f'To address this, the IT team proposed implementing a machine learning (ML) system '
        f'for instant powdery mildew detection in **cherry tree** images, with potential '
        f'application to other crops if successful.\n\n'
    )

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
        
        f'The dataset, comprising cherry leaf images provided by Farmy & Foods, '
        f'forms the basis for model training and evaluation.\n\n'
        f'This dataset, sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves) and '
        f'consists of over 4,000 images, with a subset of over 4k images chosen for expedited model training.'
    )