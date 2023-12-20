import streamlit as st
import os
from csv2pdf import convert

file = st.file_uploader("Выберете CSV файл")

if file is not None:
    if file.type.split("/")[1] in ["csv"]:
        process = st.button("convert")
        if process:
            with st.spinner("converting..."):
                file_name = file.name.split(".")[0]
                with open(f"./cache/{file_name}.csv", "wb") as f:
                    f.write(file.getvalue())
                    f.close()
                csv = f"./cache/{file_name}.csv"
                print("process started")
                convert(
                    f"./cache/{file_name}.csv",
                    f"./cache/{file_name}.pdf",
                    delimiter="&",
                    orientation="L",
                )
                print("process complete")
                with open(f"./cache/{file_name}.pdf", "rb") as file:
                    st.download_button(
                        "upload",
                        file_name=f"{file_name}.pdf",
                        data=file,
                    )
                os.remove(f"./cache/{file_name}.pdf")
                os.remove(f"./cache/{file_name}.csv")
            st.success("Нажмите кнопку upload, чтобы загрузить сконвертированный файл")
    else:
        st.warning(
            f"Файл не соответсвует формату. Ожидемый формат: csv. Переданный формат: {file.name.split('.')[1]}"
        )


