import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Apni Dhvani - Utility Suite",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.title("All in One Tool")
st.caption("All-in-one platform for file conversion, Image Conversions.")

st.divider()


st.info("Choose a tool from the sidebar on the left to begin processing your files or running AI vision tasks!")

st.space(1)


st.subheader("Available Tools")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.subheader("Image Tool")
        st.write("Modify image specifications, resize dimensions, and optimize format parameters for web use.")
        st.page_link("pages/ImageConvert.py", label="Launch Image Tools")

with col2:
    with st.container(border=True):
        st.subheader("Files Tool")
        st.write("Seamlessly convert between PDF and editable DOCX formats while preserving original styling.")
        st.page_link("pages/FileConvert.py", label="Launch File Converter")

with col3:
    with st.container(border=True):
        st.subheader("Image to PDF")
        st.write("Combine multiple image uploads directly into clean, structured PDF documents.")
        st.page_link("pages/Img2Pdf.py", label="Launch Img2Pdf")

# st.divider()

# # 5. System Stats / Project Highlights
# col_stat1, col_stat2, col_stat3 = st.columns(3)

# with col_stat1:
#     st.metric(label="Model Accuracy", value="92%", delta="+3% from last build")

# with col_stat2:
#     st.metric(label="Supported Formats", value="PDF, DOCX, JPG, PNG")

# with col_stat3:
#     st.metric(label="Processing Engine", value="Fast / Local")

# st.divider()

# # 6. Frequently Asked Questions / Info
# with st.expander("❓ How does file processing work?"):
#     st.write("""
#     * **Privacy First:** All file conversions take place directly within your local project environment.
#     * **No Data Loss:** Word documents generated via `pdf2docx` preserve paragraph flow and text structures.
#     """)

# # 7. Sidebar Customization
# st.sidebar.markdown("### 📌 **Quick Navigation**")
# st.sidebar.caption("Apni Dhvani Suite v1.0")