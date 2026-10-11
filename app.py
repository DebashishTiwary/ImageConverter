import cv2
import numpy as np
import streamlit as st

st.title("🖼️ Image Transformer Web App")
st.write("Upload an image, set your desired dimensions and format, and transform it instantly!")

# 1. File Uploader widget for the website
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the uploaded image file with OpenCV
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Show the original image on the website
    st.subheader("Original Image")
    st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), channels="RGB")

    # 2. Input widgets for user choices
    st.subheader("Transformation Settings")
    
    # Default width and height based on the uploaded image
    orig_height, orig_width = image.shape[:2]
    
    width = st.number_input("Desired Width (px)", min_value=1, value=orig_width)
    height = st.number_input("Desired Height (px)", min_value=1, value=orig_height)
    
    img_format = st.selectbox("Desired Format", ["jpg", "png", "jpeg"])
    new_name = st.text_input("Desired File Name", value="transformed_image")

    # 3. Process button
    if st.button("Transform Image"):
        # Resize image using your logic
        user_image = cv2.resize(image, (int(width), int(height)))
        
        # Encode image to save/download in memory
        success, encoded_image = cv2.imencode(f".{img_format}", user_image)
        
        if success:
            filename = f"{new_name}.{img_format}"
            
            st.success("Image transformed successfully!")
            
            # Show the transformed image preview
            st.subheader("Transformed Result")
            st.image(cv2.cvtColor(user_image, cv2.COLOR_BGR2RGB), channels="RGB")
            
            # 4. Download button for the user
            st.download_button(
                label="📥 Download Transformed Image",
                data=encoded_image.tobytes(),
                file_name=filename,
                mime=f"image/{img_format}"
            )