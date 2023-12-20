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

# 1. import streamlit as st
# Этот код импортирует библиотеку streamlit, которая позволяет создавать интерактивные веб-приложения.

# 2. import tabula
# Код импортирует модуль tabula, который позволяет преобразовывать файлы PDF в файлы CSV.

# 3. import os
# Данный код импортирует библиотеку os, которая предоставляет функции для работы с операционной системой.

# 4. file = st.file_uploader("Выберете PDF файл")
# Функция file_uploader позволяет пользователям загружать файлы на веб-страницу. В данном случае, она ищет файлы PDF.

# 5. if file is not None:
# Это условие проверяет, был ли загружен файл. Если файл был загружен, то выполняется следующий код.

# 6. if file.type.split("/")1 in "pdf":
# Это условие проверяет, является ли загруженный файл файлом PDF. Если это так, то выполняется следующий код.

# 7. process = st.button("convert")
# Функция button создает кнопку с текстом "convert". Если пользователь нажимает на эту кнопку, то выполняется следующий код.

# 8. with st.spinner("converting..."):
# Функция spinner отображает индикатор загрузки на веб-странице.

# 9. file_name = file.name.split(".")0
# Этот код извлекает имя файла и удаляет расширение.

# 10. with open(f"./cache/{file_name}.pdf", "wb") as f:
# Функция open открывает файл для записи в двоичном формате.

# 11. f.write(file.getvalue())
# Функция write записывает содержимое файла в файл.

# 12. f.close()
# Функция close закрывает файл.

# 13. pdf = f"./cache/{file_name}.pdf"
# Этот код присваивает путь к файлу переменной pdf.

# 14. tabula.convert_into(
#     pdf, f"./cache/{file_name}.csv", output_format="csv", pages="all"
# )
# Функция convert_into преобразует файл PDF в файл CSV с использованием модуля tabula.

# 15. with open(f"./cache/{file_name}.csv", "rb") as file:
# Функция open открывает файл для чтения в двоичном формате.

# 16. st.download_button(
#     "upload",
#     file_name=f"{file_name}.csv",
#     data=file,
# )
# Функция download_button создает кнопку "upload", которая позволяет скачать файл CSV.

# 17. os.remove(f"./cache/{file_name}.csv")
# Функция remove удаляет файл CSV.

# 18. os.remove(f"./cache/{file_name}.pdf")
# Функция remove удаляет файл PDF.

# 19. st.success("Нажмите кнопку upload, чтобы загрузить сконвертированный файл")
# Функция success отображает сообщение "Нажмите кнопку upload, чтобы загрузить сконвертированный файл" с использованием стилизованного элемента успеха.

# 20. else:
# Это условие проверяет, соответствует ли загруженный файл формату PDF. Если это не так, то выполняется следующий код.

# 21. st.warning(
#     f"Файл не соответсвует формату.\nОжидемый формат: pdf\nПереданный формат: {file.type.split('/')1}"
# )
# Функция warning отображает предупреждающее сообщение, указывающее на несоответствие формата файла.
