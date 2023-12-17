import streamlit as st

file = st.file_uploader("Выберете WORD файл")

if file is not None:
    if file.type.split("/")[1] in ["docs", "doc"]:
        process = st.button("convert")
        if process:
            pass
    else:
        st.warning(
            f"Файл не соответсвует формату.\nОжидемый формат: docs, doc\nПереданный формат: {file.type.split('/')[1]}"
        )
