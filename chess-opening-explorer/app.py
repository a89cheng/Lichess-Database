import streamlit as st
import chess.pgn
import chess
import pandas as pd
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

#pgn = open("pgnfile.pgn")  # your uploaded PGN file | is completely unecessary to open file... doesn't exist on disk?

"""
The games list below isolates all the games in the PGN into individual ones
The game_info goes through all the games in the list "games" and takes the header information
This is a 2 step process of isolating the games and then extracting the data
"""
games = []  # store game info dictionaries

while True:
    game = chess.pgn.read_game(pgn) #Would assume that the function read_game reads only 1 game at a time hence, the games are stored accordingly
    if game is None:  # means end of file, this si done by default by python-chess
        break
    games.append(game) #Games are added to the game list and the headers will be stored in dictionaries

game_info = []

for game in games: #For all games in a single pgn file...
    headers = game.headers
    game_info.append({
        "White": headers.get("White", "Unknown"),
        "Black": headers.get("Black", "Unknown"),
        "Result": headers.get("Result", "Unknown"),
        "Opening": headers.get("Opening", "Unknown"),
    }) #The headers are extracted and set equivalent to whatever they are in the game...


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