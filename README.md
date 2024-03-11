
# Mildew Detection in Cherry Leaves

---
## Objective and Project description

The cherry plantation at Farmy & Foods faces a challenge with powdery mildew affecting their cherry trees.
Powdery Mildew (caused by many different species of ascomycete fungi in the order Erysiphales) is a common fungus that affects a wide array of plants, manifesting as light gray or white powdery spots primarily on leaves but also on stems, flowers, fruits, and vegetables. The spread of these spots progressively covers most leaves, particularly impacting new plant growth.

While seldomly fatal, unchecked powdery mildew can inflict serious harm by depriving plants of water and nutrients. Typical effects include yellowing, withering, or distortion of leaves, along with weakened growth, reduced blooming, and slower development.

Currently, manual inspection takes around 30 minutes per tree, with an additional minute for applying treatment if needed. With thousands of trees across multiple farms, this process is not scalable. To address this, the IT team proposed implementing an ML system to instantly detect powdery mildew in cherry tree images. If successful, this approach could be extended to other crops. The dataset comprises cherry leaf images provided by Farmy & Foods.

* The App live link is:  [Powdery Mildew Detector](https://powdery-mildew-detector-fp-c8dd417a4db2.herokuapp.com/)

### Client Goals:
* Faster Testing Results: Expedite the process of obtaining disease test results.

* Reduced Manual Workload: Minimize manual effort required for diagnosing mildew infection.

* Mildew Mitigation: Prevent the spread and recurrence of mildew infection in cherry trees.

### Client Benefits:
* Automated Mildew Detection: The ML model will automatically diagnose mildew presence in cherry leaves.

* Reduced Manual Work: Manual disease diagnosis processes will be significantly streamlined, saving time and resources.

* Early Disease Detection: Early detection of mildew allows for timely treatment, preventing further spread and damage.

### Dataset Content

Dataset was obtained from Kaggle. Subsequently,  a hypothetical user scenario was created to demonstrate the practical application of predictive analytics in a workplace project.

The dataset comprises over 4,000 images captured from the client's crop fields. These images depict both healthy cherry leaves and leaves afflicted with powdery mildew, a fungal disease that poses a threat to numerous plant species. Given the cherry plantation's significance within their product portfolio, the company is deeply invested in ensuring the market receives products of uncompromised quality.

---
## Business Requirements

The cherry plantation at Farmy & Foods faces a challenge with powdery mildew affecting their cherry trees. Currently, manual inspection takes around 30 minutes per tree, with an additional minute for applying treatment if needed. With thousands of trees across multiple farms, this process is not scalable. To address this, the IT team proposed implementing an ML system to instantly detect powdery mildew in cherry tree images. If successful, this approach could be extended to other crops. The dataset comprises cherry leaf images provided by Farmy & Foods.

### Business Requirement number 1:

* Conduct a study to visually differentiate healthy cherry leaves from those with powdery mildew.

### Business Requirement number 2:
* Predict whether a cherry tree is healthy or afflicted with powdery mildew.

---
## Hypothesis and how to validate?

### Hypothesis:

Plants affected by fungal infestation, specifically powdery mildew, exhibit distinct visual characteristics on their leaves, such as light grey or white powdery spots.

### Validation Approach:

We will validate this hypothesis by conducting an average image study following research on the disease. Our aim is to determine if these visual markers effectively distinguish between infected and healthy plants. The specific mathematical approach will be determined by our understanding of the problem and the differences between mathematical functions utilized to address such problems.

### Introduction:

It is suspected that cherry leaves affected by powdery mildew exhibit distinct markings on the leaf surface, along with variations in texture. These distinctive features must be effectively translated for the machine learning (ML) model to adequately learn from the dataset and undergo proper training.
When handling an image dataset, such as this one, it must undergo several preprocessing methods before being fed into the model.
Normalizing the images is crucial as it enables the neural network to produce consistent results with new test images. Additionally, normalization extracts essential pixel features from the images, aiding the model in distinguishing between different classes, which aligns with our goal in this binary classification model.

### Observations :
Image montage shows the diference between healthy and fungal-infected leaves

![healthy](/assets/images/readmeimages/healthyimagemontage.png)

![fungal-infected](/assets/images/readmeimages/fungalinfectedimagemontage.png)

After multiple evaluations of the model's performance on both the training and validation sets, it can be concluded that the model is operating with a high level of accuracy as anticipated.
**Overfitting of the model was minimal.**
Several epochs (training cycles) were tested until achieving low levels of loss and high levels of accuracy. The model accuracy lines generally trend upwards over time, indicating improvement with each epoch. Although the lines do not perfectly overlap, they stay close throughout the chart, with minor fluctuations. Notably, there are two instances where the lines touch or come close to each other: once around the middle of the chart and again at the last point.
In terms of loss, the training and validation loss lines show a descending trend over time, suggesting that the model's loss decreases with each epoch. Similar to the accuracy chart, the loss lines mirror each other closely, indicating consistent behavior between the training and validation sets. Towards the end of the chart, the loss lines follow the same path, with one on top of the other, suggesting minimal difference between training and validation loss at those points. Overall, both the accuracy and loss charts demonstrate that the model is learning effectively, as indicated by the upward trend in accuracy and the downward trend in loss. The close alignment between training and validation metrics suggests that the model generalizes well to unseen data.



## Business Requirement 1: Data Visualization

* The dashboard will showcase "mean" and "standard deviation" images for both infected and uninfected leaves. 
* It will also illustrate the disparity between an average infected leaf and a healthy one. 
* Additionally, the dashboard will feature an image montage highlighting either infected or uninfected leaves.


## Business Requirement 2: Classification

Our objective is to predict whether a leaf is infected with powdery mildew or not. To achieve this, we aim to develop a binary classifier and generate comprehensive reports.

## ML Business Case: Powdery Mildew Classification

Our aim is to develop a machine learning model capable of accurately predicting whether a leaf is infected with Powdery Mildew or not, using historical image data. This supervised model is designed as a binary classifier, distinguishing between infected and uninfected leaves.

The ultimate goal is to provide Farmy & Foods with a rapid and dependable diagnostic tool for identifying Powdery Mildew-infected leaves. The success of the model will be measured against a minimum accuracy threshold of 97% on the test set.

The model's output will consist of a binary flag indicating the presence or absence of Powdery Mildew, along with the associated probability of infection. To streamline the process, employees will capture leaf images manually and upload them to the application, enabling real-time predictions rather than batch processing.

Currently, the manual diagnostic process is time-consuming, with employees spending up to 30 minutes per plant to identify signs of infestation. Additionally, applying treatment to infected leaves consumes an additional minute. Human error in visual criteria assessment further adds to the risk of inaccurate diagnostics. With thousands of cherry trees spread across multiple farms, scalability becomes a significant concern.

The dataset, comprising cherry leaf images provided by Farmy & Foods, serves as the foundation for model training and evaluation. This dataset, sourced from Kaggle: [https://www.kaggle.com/codeinstitute/cherry-leaves] contains over 4,000 images, with a subset of XXX images selected for expedited model training.

Train data: Target - infected or not; Features - all leaf images.

---
## User Stories 

#### Template : 
As a **'role'** , I can **'Capability'**, so I can **"recieved benefit"**.

| As a…           | I can ..                 | so that…                                     |
| --------------- |------------------------- |---------------------------------------       |
| Plant inspector | open the Dashboard       | I can view the ML project.                   |
| Plant inspector | access the dataset       | I can revise  its contents.                  |
| Plant inspector | click on the nav buttons | I can navigate the pages.                    |
| Plant inspector | click on the check box   | I can create an image montage of the dataset.|
| Plant inspector | click on the check box   | I can view different comparison analyses between healthy and fungal-infected leaves.|
| Plant inspector | select different labels on the Leaf Visualizer page | I can create an image montage of the healthy and the fungal-infected leaves. |
| Plant inspector | upload an image of a leaf sample  | the Ml model gives me a prediction. |
| Data Practitioner | access the Jupyter Notebooks | I can have a deep insight on how the model was created. |
| Data Practitioner| review the Metric Performance Page| I can provide with better insights to the client. |

[Github Project](https://github.com/users/FerchaPombo/projects/3)


---
## Dashboard Design (Streamlit App User Interface)
---
### Page 1: Project Overview

#### General Information:
Powdery Mildew, a common fungus, affects a wide array of plants, manifesting as light grey or white powdery spots primarily on leaves but also on stems, flowers, fruits, and vegetables. The spread of these spots progressively covers most leaves, particularly impacting new plant growth.

While seldom fatal, unchecked powdery mildew can inflict serious harm by depriving plants of water and nutrients. Typical effects include yellowing, withering, or distortion of leaves, along with weakened growth, reduced blooming, and slower development.

Currently, manual inspection of each tree requires approximately 30 minutes, with an additional minute per tree for treatment application if necessary. This process, given the multitude of trees across various farms, lacks scalability. To address this, the IT team proposed implementing a machine learning (ML) system for instant powdery mildew detection in cherry tree images, with potential application to other crops if successful.

#### Business Requirements:
  ** Conduct a study to visually differentiate healthy cherry leaves from those with powdery mildew.
  ** Predict whether a cherry tree is healthy or afflicted with powdery mildew.

#### Project Dataset:
The dataset, comprising cherry leaf images provided by Farmy & Foods, forms the basis for model training and evaluation. This dataset, sourced from Kaggle: [https://www.kaggle.com/codeinstitute/cherry-leaves], consists of over 4,000 images, with a subset of XXX images chosen for expedited model training.

Additional Information:
For further details, refer to the following sources:

* [Wikipedia:](https://en.wikipedia.org/wiki/Powdery_mildew)
* [Additional Sources:](https://portal.ct.gov/CAES/Fact-Sheets/Plant-Pathology/Powdery-Mildew#:~:text=Powdery%20mildews%20are%20easily%20recognized,chains%20of%20spores%20(conidia))


![Page 1](/workspace/mildew-detection-in-cherry-leaves/Page1.jpg)

## Page 2: Leaf Visualiser 

### Answering Business requirement 1 : Conduct a study to visually differentiate healthy cherry leaves from those with powdery mildew.
  * Checkbox 1 - Difference between average and variability image
  * Checkbox 2 - Differences between average infected and average uninfected leaves.
  * Checkbox 3 - Image Montage

![Page 2](/workspace/mildew-detection-in-cherry-leaves/Page2.jpg)

## Page 3: Powdery Mildew Detector: 

### Answering Business requirement 2 : Predict whether a leaf is infected with powdery mildew or not. 

The analysis strategy involves developing a binary classifier and generating comprehensive reports to fulfill this objective.
We provide a link to download a dataset comprising images of leaves containing fungal infected and healthy leaves for real-time prediction.

The user interface features a file uploader widget enabling users to upload multiple leaf images. Upon upload, the interface displays each image alongside a prediction statement indicating whether the plant is infected with powdery mildew and the associated probability.

A table is presented showcasing the image names and corresponding prediction results for reference.
Additionally, users have the option to download the table for further analysis using the provided download button.

![Page 3](/workspace/mildew-detection-in-cherry-leaves/Page3.jpg)

## Page 4: Hypothesis and Validation:
### Hypothesis :

Plants affected by fungal infestation, specifically powdery mildew,
exhibit distinct visual characteristics on their leaves, such as light
grey or white powdery spots. 

### How to validate it: 

By conducting an average image study, we aim to investigate whether these visual markers 
reliably differentiate infected plants from healthy, uninfected ones.'

![Page 4](/workspace/mildew-detection-in-cherry-leaves/Page4.jpg)

## Page 5: ML Performance Metrics: 

* Label Frequencies for Train, Validation and Test Sets
* Model History - Accuracy and Losses
* Model evaluation result

![Page 5](/workspace/mildew-detection-in-cherry-leaves/page5.jpg)
 
---
## Deployment
### Heroku Deployment Steps:

1. Log in to your Heroku account or sign up if you don't have one.
2. Click the "New" button at the top right corner and choose "Create New App".
3. Provide a unique name for your application.
4. Select your preferred region.
5. Click "Create App".
6. Ensure that the chosen name aligns with your project's name.
7. Navigate to the deploy tab on Heroku and connect to your GitHub repository.
8. Select your repository name and click Search. Once it is found, click Connect.
9. Scroll down to the bottom of the deploy page.
10. To log into the Heroku toolbelt CLI:
 * In the terminal, run heroku_config
 * Paste in your API key when asked
 * Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported 
   version.
11. Come back to heroku 
12. Choose between enabling Automatic Deploys for automatic updates or manually deploying by clicking "Deploy Branch". Note: Manually deployed branches require redeployment whenever the GitHub repository is updated.
13. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
14. Click 'Open App' to view your deployed live site.
* **Your site is now live and accessible.**

* The App live link is:  [Powdery Mildew Detector](https://powdery-mildew-detector-fp-c8dd417a4db2.herokuapp.com/)

---
## Testing 
* The application underwent iterative development and was continuously tested throughout its development process. 
* All Python files underwent scrutiny using the CI linter Python checker.[CI](https://pep8ci.herokuapp.com/)
* Deployed app was tested on browsers like GoogleCrome, Firefox and Safari without issues.
* The small-screen dashboard on Android operated incorreclty, not loading the cover image. 

---
## Main Data Analysis and Machine Learning Libraries

### Languages Used:

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Editors and source control: 
* [Github](https://github.com/about) - Online storage of code.
* [Jupyter Notebooks](https://jupyter.org/about) - Editor notebooks 

### Dashboard or API:
* [Streamlit](https://streamlit.io/) - Used to create the Dashboard 

### Programs Used: 

* [Gitpod](https://www.gitpod.io/about) - IDE used to develop the code.
* [Heroku](https://www.heroku.com/about) - Cloud-based platform used to deploy the site.

### Data Analytics Packages:

* [NumPy](https://numpy.org/about/) - Numerical computing with Python
* [Pandas](https://pandas.pydata.org/about/) - Fro creating, using and manipulating DataFrames ans Series
* [Matplotlib](https://matplotlib.org/stable/) - Ploting charts 
* [SciPy](https://scipy.org/) - Providing algorithms for optimization 
* [Seaborn](https://seaborn.pydata.org/index.html) - Statistical data visualisation 
* [TensorFlow](https://www.tensorflow.org/about) n- ML models 
* [Scikitlearn](https://scikit-learn.org/stable/about.html) - Machine learning in python

### Installed Packages: 
* numpy==1.19.2
* pandas==1.1.2
* matplotlib==3.3.1
* seaborn==0.11.0
* plotly==4.12.0

* streamlit==0.85.0

* scikit-learn==0.24.2
* tensorflow-cpu==2.6.0
* keras==2.6.0
* protobuf==3.20
* altair<5
---

## Unresolved Bugs 
* All known bugs have been addressed. However, an ongoing concern revolves around the continuous deprecation of machine learning (ML) packages.
* Installing and maintaining the correct versions of ML packages has been challenging, as different versions often require compatibility adjustments. 

---
## Credits 

All content used for the project came from the school material and some internet forums stated under *Reference* section.
Thanks to fellow students in the slack chanel who read me, and specially A-Hoenig, who shared me their project when i was lost [here](https://github.com/A-Hoenig/student-AI)


---
## Content 

- The template used was from Code Institute learning material
- Cover image was obtained freely from [here](https://www.vecteezy.com/photo/17725783-closeup-of-wild-himalayan-cherry-flower-at-park)


---
## Acknowledgements:

Special thanks to Bianca, my partner, for their unwavering support and assistance in taking care of our child throughout the duration of this project.

Gratitude to myself for persevering and learning almost independently, with guidance from accelerated screencasts, during this period of development.

---
## References 
* [Powdery Mildew](https://www.gardendesign.com/how-to/powdery-mildew.html#:~:text=Powdery%20mildew%20is%20a%20common,%2C%20flowers%2C%20fruit%20or%20vegetables.)
* [Cmap colors](https://matplotlib.org/stable/gallery/color/colormap_reference.html)
* [Train,ValidationandTest](https://www.v7labs.com/blog/train-validation-test-set#h2)
* [DirectoryError](https://stackoverflow.com/questions/52338706/isadirectoryerror-errno-21-is-a-directory-it-is-a-file)
* [Spliting DataSet](https://towardsdatascience.com/how-to-split-a-dataset-into-training-and-testing-sets-b146b1649830#:~:text=The%20simplest%20way%20to%20split,the%20performance%20of%20our%20model.)
* [seaborn Scatterplot](https://towardsdatascience.com/7-points-to-create-better-scatter-plots-with-seaborn-9f0202fb2ba4)
* [Base64](https://www.cybrosys.com/blog/base64-encoding-and-decoding-using-python#:~:text=A%20built%2Din%20module%20in,string%20of%20printable%20ASCII%20characters.)
* [Subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html)
* [imread](https://www.askpython.com/python-modules/python-imread-opencv)
* [Local Variable](https://careerkarma.com/blog/python-local-variable-referenced-before-assignment/)
* [Image type](https://subscription.packtpub.com/book/data/9781789343731/1/ch01lvl1sec15/dealing-with-different-image-types-and-file-formats-and-performing-basic-image-manipulations)
* [Load Model](https://www.tensorflow.org/tutorials/keras/save_and_load)
* [st.file_uploader()](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)
* [Heroku-20](https://devcenter.heroku.com/articles/heroku-20-stack)
* [Clear Cache](https://pip.pypa.io/en/stable/cli/pip_cache/)
* [Git Clean](https://git-scm.com/docs/git-clean)
* [Image Resize](https://cloudinary.com/guides/bulk-image-resize/python-image-resize-with-pillow-and-opencv)
* [Links StreamLit](https://towardsdatascience.com/how-to-use-streamlits-st-write-function-to-improve-your-streamlit-dashboard-1586333eb24d)
* [Markup General](https://github.github.com/gfm/#images)
* [Image Upload to ReadME](https://www.educative.io/answers/adding-images-to-readmemd-in-github)
* [Incorrect Label](https://datascience.stackexchange.com/questions/115836/flipping-the-labels-in-a-binary-classification-gives-different-model-and-results)
* [Incorrect Label](https://datascience.stackexchange.com/questions/98206/how-to-correct-mislabeled-data-in-training-validation-and-test-set)
* [Model Performance](https://machinelearningmastery.com/different-results-each-time-in-machine-learning/)
* [Model Performance](https://www.linkedin.com/advice/3/how-can-you-improve-neural-network-performance-xkrxe#:~:text=Adjusting%20the%20number%20of%20epochs%20in%20a%20neural%20network%20training,the%20right%20balance%20is%20crucial.)
* [Loss and Acurracy](https://www.baeldung.com/cs/ml-loss-accuracy)
* [Learning Curve](https://www.baeldung.com/cs/learning-curve-ml)
