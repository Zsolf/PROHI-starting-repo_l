import streamlit as st

st.set_page_config(
    page_title="PROHI Dashboard",
    page_icon="👋",
)

# Sidebar configuration
st.sidebar.success("Select a tab above.")

# # Page information

st.write("# Welcome to Assigment 2 👋")

st.markdown(
"""
    ## Lorem Ipsum

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
     Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
     Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
     Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

"""
)



### UNCOMMENT THE CODE BELOW TO SEE EXAMPLE OF INPUT WIDGETS

"# Dataframe management"
import numpy as np

add_slider = st.slider(
'Select values for the number of rows and columns in the dataframe',
0.0, 100.0, (25.0, 75.0)
)

dataframe = np.random.randn(int(add_slider[0]), int(add_slider[1]))
st.dataframe(dataframe)

"## Basic charting"

st.area_chart(dataframe)

st.text_area("What do you think about this chart?", "Type Here...")

st.button("Refresh")

