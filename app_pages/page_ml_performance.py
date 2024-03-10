import streamlit as st 
import matplotlib.pyplot as plt
import pandas as pd 
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def page_ml_performance_metrics():
    version = 'v1'
    '''
    Function that renders the performance metrics of the ML model,
    v1
    '''

    st.write('## Train, Validation and Test Set: Labels Frequencies\n\n')
    st.write(
        f'Dataset was divided into 3 subsets: \n\n'
        f'* Training Set: comprises 70% of the data.\n'
        f'* Test Set: comprises 10% of the data.\n'
        f'* Validation Set: comprises 20% of the data. \n'
    )
    st.write(
        f"Labels were divided in : *'healthy'* and *'fungal-infected*"

    )
   
    labels_distribution = plt.imread(f'outputs/{version}/labels_distribution.png')
    st.image(labels_distribution, caption='Model Training Acurracy')
    st.write("---")


    st.write('## Model History')
    col1, col2 = st.beta_columns(2)
    with col1:
        model_acc = plt.imread('outputs/v1/model_training_acc.png')
        st.image(model_acc, caption='Model Training Accuracy')

    with col2:
        model_loss = plt.imread('outputs/v1/model_training_losses.png')
        st.image(model_loss, caption="Model Training Losses")
        st.write('---')

    

    
    st.write('### Generalized Performamce on Test Set')
    st.dataframe(pd.DataFrame(load_test_evaluation(version), index=['Loss', 'Accuracy']))

    st.write('### General analysis of Accuracy and Loss')

    
    st.write(
        f'### Concepts summary on performance metrics : \n\n'

        f"**Loss** and **accuracy** are two essential metrics used to evaluate the performance of machine learning models. \n\n"


        f'* **Loss:**\n\n '

            f' -Loss represents the accumulation of errors in our model and measures how well the model is performing.\n\n '

            f' -High loss indicates significant errors, while low loss suggests better model performance. Observing the '
            f"loss over time can provide insights into the model's learning process. \n\n"

            f' -Oscillating loss may indicate the model is not learning, while decreasing loss in the training set but '
            f'not in the validation set may indicate overfitting.\n\n'
            f''

        f'* **Accuracy:**\n\n '

        f'-Accuracy measures the percentage of correct predictions made by the model compared to the true values. \n\n'

        f'-High accuracy indicates accurate predictions, while low accuracy suggests significant errors in predictions. \n\n'
        f''

        f'* **Learning Curve:**\n\n'

        f"-A learning curve is a graphical representation of a specific metric's progress during the training of a machine learning model.\n\n"

        f'-It typically plots time or progress on the x-axis and error or performance on the y-axis.\n\n'

        f"-Learning curves help monitor the model's evolution during training, diagnose problems, and optimize prediction performance.\n"
        f''
            
        f'* **Single Curves:**\n\n'

        f'-Common examples of learning curves include loss over time, accuracy, precision, and recall.\n\n'

        f"-Improvements in these metrics over time indicate the model's learning and improved performance.\n\n"

        f'-Learning curves may reach a plateau, indicating that the model has stopped learning and further '
        f'training may not yield significant improvements.\n\n'
        f''


        f'* **Detecting Model Behavior:**\n\n'

        f'-Monitoring the evolution of learning curves helps detect issues in the behavior of the model.\n\n'

        f'-Sudden changes or lack of improvement in learning curves may indicate underlying problems such as overfitting or underfitting. \n\n'
        f''
        
    f'Overall, learning curves provide valuable insights into the training process and the performance of machine learning models, '
    f'aiding in model evaluation and optimization.'
    )
