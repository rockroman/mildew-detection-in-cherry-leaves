import streamlit as st 

#This class generates a multiple page dashboard using (OOP)

class MultiPage;

    def __init__(self,app_name)-> None :
        self.pages=[]
        se;f.app_name = app_name

        st.set_page_config(
            page_title=self.spp_name,
            page_icon="🌱")

    def add_page(self, title, func) -> None:
        self.pages.append({'title': title, 'function': func})

    def run(self):
        st.title(self.app_name)
        page = st.sidebar.radio('Menu', self.pages, format_func=lambda page: page['title'])
        page['function']()