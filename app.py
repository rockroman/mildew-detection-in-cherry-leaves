import streamlit as streamlit
from app_pages.multipage import multipage

# load the pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_leaf_visualizer import page_leaf_visualizer_body
from app_pages.page_powdery_mildew_detector import page_powdery_mildew_detector_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_ml_performance import page_ml_performance_metrics

app = MultiPage(app_name= "Powery Mildew Detector")

# Adding the pages with .add_page()

app.add_page("Project Summary", page_summary_body)
app.add_page("Leaf Visualizer", page_leaf_visualizer_body)
app.add_page("Powdery Mildew Detection", page_powdery_mildew_detector_body)
app.add_page("Project Hypothesis", page_project_hypothesis_body)
app.add_page("ML Performance Metrics", page_ml_performance_metrics)

app.run() #run the app 