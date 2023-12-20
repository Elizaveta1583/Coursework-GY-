import streamlit as st
import os

file = st.file_uploader("Выберете PDF файл")

if file is not None:
    if file.type.split("/")[1] in ["pdf"]:
        process = st.button("convert")
        if process:
            with st.spinner("converting..."):
                file_name = file.name.split(".")[0]
                print(file_name)
                with open(f"./cache/{hash(file_name)}.pdf", "wb") as f:
                    f.write(file.getvalue())
                    f.close()
                os.system(f"pdf2pptx ./cache/{hash(file_name)}.pdf")
                with open(f"./cache/{hash(file_name)}.pptx", "rb") as file:
                    st.download_button(
                        "upload",
                        file_name=f"{file_name}.pptx",
                        data=file,
                    )
                os.remove(f"./cache/{hash(file_name)}.pdf")
                os.remove(f"./cache/{hash(file_name)}.pptx")
            st.success("Нажмите кнопку upload, чтобы загрузить сконвертированный файл")
    else:
        st.warning(
            f"Файл не соответсвует формату.\nОжидемый формат: pdf\nПереданный формат: {file.type.split('/')[1]}"
        )

