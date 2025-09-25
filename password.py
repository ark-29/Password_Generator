import streamlit as st
import random 
import string
import pyperclip


st.markdown(""" 
            <link href="https://fonts.googleapis.com/css2?family=Audiowide&family=Barrio&family=Bitcount+Single+Ink:wght@100..900&family=Fascinate&display=swap" rel="stylesheet">
            <h1 style='font-family:"Audiowide";color:white'>Password Generator</h1>
            """,unsafe_allow_html=True)
        
st.header("     ")

choice=st.radio("Choose option:",["Random","Custom"])
if choice=="Random":
    if st.button("Generate"):
        if choice=="Random":
            password=""
            characters=string.ascii_letters
            characters+=string.digits

            for i in range(8):
                password+=random.choice(characters)
            col1,col2=st.columns([8,1.25])
            with col1:
                st.success(password)
            with col2:
                pyperclip.copy(password)
                st.info("Copied!")


if choice=="Custom":
    email=st.text_input("Enter your mail")
    characters=string.ascii_letters
    characters+=string.digits
    if st.button("Submit"):
        if "@" in email:
            first_name=email.split("@")[0]
            domain=email.split("@")[1]
            if domain in ["gmail.com","yahoo.com","outlook.com","raghuenggcollege.in"]:
                password=first_name[:6:]
                password+='_'
                for i in range(6):
                    password+=random.choice(characters)
                col1,col2=st.columns([8,1.25])
                with col1:
                    st.success(password)
                with col2:
                    pyperclip.copy(password)
                    st.info("Copied!")
            else:
                st.error("Enter a valid mail")
        elif "@" not in email:
            st.error("enter a valid mail")
        