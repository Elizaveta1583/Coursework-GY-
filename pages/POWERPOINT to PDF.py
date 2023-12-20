import streamlit as st
import os
import win32com.client


def PPTtoPDF(inputFileName, outputFileName, formatType=32):
    powerpoint = win32com.client.DispatchEx("Powerpoint.Application")
    powerpoint.Visible = 1

    if outputFileName[-3:] != "pdf":
        outputFileName = outputFileName + ".pdf"
    deck = powerpoint.Presentations.Open(inputFileName)
    deck.SaveAs(outputFileName, formatType)  # formatType = 32 for ppt to pdf
    deck.Close()
    powerpoint.Quit()


file = st.file_uploader("Выберете POWERPOINT файл")

if file is not None:
    if file.name.split(".")[1] in ["pptx"]:
        process = st.button("convert")
        if process:
            with st.spinner("converting..."):
                file_name = file.name.split(".")[0]
                with open(f"./cache/{file_name}.pptx", "wb") as f:
                    f.write(file.getvalue())
                    f.close()
                PPTtoPDF(f"./cache/{file_name}.pptx", f"./cache/{file_name}.pdf")
                with open(f"./cache/{file_name}.pdf", "rb") as file:
                    st.download_button(
                        "upload",
                        file_name=f"{file_name}.pdf",
                        data=file,
                    )
                os.remove(f"./cache/{file_name}.pdf")
                os.remove(f"./cache/{file_name}.pptx")
            st.success("Нажмите кнопку upload, чтобы загрузить сконвертированный файл")
    else:
        st.warning(
            f"Файл не соответсвует формату.\nОжидемый формат: ppt\nПереданный формат: {file.name.split('.')[1]}"
        )


# 1. import streamlit as st
# Этот код импортирует библиотеку streamlit, которая позволяет создавать интерактивные веб-приложения.

# 2. import os
# Этот код импортирует библиотеку os, которая позволяет работать с операционной системой, в частности, с файлами и директориями.

# 3. import win32com.client
# Этот код импортирует библиотеку win32com.client, которая позволяет взаимодействовать с объектами COM (Component Object Model), такими как PowerPoint.

# 4. def PPTtoPDF(inputFileName, outputFileName, formatType=32):
# Это функция, которая принимает три аргумента: inputFileName (имя входного файла), outputFileName (имя выходного файла) и formatType (тип формата). По умолчанию formatType равен 32, что соответствует формату PDF.

# 5. powerpoint = win32com.client.DispatchEx("Powerpoint.Application")
# Этот код создает объект PowerPoint с помощью функции DispatchEx из библиотеки win32com.client.

# 6. powerpoint.Visible = 1
# Этот код делает приложение PowerPoint видимым, чтобы пользователь мог видеть процесс конвертации.

# 7. if outputFileName-3: != "pdf":
# Это условие проверяет, заканчивается ли имя выходного файла на "pdf". Если это не так, то имя файла будет изменено на "outputFileName + .pdf".

# 8. deck = powerpoint.Presentations.Open(inputFileName)
# Этот код открывает презентацию с указанным именем входного файла.

# 9. deck.SaveAs(outputFileName, formatType)
# Этот код сохраняет презентацию в формате, указанном в аргументе formatType. В данном случае это 32 для конвертации в PDF.

# 10. deck.Close()
# Этот код закрывает презентацию после сохранения.

# 11. powerpoint.Quit()
# Этот код закрывает приложение PowerPoint после выполнения всех операций.

# 12. file = st.file_uploader("Выберете POWERPOINT файл")
# Этот код предлагает пользователю выбрать файл PowerPoint для конвертации.

# 13. if file is not None:
# Это условие проверяет, был ли выбран файл. Если файл не был выбран, то код пропускает выполнение.

# 14. if file.name.split(".")1 in "pptx":
# Это условие проверяет, имеет ли имя файла расширение ".pptx", что означает, что файл является файлом PowerPoint.

# 15. process = st.button("convert")
# Этот код предлагает пользователю нажать кнопку "convert". Если пользователь нажимает кнопку, то код продолжает выполнение.

# 16. if process:
# Это условие проверяет, была ли нажата кнопка "convert". Если кнопка была нажата, то код продолжает выполнение.

# 17. with st.spinner("converting..."):
# Этот код отображает индикатор выполнения во время процесса конвертации.

# 18. file_name = file.name.split(".")0
# Этот код извлекает имя файла без расширения из имени входного файла.

# 19. with open(f"./cache/{file_name}.pptx", "wb") as f:
# Этот код открывает файл с именем {file_name}.pptx в режиме записи (wb) и записывает в него содержимое входного файла.

# 20. f.write(file.getvalue())
# Этот код записывает содержимое входного файла в файл {file_name}.pptx.

# 21. f.close()
# Этот код закрывает файл {file_name}.pptx.

# 22. PPTtoPDF(f"./cache/{file_name}.pptx", f"./cache/{file_name}.pdf")
# Этот код вызывает функцию PPTtoPDF с аргументами {file_name}.pptx и {file_name}.pdf.

# 23. with open(f"./cache/{file_name}.pdf", "rb") as file:
# Этот код открывает файл с именем {file_name}.pdf в режиме чтения (rb).

# 24. st.download_button(
# Этот код создает кнопку "upload", которая позволяет пользователю загрузить сконвертированный файл.

# 25. os.remove(f"./cache/{file_name}.pdf")
# Этот код удаляет файл {file_name}.pdf из временной директории.

# 25. os.remove(f"./cache/{file_name}.pptx")
# Этот код удаляет файл {file_name}.pdf из временной директории.

# 26. st.success("Нажмите кнопку upload, чтобы загрузить сконвертированный файл")
# Функция success отображает сообщение "Нажмите кнопку upload, чтобы загрузить сконвертированный файл" с использованием стилизованного элемента успеха.

# 27. else:
# Это условие проверяет, соответствует ли загруженный файл формату PDF. Если это не так, то выполняется следующий код.

# 28. st.warning(
#     f"Файл не соответсвует формату.\nОжидемый формат: pdf\nПереданный формат: {file.type.split('/')1}"
# )
# Функция warning отображает предупреждающее сообщение, указывающее на несоответствие формата файла.
