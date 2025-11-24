# Image_resizer
This program takes all the images from a folder, resizes them, and saves them into another folder automatically. First, the code imports two things: os which helps in working with folders and files, and Image from Pillow which helps in opening and editing images.
The code sets two folder names: one folder where your original images are kept, and another folder where the resized images will be saved. It also sets the new size you want for the images, like 400 by 500.
Then it checks if the output folder exists. If not, it creates that folder. After this, the program looks inside the input folder and goes through each file one by one. For every file, it checks if the file is an image (like .jpg, .png, .jpeg, or .webp).
If it is an image, the code opens it using Pillow, resizes it to the size you gave, and then saves the new resized version into the output folder with the same name as the original.
While doing this, it prints the name of each image that gets resized. When all images are done, it prints a message saying that all images have been resized successfully.
