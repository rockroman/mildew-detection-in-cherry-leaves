# Bugs

### Minor fixed bugs 

#### Some of the bugs listed here were addressed during the development of the app.

##### 1

![Backwards](assets/images/bugsandfixes/modelpredictingbackwards.png)

After adjusting the label for the 'fungal-infected' class, the model consistently provided correct predictions when new data was input. This issue was resolved by modifying the key indexes in the predictive_analysis.py file. Specifically, the change involved swapping the positions of the 0 and 1 indexes.

index={'healthy': 1, 'fungal-infected': 0}.keys()

After this minor adjustment, the model resumed accurate predictions each time an image was uploaded through the Streamlit app.

##### 2

![Learning Curve](assets/images/bugsandfixes/modellearningcurve.png)

Dont remember how it was fixed ! 

##### 3

![Image Montage](assets/images/bugsandfixes/buginimagemontage2.png)

##### 4

![File not found](assets/images/bugsandfixes/couldntfindfileinpagevisualizer.png)

#### 5

![Key Error](assets/images/bugsandfixes/keyErrorprobability.png)

#### 6

![image montage](assets/images/bugsandfixes/Leafvisualizerimagemontageerror.png)

#### 7

![Load Model](assets/images/bugsandfixes/loadmodelgotanunexpectedargument.png)


