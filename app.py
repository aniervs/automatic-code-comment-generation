import streamlit as st
from generate_comments import generate_comment
from utils.language_detector import detect_language

st.title("Code Automatic comments")

code = st.text_area("Enter your code to add comments:", height=300)


if st.button("Run"):
    language = detect_language(code)
    st.write(f"You entered code in {language}.")
    language = language.lower()
    
    commented_code = generate_comment(code, language)
    st.code(commented_code, language=language)
