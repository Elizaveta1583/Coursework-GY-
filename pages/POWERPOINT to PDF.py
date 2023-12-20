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


