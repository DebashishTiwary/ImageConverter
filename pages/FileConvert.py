import cv2
import numpy as np
import streamlit as st
from docx import Document
from pdf2docx import Converter
import os
import tempfile
from docx2pdf import convert
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

st.set_page_config(page_title="Convert your files to different extensions", layout="wide")
st.title("File Convertor")
st.write("Upload a file (pdf) and convert to docx or Vice-Versa")
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
        temp_pdf_path = "output_document.pdf"

        if st.button("Convert to PDF"):
            with st.spinner("Generating PDF layout..."):
            # Load the Word document using python-docx
                doc = Document(uploaded_file)
            
            # Setup ReportLab document structure
                pdf = SimpleDocTemplate(temp_pdf_path, pagesize=letter)
                styles = getSampleStyleSheet()
                story = []
            
            # Extract paragraphs and add them to the ReportLab story
                for para in doc.paragraphs:
                    if para.text.strip():
                        p = Paragraph(para.text, styles['Normal'])
                        story.append(p)
                        story.append(Spacer(1, 10)) # Add spacing between paragraphs
            
            # Build the PDF file
                pdf.build(story)
                st.success("Conversion successful!")

    # Display download button persistently if the PDF exists
            if os.path.exists(temp_pdf_path):
                with open(temp_pdf_path, "rb") as f:
                    st.download_button(
                        label="Download Converted PDF File",
                        data=f,
                        file_name="converted_document.pdf",
                        mime="application/pdf"
            )