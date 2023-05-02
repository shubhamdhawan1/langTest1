import streamlit as st




st.title("Test 1")
st.subheader("Lets Input Data")
# st.date_input()


import pandas as pd
from io import StringIO

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    # bytes_data = uploaded_file.getvalue()
    # st.write(bytes_data)

    # To convert to a string based IO:
    # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # st.write(stringio)

    # # To read file as string:
    # string_data = stringio.read()
    # st.write(string_data)

    # # Can be used wherever a "file-like" object is accepted:
    # dataframe = pd.read_csv(uploaded_file)
    # st.write(dataframe)
    # st.write(uploaded_file.name.split('.')[1])
    # st.write(type(uploaded_file.name))
    if(uploaded_file.name.split('.')[1]=='csv'):
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)
        st.write(uploaded_file)
    if(uploaded_file.name.split('.')[1]=='text'):
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        st.write(stringio)