import os
from PIL import Image

input_folder = "input_images"
output_folder = "output_images"
new_size = (400, 500)  

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for file_name in os.listdir(input_folder):
    if file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
        img_path = os.path.join(input_folder, file_name)
        img = Image.open(img_path)

        resized_img = img.resize(new_size)

        save_path = os.path.join(output_folder, file_name)
        resized_img.save(save_path)

        print("Resized:", file_name)

print(" All images resized successfully!")
