import streamlit as st
import os
from pdf2docx import Converter

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
                docx = f"./cache/{file_name}.docx"
                cv = Converter(pdf)
                cv.convert(docx)
                cv.close()
                with open(docx, "rb") as file:
                    st.download_button(
                        "upload",
                        file_name=f"{file_name}.docx",
                        data=file,
                    )
                os.remove(docx)
                os.remove(pdf)
            st.success("Нажмите кнопку upload, чтобы загрузить сконвертированный файл")
    else:
        st.warning(
            f"Файл не соответсвует формату.\nОжидемый формат: pdf\nПереданный формат: {file.type.split('/')[1]}"
        )


# 1. import streamlit as st - Импортирует библиотеку Streamlit, которая позволяет создавать интерактивные веб-приложения.
# 2. import os - Импортирует модуль os, который предоставляет функции для работы с операционной системой.
# 3. from pdf2docx import Converter - Импортирует модуль pdf2docx, который позволяет преобразовывать файлы PDF в файлы DOCX.
# 4. file = st.file\_uploader("Выберете PDF файл") - Определяет элемент загрузки файла, который позволяет пользователю выбрать файл PDF для преобразования.
# 5. if file is not None: - Проверяет, был ли выбран файл. Если файл не был выбран, код в блоке if не будет выполнен.
# 6. if file.type.split("/")[1] in ["pdf"]: - Проверяет, является ли тип файла PDF. Если это не PDF, код в блоке if не будет выполнен.
# 7. process = st.button("convert") - Определяет кнопку "convert", которую пользователь может нажать для начала процесса преобразования.
# 8. if process: - Проверяет, была ли нажата кнопка "convert". Если это так, код в блоке if будет выполнен.
# 9. with st.spinner("converting..."): - Использует атрибут spinner для отображения индикатора выполнения во время преобразования файла.
# 10. file\_name = file.name.split(".")[0] - Получает имя файла и удаляет расширение.
# 11. with open(f"./cache/{file\_name}.pdf", "wb") as f: - Открывает файл для записи в режиме binary и записывает содержимое файла PDF.
# 12. f.write(file.getvalue()) - Записывает содержимое файла PDF в файл в памяти.
# 13. f.close() - Закрывает файл.
# 14. pdf = f"./cache/{file\_name}.pdf" - Определяет переменную pdf, которая содержит путь к файлу PDF.
# 15. docx = f"./cache/{file\_name}.docx" - Определяет переменную docx, которая содержит путь к файлу DOCX после преобразования.
# 16. cv = Converter(pdf) - Создает экземпляр объекта Converter и передает в него путь к файлу PDF.
# 17. cv.convert(docx) - Преобразует файл PDF в файл DOCX.
# 18. cv.close() - Закрывает объект Converter.
# 19. with open(docx, "rb") as file: - Открывает файл DOCX для чтения в режиме binary.
# 20. st.download\_button(
#         "upload",
#         file\_name=f"{file\_name}.docx",
#         data=file,
#     ) - Создает кнопку загрузки, которая позволяет пользователю скачать файл DOCX.
# 21. os.remove(docx) - Удаляет файл DOCX из временного хранилища.
# 22. os.remove(pdf) - Удаляет файл PDF из временного хранилища.
# 23. st.success("Нажмите кнопку upload, чтобы загрузить сконвертированный файл") - Отображает сообщение об успешном преобразовании файла.
# 24. else: - Если файл не является PDF, выводится сообщение об ошибке.
# 25. st.warning(
#         f"Файл не соответсвует формату.\nОжидемый формат: pdf\nПереданный формат: {file.type.split('/')[1]}"
#     ) - Отображается предупреждающее сообщение о том, что файл не соответствует ожидаемому формату.
