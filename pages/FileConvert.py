import cv2
import numpy as np
import streamlit as st
from docx import Document
# import pypdf
from pdf2docx import Converter
import os
# from docx2pdf import 

st.set_page_config(page_title="Convert your files to different extensions", layout="wide")
st.title("File Convertor")

uploaded_file=st.file_uploader("Choose your file",type=["pdf","docx"])
if uploaded_file is not None:
    if uploaded_file.name.endswith(".pdf"):
        temp_pdf="temp.pdf"
        temp_doc="output.docx"

        with open (temp_pdf,"wb") as file:
            file.write(uploaded_file.getbuffer())
        if st.button("Convert to Docx"):
            with st.spinner("Converting.."):
                cv = Converter(temp_pdf)
                cv.convert(temp_doc,start=0,end=None)
                cv.close()
                st.success("Conversion successful!")
            if os.path.exists (temp_doc):
                with open(temp_doc, "rb") as f:
                    st.download_button(
                        label="Download Converted Word File",
                        data=f,
                        file_name="converted_document.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
    elif uploaded_file.name.endswith(".doc") or uploaded_file.name.endswith(".docx"):
        