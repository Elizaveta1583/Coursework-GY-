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

# 1. import streamlit as st
# Этот код импортирует библиотеку streamlit, которая позволяет создавать интерактивные веб-приложения.

# 2. from pdf2jpg import pdf2jpg
# Код импортирует модуль pdf2jpg, который позволяет преобразовывать файлы PDF в файлы JPG.

# 3. from zipfile import ZipFile
# Модуль zipfile позволяет создавать и управлять ZIP-файлами.

# 4. from shutil import rmtree, make_archive
# Модуль shutil предоставляет функции для работы с файлами и каталогами, включая удаление и создание архивов.

# 5. import os
# Данный код импортирует библиотеку os, которая предоставляет функции для работы с операционной системой.

# 6. file = st.file_uploader("Выберете PDF файл")
# Функция file_uploader позволяет пользователям загружать файлы на веб-страницу. В данном случае, она ищет файлы PDF.

# 7. if file is not None:
# Это условие проверяет, был ли загружен файл. Если файл был загружен, то выполняется следующий код.

# 8. if file.type.split("/")1 in "pdf":
# Это условие проверяет, является ли загруженный файл файлом PDF. Если это так, то выполняется следующий код.

# 9. process = st.button("convert")
# Функция button создает кнопку с текстом "convert". Если пользователь нажимает на эту кнопку, то выполняется следующий код.

# 10. with st.spinner("converting..."):
# Функция spinner отображает индикатор загрузки на веб-странице.

# 11. file_name = file.name.split(".")0
# Этот код извлекает имя файла и удаляет расширение.

# 12. with open(f"./cache/{file_name}.pdf", "wb") as f:
# Функция open открывает файл для записи в двоичном формате.

# 13. f.write(file.getvalue())
# Функция write записывает содержимое файла в файл.

# 14. f.close()
# Функция close закрывает файл.

# 15. pdf = f"./cache/{file_name}.pdf"
# Этот код присваивает путь к файлу переменной pdf.

# 16. pdf2jpg.convert_pdf2jpg(pdf, f"./cache")
# Функция convert_pdf2jpg преобразует файл PDF в файлы JPG с использованием модуля pdf2jpg.

# 17. os.rename(f"./cache/{file_name}.pdf_dir", f"./cache/{file_name}")
# Функция rename переименовывает файл, удаляя суффикс "_dir" из имени файла.

# 18. make_archive(f"./cache/{file_name}", "zip", f"./cache/{file_name}")
# Функция make_archive создает архив ZIP с использованием модуля zipfile.

# 19. with open(f"./cache/{file_name}.zip", "rb") as file:
# Функция open открывает файл для чтения в двоичном формате.

# 20. st.download_button(
#     "upload",
#     file_name=f"{file_name}.zip",
#     data=file,
# )
# Функция download_button создает кнопку "upload", которая позволяет скачать файл ZIP.

# 21. os.remove(f"./cache/{file_name}.zip")
# Функция remove удаляет файл ZIP.

# 22. os.remove(f"./cache/{file_name}.pdf")
# Функция remove удаляет файл PDF.

# 23. rmtree(f"./cache/{file_name}")
# Функция remove_tree удаляет каталог "cache" с именем файла.

# 24. st.success("Нажмите кнопку upload, чтобы загрузить сконвертированный файл")
# Функция success отображает сообщение "Нажмите кнопку upload, чтобы загрузить сконвертированный файл" с использованием стилизованного элемента успеха.

# 25. else:
# Это условие проверяет, соответствует ли загруженный файл формату PDF. Если это не так, то выполняется следующий код.

# 26. st.warning(
#     f"Файл не соответсвует формату.\nОжидемый формат: pdf\nПереданный формат: {file.type.split('/')1}"
# )
# Функция warning отображает предупреждающее сообщение, указывающее на несоответствие формата файла.
