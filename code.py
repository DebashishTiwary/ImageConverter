from PIL import Image, ImageOps  # 1. Added ImageOps import

# Open the image
img = Image.open("icrb_profile.jpg")

# Convert to RGB (required for JPG format)
img = img.convert("RGB")

# Calculate exact pixel size for 3.5cm x 4.5cm at 200 DPI
target_size = (276, 354)

# Resize image
resized_img = img.resize(target_size, Image.Resampling.LANCZOS)

# 2. ADD PADDING LINE HERE (adds a 20-pixel white border around the resized image)
padded_img = ImageOps.expand(resized_img, border=0, fill="white")

# 3. Save the padded image instead of resized_img
padded_img.save("formatted_photo.jpg", "JPEG", dpi=(200, 200), quality=100)