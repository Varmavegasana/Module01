import streamlit as st

#load EDA Pkgs
import pandas as pd


# display data
df = pd.read_csv("iris.csv")

# Method
st.dataframe(df)

# Working with Widgets
#Buttons/Radio/Checkbox/Select

name = "jesse"

# st.button("Submit")

if st.button("Submit"):
	st.write("Name: {}".format(name.upper()))

if st.button("Submit",key='new02'):
	st.write("First Name: {}".format(name.lower()))

    
#select/Multiple select
my_lang = {"Python","Julia","Go","Rust"}

choice = st.selectbox("Language",my_lang)
st.write("You Selected {}".format(choice))

#Multiple selection
spoken_lang = ("English","French","Spanish","Twi")
my_spoken_lang = st.multiselect("Spoken Lang",spoken_lang,default="English")

#slider
#Any datatpe(Int/Float?data)
age = st.slider("Age",1,100)

#Any datatype
#select slider
close = st.select_slider("choose color",options={"yellow","red","blue","black"})
