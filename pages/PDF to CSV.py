import streamlit as st
import tabula
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
                tabula.convert_into(
                    pdf, f"./cache/{file_name}.csv", output_format="csv", pages="all"
                )
                with open(f"./cache/{file_name}.csv", "rb") as file:
                    st.download_button(
                        "upload",
                        file_name=f"{file_name}.csv",
                        data=file,
                    )
                os.remove(f"./cache/{file_name}.csv")
                os.remove(f"./cache/{file_name}.pdf")
            st.success("Нажмите кнопку upload, чтобы загрузить сконвертированный файл")
    else:
        st.warning(
            f"Файл не соответсвует формату.\nОжидемый формат: pdf\nПереданный формат: {file.type.split('/')[1]}"
        )


