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


# 1. import streamlit as st
# Этот код импортирует библиотеку streamlit, которая позволяет создавать интерактивные веб-приложения.

# 2. import os
# Данный код импортирует библиотеку os, которая предоставляет функции для работы с операционной системой.

# 3. from csv2pdf import convert
# Код импортирует функцию convert из модуля csv2pdf, которая преобразует файлы CSV в файлы PDF.

# 4. file = st.file_uploader("Выберете EXCEL файл")
# Функция file_uploader позволяет пользователям загружать файлы на веб-страницу. В данном случае, она ищет файлы Excel.

# 5. if file is not None:
# Это условие проверяет, был ли загружен файл. Если файл был загружен, то выполняется следующий код.

# 6. if file.type.split("/")1 in "csv":
# Это условие проверяет, является ли загруженный файл файлом CSV. Если это так, то выполняется следующий код.

# 7. process = st.button("convert")
# Функция button создает кнопку с текстом "convert". Если пользователь нажимает на эту кнопку, то выполняется следующий код.

# 8. with st.spinner("converting..."):
# Функция spinner отображает индикатор загрузки на веб-странице.

# 9. file_name = file.name.split(".")0
# Этот код извлекает имя файла и удаляет расширение.

# 10. with open(f"./cache/{file_name}.csv", "wb") as f:
# Функция open открывает файл для записи в двоичном формате.

# 11. f.write(file.getvalue())
# Функция write записывает содержимое файла в файл.

# 12. f.close()
# Функция close закрывает файл.

# 13. csv = f"./cache/{file_name}.csv"
# Этот код присваивает путь к файлу переменной csv.

# 14. print("process started")
# Функция print выводит сообщение "process started" в консоль.

# 15. convert(
#     f"./cache/{file_name}.csv",
#     f"./cache/{file_name}.pdf",
#     delimiter="&",
#     orientation="L",
# )
# Функция convert преобразует файл CSV в файл PDF.

# 16. print("process complete")
# Функция print выводит сообщение "process complete" в консоль.

# 17. with open(f"./cache/{file_name}.pdf", "rb") as file:
# Функция open открывает файл для чтения в двоичном формате.

# 18. st.download_button(
#     "upload",
#     file_name=f"{file_name}.pdf",
#     data=file,
# )
# Функция download_button создает кнопку "upload", которая позволяет скачать файл PDF.

# 19. os.remove(f"./cache/{file_name}.pdf")
# Функция remove удаляет файл PDF.

# 20. os.remove(f"./cache/{file_name}.csv")
# Функция remove удаляет файл CSV.

# 21. st.success("Нажмите кнопку upload, чтобы загрузить сконвертированный файл")
# Функция success отображает сообщение "Нажмите кнопку upload, чтобы загрузить сконвертированный файл" с использованием стилизованного элемента успеха.
