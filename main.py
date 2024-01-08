import streamlit as st
import logging
import cofounder
import calculator

#logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logging.basicConfig(encoding='utf-8', level=logging.INFO)

PAGES = {
    "Cofounder": cofounder,
    "Calculator": calculator
}

def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Available Apps", list(PAGES.keys()))
    page = PAGES[selection]
    page.app()

if __name__ == "__main__":
    main()
