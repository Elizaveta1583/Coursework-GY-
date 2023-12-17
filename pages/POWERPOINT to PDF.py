import streamlit as st
import subprocess

file = st.file_uploader("Выберете POWERPOINT файл")

if file is not None:
    if file.type.split("/")[1] in ["pptx"]:
        process = st.button("convert")
        if process:
            subprocess.call(["unoconv", "-f", "pdf", "test.jpg"])
    else:
        st.warning(
            f"Файл не соответсвует формату.\nОжидемый формат: pptx\nПереданный формат: {file.type.split('/')[1]}"
        )
