import streamlit as st
import os

file = st.file_uploader("Выберете PDF файл")

if file is not None:
    if file.type.split("/")[1] in ["pdf"]:
        process = st.button("convert")
        if process:
            with st.spinner("converting..."):
                file_name = file.name.split(".")[0]
                print(file_name)
                with open(f"./cache/{hash(file_name)}.pdf", "wb") as f:
                    f.write(file.getvalue())
                    f.close()
                os.system(f"pdf2pptx ./cache/{hash(file_name)}.pdf")
                with open(f"./cache/{hash(file_name)}.pptx", "rb") as file:
                    st.download_button(
                        "upload",
                        file_name=f"{file_name}.pptx",
                        data=file,
                    )
                os.remove(f"./cache/{hash(file_name)}.pdf")
                os.remove(f"./cache/{hash(file_name)}.pptx")
            st.success("Нажмите кнопку upload, чтобы загрузить сконвертированный файл")
    else:
        st.warning(
            f"Файл не соответсвует формату.\nОжидемый формат: pdf\nПереданный формат: {file.type.split('/')[1]}"
        )

# 1. import streamlit as st - Импортирует библиотеку Streamlit, позволяющую создавать интерактивные веб-приложения.
# 2. import os - Импортирует модуль os, который предоставляет функции для работы с операционной системой.
# 3. file = st.file\_uploader("Выберете PDF файл") - Определяет элемент загрузки файла, который позволяет пользователю выбрать файл PDF для преобразования.
# 4. if file is not None: - Проверяет, был ли выбран файл. Если файл не был выбран, код в блоке if не будет выполнен.
# 5. if file.type.split("/")[1] in ["pdf"]: - Проверяет, является ли тип файла PDF. Если это не PDF, код в блоке if не будет выполнен.
# 6. process = st.button("convert") - Определяет кнопку "convert", которую пользователь может нажать для начала процесса преобразования.
# 7. if process: - Проверяет, была ли нажата кнопка "convert". Если это так, код в блоке if будет выполнен.
# 8. with st.spinner("converting..."): - Использует атрибут spinner для отображения индикатора выполнения во время преобразования файла.
# 9. file\_name = file.name.split(".")[0] - Получает имя файла и удаляет расширение.
# 10. print(file\_name) - Выводит имя файла в консоль.
# 11. with open(f"./cache/{hash(file\_name)}.pdf", "wb") as f: - Открывает файл для записи в режиме binary и записывает содержимое файла PDF.
# 12. f.write(file.getvalue()) - Записывает содержимое файла PDF в файл в памяти.
# 13. f.close() - Закрывает файл.
# 14. os.system(f"pdf2pptx ./cache/{hash(file\_name)}.pdf") - Запускает утилиту pdf2pptx для преобразования файла PDF в файл PPTX.
# 15. with open(f"./cache/{hash(file\_name)}.pptx", "rb") as file: - Открывает файл PPTX для чтения в режиме binary.
# 16. st.download\_button(
#         "upload",
#         file\_name=f"{file\_name}.pptx",
#         data=file,
#     ) - Создает кнопку загрузки, которая позволяет пользователю скачать файл PPTX.
# 17. os.remove(f"./cache/{hash(file\_name)}.pdf") - Удаляет файл PDF из временного хранилища.
# 18. os.remove(f"./cache/{hash(file\_name)}.pptx") - Удаляет файл PPTX из временного хранилища.
# 19. st.success("Нажмите кнопку upload, чтобы загрузить сконвертированный файл") - Отображает сообщение об успешном преобразовании файла.
# 20. else: - Если файл не является PDF, выводится сообщение об ошибке.
# 21. st.warning(
#         f"Файл не соответсвует формату.\nОжидемый формат: pdf\nПереданный формат: {file.type.split('/')[1]}"
#     ) - Отображается предупреждающее сообщение о том, что файл не соответствует ожидаемому формату.
