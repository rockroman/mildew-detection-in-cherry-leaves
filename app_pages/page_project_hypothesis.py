import streamlit as st 
import matplotlib.pyplot as plt

# Plan project Hypotesis visualization page

def page_project_hypothesis_body():
    st.write('## Hypothesis and Validation')
    st.write('### Hypothesis:')

    st.write(
        f'Plants affected by fungal infestation, specifically powdery mildew,'
        f'exhibit distinct visual characteristics on their leaves, such as light'
        f'grey or white powdery spots. By conducting an average image study, we aim'
        f'to investigate whether these visual markers reliably differentiate infected'
        f'plants from healthy, uninfected ones.'
        )

    st.success(
        f'### Validation:\n\n'
        f'An image montage reveals characteristic whitish marks on leaves affected by '
        f'powdery mildew fungal infestation. Through analysis of average images, variability'
        f'images, and the differences between averages, distinct patterns emerge, facilitating'
        f'differentiation between infected and healthy leaves.'
    )
