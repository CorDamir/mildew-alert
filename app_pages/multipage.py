# Code in this file is NOT my work
# This entire file was copied from Code Institute's lesson project
# on the following link:
# https://github.com/Code-Institute-Solutions/WalkthroughProject01/blob/main/app_pages/multipage.py

import streamlit as st


# Class to generate multiple Streamlit pages using an object oriented approach
class MultiPage:

    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title=self.app_name,
            page_icon=":herb:")  # You may add an icon, to personalize your App
        # check links below for additional icons reference
        # https://docs.streamlit.io/en/stable/api.html#streamlit.set_page_config
        # https://twemoji.maxcdn.com/2/test/preview.html

    def add_page(self, title, func) -> None:
        self.pages.append({"title": title, "function": func})

    def run(self):
        st.title(self.app_name)
        page = st.sidebar.radio(
            'Menu', self.pages, format_func=lambda page: page['title']
            )
        page['function']()
