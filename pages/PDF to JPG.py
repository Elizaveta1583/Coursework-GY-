import streamlit as st
from pdf2jpg import pdf2jpg
from zipfile import ZipFile
from shutil import rmtree, make_archive
import os

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
                pdf2jpg.convert_pdf2jpg(pdf, f"./cache")
                os.rename(f"./cache/{file_name}.pdf_dir", f"./cache/{file_name}")
                make_archive(f"./cache/{file_name}", "zip", f"./cache/{file_name}")
                with open(f"./cache/{file_name}.zip", "rb") as file:
                    st.download_button(
                        "upload",
                        file_name=f"{file_name}.zip",
                        data=file,
                    )
                os.remove(f"./cache/{file_name}.zip")
                os.remove(f"./cache/{file_name}.pdf")
                rmtree(f"./cache/{file_name}")
            st.success("Нажмите кнопку upload, чтобы загрузить сконвертированный файл")
    else:
        st.warning(
            f"Файл не соответсвует формату.\nОжидемый формат: pdf\nПереданный формат: {file.type.split('/')[1]}"
        )


