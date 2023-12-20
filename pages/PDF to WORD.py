import streamlit as st
import os
from pdf2docx import Converter

file = st.file_uploader("Выберете PDF файл")

if file is not None:
    if file.type.split("/")[1] in ["pdf"]:
        process = st.button("convert")
        if process:
            with st.spinner("converting..."):
                file_name = file.name.split(".")[0]
                with open(f"./cache/{file_name}.pdf", "wb") as f:
                    f.write(file.getvalue())
                    f.close()
                pdf = f"./cache/{file_name}.pdf"
                docx = f"./cache/{file_name}.docx"
                cv = Converter(pdf)
                cv.convert(docx)
                cv.close()
                with open(docx, "rb") as file:
                    st.download_button(
                        "upload",
                        file_name=f"{file_name}.docx",
                        data=file,
                    )
                os.remove(docx)
                os.remove(pdf)
            st.success("Нажмите кнопку upload, чтобы загрузить сконвертированный файл")
    else:
        st.warning(
            f"Файл не соответсвует формату.\nОжидемый формат: pdf\nПереданный формат: {file.type.split('/')[1]}"
        )


