#!/bin/bash

# Install necessary packages with specific options
pip install numpy==1.26.2 --no-deps
pip install pandas==2.1.3 --no-deps
pip install plotly==5.18.0 --no-deps
pip install matplotlib==3.8.2 --no-deps
pip install streamlit==1.28.2 --no-deps
pip install seaborn==0.13.0 --no-deps
pip install scikit-learn==1.3.2 --no-deps
pip install tensorflow-cpu==2.16.0rc0 --no-deps
pip install keras==3.7.0 --no-deps
pip install protobuf==4.25.1 --no-deps
pip install altair==5.1.2 --no-deps


mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
