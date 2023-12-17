import streamlit as st

file = st.file_uploader("Выберете EXCEL файл")

if file is not None:
    if file.type.split("/")[1] in ["csv"]:
        process = st.button("convert")
    else:
        st.warning(
            f"Файл не соответсвует формату. Ожидемый формат: xlsx, xls. Переданный формат: {file.type.split('/')[1]}"
        )
