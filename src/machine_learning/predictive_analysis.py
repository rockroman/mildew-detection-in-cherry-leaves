#functions dealing with the powdery mildew detection page. 
# plot_predictions_probabilities function plots the probabilistic result of any image as infected or not infected using a bargraoh using hte plotly package  which pltos the probability  per class healthy and fungal-infected and using plotly_chart to render the plot in the dashboard

#2nd function is used to rezise the shape of the shape of the input image to the average image size of 129x129 px.abs
#we load the average images from the embedded pickle file we cretated

#3rd function: load_model_and_predict function loads the trained ML model and predicts the live image data. function predicts a value between 0 and 1 and maps it with its key as a fungal contained leaf or a healthy one, it also calculates the prediction  probability value 
#for both the classes and the returns  it into the view along with the predicted class label 

#st.write function  writes a statement for every image  on the view for its predicted labels 
