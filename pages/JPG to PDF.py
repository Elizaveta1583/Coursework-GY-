import streamlit as st
import jpg2pdf
import numpy as np
import cv2
import os

file = st.file_uploader("Выберете JPG файл")

if file is not None:
    if file.type.split("/")[1] in ["jpeg", "jpg"]:
        process = st.button("convert")
        if process:
            with st.spinner():
                file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
                opencv_image = cv2.imdecode(file_bytes, 1)
                file_name = file.name.split(".")[0]
                cv2.imwrite(f"./cache/{file_name}.jpg", opencv_image)
                with jpg2pdf.create(f"./cache/{file_name}.pdf") as pdf:
                    pdf.add(f"./cache/{file_name}.jpg")
                with open(f"./cache/{file_name}.pdf", "rb") as file:
                    st.download_button(
                        "upload",
                        file_name=f"{file_name}.pdf",
                        data=file,
                        mime="image/jpg",
                    )
                os.remove(f"./cache/{file_name}.jpg")
                os.remove(f"./cache/{file_name}.pdf")
            st.success("Нажмите кнопку upload, чтобы загрузить сконвертированный файл")
    else:
        st.warning(
            f"Файл не соответсвует формату.\nОжидемый формат: jpeg, jpg\nПереданный формат: {file.type.split('/')[1]}"
        )


