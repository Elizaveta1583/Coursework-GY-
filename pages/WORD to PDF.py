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


# 1. import streamlit as st
# Этот код импортирует библиотеку streamlit, которая позволяет создавать интерактивные веб-приложения.

# 2. import os
# Этот код импортирует библиотеку os, которая позволяет работать с операционной системой, в частности, с файлами и директориями.

# 3. from docx2pdf import convert
# Этот код импортирует функцию convert из библиотеки docx2pdf, которая позволяет конвертировать файлы Word в формат PDF.

# 4. file = st.file_uploader("Выберете WORD файл")
# Этот код предлагает пользователю выбрать файл Word для конвертации.

# 5. if file is not None:
# Это условие проверяет, был ли выбран файл. Если файл не был выбран, то код пропускает выполнение.

# 6. if file.name.split(".")1 in "docx", "doc":
# Это условие проверяет, имеет ли имя файла расширение ".docx" или ".doc", что означает, что файл является файлом Word.

# 7. process = st.button("convert")
# Этот код предлагает пользователю нажать кнопку "convert". Если пользователь нажимает кнопку, то код продолжает выполнение.

# 8. if process:
# Это условие проверяет, была ли нажата кнопка "convert". Если кнопка была нажата, то код продолжает выполнение.

# 9. with st.spinner("converting..."):
# Этот код отображает индикатор выполнения во время процесса конвертации.

# 10. file_name = file.name.split(".")0
# Этот код извлекает имя файла без расширения из имени входного файла.

# 11. with open(f"./cache/{file_name}.docx", "wb") as f:
# Этот код открывает файл с именем {file_name}.docx в режиме записи (wb) и записывает в него содержимое входного файла.

# 12. f.write(file.getvalue())
# Этот код записывает содержимое входного файла в файл {file_name}.docx.

# 13. f.close()
# Этот код закрывает файл {file_name}.docx.

# 14. pdf = f"./cache/{file_name}.pdf"
# Этот код определяет имя выходного файла как {file_name}.pdf.

# 15. docx = f"./cache/{file_name}.docx"
# Этот код определяет имя файла Word как {file_name}.docx.

# 16. convert(f"./cache/{docx}", f"./cache/{pdf}")
# Этот код вызывает функцию convert с аргументами {file_name}.docx и {file_name}.pdf.

# 17. with open(pdf, "rb") as file:
# Этот код открывает файл с именем {file_name}.pdf в режиме чтения (rb).

# 18. st.download_button(
# Этот код создает кнопку "upload", которая позволяет пользователю загрузить сконвертированный файл.

# 19. os.remove(f"./cache/{file_name}.pdf")
# Этот код удаляет файл {file_name}.pdf из временной директории.

# 20. os.remove(f"./cache/{file_name}.docx")
# Этот код удаляет файл {file_name}.docx из временной директории.

# 21. st.success("Нажмите кнопку upload, чтобы загрузить сконвертированный файл")
# Этот код отображает сообщение об успешном выполнении и предлагает пользователю нажать кнопку "upload".

# 22. else:
# Это условие проверяет, был ли выбран файл Word. Если файл не является файлом Word, то код выводит предупреждение.

# 23. st.warning(
#     f"Файл не соответсвует формату.\nОжидемый формат: pdf\nПереданный формат: {file.type.split('/')1}"
# )
# Функция warning отображает предупреждающее сообщение, указывающее на несоответствие формата файла.
