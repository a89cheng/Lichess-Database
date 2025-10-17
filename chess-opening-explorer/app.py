import streamlit as st
import chess.pgn
#import pandas
#import python-chess
#import matplotlib

#Key concepts:
#st.title("My App") → shows a big title in the browser
#st.write("Hello!") → prints text
#st.file_uploader("Upload PGN") → lets users upload files
#st.dataframe(my_data) → shows tables
#st.bar_chart(my_data) → makes simple charts
#st.title("Chess Opening Explorer Test")

while True:
    pgnfile = st.file_uploader("Upload PGN")
    if pgnfile is not None: 
        st.write("File is uploaded!")
    else:
        st.write("File is not uploaded. Try again!")

pgn = open("pgnfile.pgn")  # your uploaded PGN file
games = []  # store game info dictionaries


""""""
data = pgnfile.read()  # bytes

lines = text.splitlines()
st.write(lines[:10])  # show first 10 lines

text = data.decode("utf-8")  # string and "utf-8" tells the computer how to convert those 0s and 1s back into human-readable characters
st.write(text[:100])  # first 100 characters
""""""

#PGN Subheadings typically include:
#Typical headers are:
#Event, Site, Date
#White, Black
#Result
#Opening, ECO