![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Codeanywhere Template Instructions

Welcome,

This is the Code Institute student template for Codeanywhere. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions. Click the `Use this template` button above to get started.

You can safely delete the Codeanywhere Template Instructions section of this README.md file,  and modify the remaining paragraphs for your own project. Please do read the Codeanywhere Template Instructions at least once, though! It contains some important information about the IDE and the extensions we use. 

## How to use this repo

1. Use this template to create your GitHub project repo

1. Log into <a href="https://app.codeanywhere.com/" target="_blank" rel="noreferrer">CodeAnywhere</a> with your GitHub account.

1. On your Dashboard, click on the New Workspace button

1. Paste in the URL you copied from GitHub earlier

1. Click Create

1. Wait for the workspace to open. This can take a few minutes.

1. Open a new terminal and <code>pip3 install -r requirements.txt</code>

1. In the terminal type <code>pip3 install jupyter</code>

1. In the terminal type <code>jupyter notebook --NotebookApp.token='' --NotebookApp.password=''</code> to start the jupyter server.

1. Open port 8888 preview or browser

1. Open the jupyter_notebooks directory in the jupyter webpage that has opened and click on the notebook you want to open.

1. Click the button Not Trusted and choose Trust.

Note that the kernel says Python 3. It inherits from the workspace so it will be Python-3.8.12 as installed by our template. To confirm this you can use <code>! python --version</code> in a notebook code cell.


## Cloud IDE Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.


## Dataset Content

* Dataset was obtained from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). Subsequently,  a hypothetical user scenario was created to demonstrate the practical application of predictive analytics in a workplace project.
* The dataset comprises over 4,000 images captured from the client's crop fields. These images depict both healthy cherry leaves and leaves afflicted with powdery mildew, a fungal disease that poses a threat to numerous plant species. Given the cherry plantation's significance within their product portfolio, the company is deeply invested in ensuring the market receives products of uncompromised quality.



## Business Requirements

* The cherry plantation at Farmy & Foods faces a challenge with powdery mildew affecting their cherry trees. Currently, manual inspection takes around 30 minutes per tree, with an additional minute for applying treatment if needed. With thousands of trees across multiple farms, this process is not scalable. To address this, the IT team proposed implementing an ML system to instantly detect powdery mildew in cherry tree images. If successful, this approach could be extended to other crops. The dataset comprises cherry leaf images provided by Farmy & Foods.

# Business Requirement number 1:
* Conduct a study to visually differentiate healthy cherry leaves from those with powdery mildew.
# Business Requirement number 2:
* Predict whether a cherry tree is healthy or afflicted with powdery mildew.

# Client Benefits:
* Automated Mildew Detection: The ML model will automatically diagnose mildew presence in cherry leaves.
Reduced Manual Work: Manual disease diagnosis processes will be significantly streamlined, saving time and resources.
Early Disease Detection: Early detection of mildew allows for timely treatment, preventing further spread and damage.
# Client Goals:
* Faster Testing Results: Expedite the process of obtaining disease test results.
* Reduced Manual Workload: Minimize manual effort required for diagnosing mildew infection.
* Mildew Mitigation: Prevent the spread and recurrence of mildew infection in cherry trees.

## Hypothesis and how to validate?
* Hypothesis: 
Plants affected by fungal infestation, specifically powdery mildew, exhibit distinct visual characteristics on their leaves, such as light grey or white powdery spots. By conducting an average image study, we aim to investigate whether these visual markers reliably differentiate infected plants from healthy, uninfected ones."


## The rationale to map the business requirements to the Data Visualisations and ML tasks

* The project will follow the ML lifecycle, encompassing the following stages:
  ** Information Gathering & Data Collection: Gather and understand relevant data from the client.
  ** Data Visualization, Cleaning & Preparation: Preprocess and prepare the data for model training.
  ** Model Training, Validation & Optimization: Train, validate, and refine the ML model for optimal performance.
  ** Dashboard Planning, Design & Development: Design and develop the user interface for the dashboard.
  ** Dashboard Deployment & Release: Deploy and release the final solution to the client.

# Business Requirement 1: Data Visualization

* The dashboard will showcase "mean" and "standard deviation" images for both infected and uninfected leaves. 
* It will also illustrate the disparity between an average infected leaf and a healthy one. 
* Additionally, the dashboard will feature an image montage highlighting either infected or uninfected leaves.


# Business Requirement 2: Classification

* Our objective is to predict whether a leaf is infected with powdery mildew or not. To achieve this, we aim to develop a binary classifier and generate comprehensive reports.

# ML Business Case: Powdery Mildew Classification

Our aim is to develop a machine learning model capable of accurately predicting whether a leaf is infected with Powdery Mildew or not, using historical image data. This supervised model is designed as a binary classifier, distinguishing between infected and uninfected leaves.

The ultimate goal is to provide Farmy & Foods with a rapid and dependable diagnostic tool for identifying Powdery Mildew-infected leaves. The success of the model will be measured against a minimum accuracy threshold of 97% on the test set.

The model's output will consist of a binary flag indicating the presence or absence of Powdery Mildew, along with the associated probability of infection. To streamline the process, employees will capture leaf images manually and upload them to the application, enabling real-time predictions rather than batch processing.

Currently, the manual diagnostic process is time-consuming, with employees spending up to 30 minutes per plant to identify signs of infestation. Additionally, applying treatment to infected leaves consumes an additional minute. Human error in visual criteria assessment further adds to the risk of inaccurate diagnostics. With thousands of cherry trees spread across multiple farms, scalability becomes a significant concern.

