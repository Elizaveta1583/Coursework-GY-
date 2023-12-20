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


# 1. import streamlit as st
# Этот код импортирует библиотеку streamlit, которая позволяет создавать интерактивные веб-приложения.

# 2. import jpg2pdf
# Код импортирует модуль jpg2pdf, который позволяет преобразовывать файлы JPG в файлы PDF.

# 3. import numpy as np
# Модуль numpy предоставляет функции для работы с массивами и математическими операциями.

# 4. import cv2
# Код импортирует библиотеку OpenCV, которая позволяет работать с изображениями.

# 5. import os
# Данный код импортирует библиотеку os, которая предоставляет функции для работы с операционной системой.

# 6. file = st.file_uploader("Выберете JPG файл")
# Функция file_uploader позволяет пользователям загружать файлы на веб-страницу. В данном случае, она ищет файлы JPG.

# 7. if file is not None:
# Это условие проверяет, был ли загружен файл. Если файл был загружен, то выполняется следующий код.

# 8. if file.type.split("/")1 in "jpeg", "jpg":
# Это условие проверяет, является ли загруженный файл файлом JPG. Если это так, то выполняется следующий код.

# 9. process = st.button("convert")
# Функция button создает кнопку с текстом "convert". Если пользователь нажимает на эту кнопку, то выполняется следующий код.

# 10. with st.spinner():
# Функция spinner отображает индикатор загрузки на веб-странице.

# 11. file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
# Этот код считывает файл и преобразует его содержимое в массив байтов.

# 12. opencv_image = cv2.imdecode(file_bytes, 1)
# Функция imdecode декодирует изображение из массива байтов в объекте OpenCV.

# 13. file_name = file.name.split(".")0
# Этот код извлекает имя файла и удаляет расширение.

# 14. cv2.imwrite(f"./cache/{file_name}.jpg", opencv_image)
# Функция imwrite записывает изображение в файл с использованием модуля OpenCV.

# 15. with jpg2pdf.create(f"./cache/{file_name}.pdf") as pdf:
# Этот код создает новый PDF-документ с помощью функции create из модуля jpg2pdf.

# 16. pdf.add(f"./cache/{file_name}.jpg")
# Функция add добавляет изображение в PDF-документ.

# 17. with open(f"./cache/{file_name}.pdf", "rb") as file:
# Функция open открывает файл для чтения в двоичном формате.

# 18. st.download_button(
#     "upload",
#     file_name=f"{file_name}.pdf",
#     data=file,
#     mime="image/jpg",
# )
# Функция download_button создает кнопку "upload", которая позволяет скачать файл PDF.

# 19. os.remove(f"./cache/{file_name}.jpg")
# Функция remove удаляет файл JPG.

# 20. os.remove(f"./cache/{file_name}.pdf")
# Функция remove удаляет файл PDF.

# 21. st.success("Нажмите кнопку upload, чтобы загрузить сконвертированный файл")
# Функция success отображает сообщение "Нажмите кнопку upload, чтобы загрузить сконвертированный файл" с использованием стилизованного элемента успеха.
