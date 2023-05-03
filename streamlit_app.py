import streamlit as st

st.title("Test 1")
st.subheader("Lets Input Data")
# st.date_input()

import csv
import pandas as pd
from io import StringIO
# from langchain.document_loaders.csv_loader import CSVLoader

def csv_reader(file):
    dataframe = pd.read_csv(file)
    st.write(dataframe)

# def csv_reader(file, delimiter = ',', quotechar = '"', escapechar = None, doublequote = True,skipinitialspace = False, lineterminator = '\r\n', quoting = 'QUOTE_MINIMAL'):
#     # loader = CSVLoader(file_path='./example_data/mlb_teams_2012.csv')
#     loader = CSVLoader(file_path=file)
#     data = loader.load()
#     st.write(data)


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
        csv_reader(uploaded_file)
    if(uploaded_file.name.split('.')[1]=='txt'):
        bytes_data = uploaded_file.getvalue()
        st.write(bytes_data)



st.write("By Shubham Dhawan")