The dataset, comprising cherry leaf images provided by Farmy & Foods, serves as the foundation for model training and evaluation. This dataset, sourced from Kaggle: [https://www.kaggle.com/codeinstitute/cherry-leaves] contains over 4,000 images, with a subset of XXX images selected for expedited model training.

Train data: Target - infected or not; Features - all leaf images.


## Dashboard Design (Streamlit App User Interface)
# Page 1: Project Overview

* General Information:
  **Powdery Mildew, a common fungus, affects a wide array of plants, manifesting as light grey or white powdery spots primarily on leaves but also on stems, flowers, fruits, and vegetables. The spread of these spots progressively covers most leaves, particularly impacting new plant growth.

  **While seldom fatal, unchecked powdery mildew can inflict serious harm by depriving plants of water and nutrients. Typical effects include yellowing, withering, or distortion of leaves, along with weakened growth, reduced blooming, and slower development.

  **Currently, manual inspection of each tree requires approximately 30 minutes, with an additional minute per tree for treatment application if necessary. This process, given the multitude of trees across various farms, lacks scalability. To address this, the IT team proposed implementing a machine learning (ML) system for instant powdery mildew detection in cherry tree images, with potential application to other crops if successful.

* Project Dataset:
  ** The dataset, comprising cherry leaf images provided by Farmy & Foods, forms the basis for model training and evaluation. This dataset, sourced from Kaggle: [https://www.kaggle.com/codeinstitute/cherry-leaves], consists of over 4,000 images, with a subset of XXX images chosen for expedited model training.

* Additional Information:
For further details, refer to the following sources:

  ** Wikipedia: [https://en.wikipedia.org/wiki/Powdery_mildew]
  ** Additional Sources: [https://portal.ct.gov/CAES/Fact-Sheets/Plant-Pathology/Powdery-Mildew#:~:text=Powdery%20mildews%20are%20easily%20recognized,chains%20of%20spores%20(conidia)]

* Business Requirements:
  ** Conduct a study to visually differentiate healthy cherry leaves from those with powdery mildew.
  ** Predict whether a cherry tree is healthy or afflicted with powdery mildew.

# Page 2: Leaf Visualiser 

* Answering Business requirement 1 : Conduct a study to visually differentiate healthy cherry leaves from those with powdery mildew.
    ** Checkbox 1 - Difference between average and variability image
    ** Checkbox 2 - Differences between average infected and average uninfected leaves.
    ** Checkbox 3 - Image Montage

# Page 3: Powdery Mildew Detector: 

* Answering Business requirement 2 : Predict whether a leaf is infected with powdery mildew or not. 
    ** The analysis strategy involves developing a binary classifier and generating comprehensive reports to fulfill this objective.
    ** We provide a link to download a dataset comprising images of leaves containing fungal infections and uninfected leaves for real-time prediction.
    ** The user interface features a file uploader widget enabling users to upload multiple leaf images. Upon upload, the interface displays each image alongside a prediction statement indicating whether the plant is infected with powdery mildew and the associated probability.
    ** A table is presented showcasing the image names and corresponding prediction results for reference.
    ** Additionally, users have the option to download the table for further analysis using the provided download button.

# Page 4: A page indicating your project hypothesis and how you validated it across the project.

# Page 5: ML Performance Metrics: 

* Label Frequencies for Train, Validation and Test Sets
* Model History - Accuracy and Losses
* Model evaluation result


## Unfixed Bugs
* You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file. 


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.



## Acknowledgements (optional)
* Thank the people that provided support throughout this project.


## References 
* https://www.gardendesign.com/how-to/powdery-mildew.html#:~:text=Powdery%20mildew%20is%20a%20common,%2C%20flowers%2C%20fruit%20or%20vegetables.
* [Cmap colors](https://matplotlib.org/stable/gallery/color/colormap_reference.html)
* [Train,ValidationandTest](https://www.v7labs.com/blog/train-validation-test-set#h2)
* [DirectoryError](https://stackoverflow.com/questions/52338706/isadirectoryerror-errno-21-is-a-directory-it-is-a-file)
* [Spliting DataSet](https://towardsdatascience.com/how-to-split-a-dataset-into-training-and-testing-sets-b146b1649830#:~:text=The%20simplest%20way%20to%20split,the%20performance%20of%20our%20model.)
* [seaborn Scatterplot](https://towardsdatascience.com/7-points-to-create-better-scatter-plots-with-seaborn-9f0202fb2ba4)
* [Base64](https://www.cybrosys.com/blog/base64-encoding-and-decoding-using-python#:~:text=A%20built%2Din%20module%20in,string%20of%20printable%20ASCII%20characters.)
* [Subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html)
* [imread()](https://www.askpython.com/python-modules/python-imread-opencv)(https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imread.html)
* [Local Variable](https://careerkarma.com/blog/python-local-variable-referenced-before-assignment/)
* [Image type](https://subscription.packtpub.com/book/data/9781789343731/1/ch01lvl1sec15/dealing-with-different-image-types-and-file-formats-and-performing-basic-image-manipulations)
* [Load Model](https://www.tensorflow.org/tutorials/keras/save_and_load)
* [st.file_uploader()](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)
* [Heroku-20](https://devcenter.heroku.com/articles/heroku-20-stack)
* [Clear Cache](https://pip.pypa.io/en/stable/cli/pip_cache/)
* [Git Clean](https://git-scm.com/docs/git-clean)
* [Image Resize](https://cloudinary.com/guides/bulk-image-resize/python-image-resize-with-pillow-and-opencv)
