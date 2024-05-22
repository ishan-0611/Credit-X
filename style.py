import streamlit as st
import streamlit.components.v1 as components

info_string = '''
**CreditX** is a comprehensive financial management application designed to help users efficiently **manage their credit cards,
make payments, and track their expenditures**. 
'''

string = '''
By providing **insightful spending analytics** and payment reminders, 
CreditX empowers users to take **control** of their **financial health** and make informed financial decisions.
'''


def center_text(text, tag="h1"):
    st.markdown(f"<div style='text-align: center;'><{tag}>{text}</{tag}></div>", unsafe_allow_html=True)


def hide_page_names():
    """Hides the page navigation element in the sidebar using CSS."""
    style = """
        <style>
        [data-testid="stSidebarNav"] {
            display: none;
        }
        </style>
        """
    components.html(style, unsafe_allow_html=True)
