import streamlit as st
import os
from docx2pdf import convert

file = st.file_uploader("Выберете WORD файл")

if file is not None:
    if file.name.split(".")[1] in ["docx", "doc"]:
        process = st.button("convert")
        if process:
            with st.spinner("converting..."):
                file_name = file.name.split(".")[0]
                with open(f"./cache/{file_name}.docx", "wb") as f:
                    f.write(file.getvalue())
                    f.close()
                pdf = f"./cache/{file_name}.pdf"
                docx = f"./cache/{file_name}.docx"
                convert(f"./cache/{docx}", f"./cache/{pdf}")
                with open(pdf, "rb") as file:
                    st.download_button(
                        "upload",
                        file_name=f"{file_name}.pdf",
                        data=file,
                    )
                os.remove(docx)
                os.remove(pdf)
            st.success("Нажмите кнопку upload, чтобы загрузить сконвертированный файл")
    else:
        st.warning(
            f"Файл не соответсвует формату.\nОжидемый формат: docx, doc\nПереданный формат: {file.type.split('/')[1]}"
        )


