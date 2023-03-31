import os
from PIL import Image

# Define input and output directories
input_dir = "input"
output_dir = "output1"

# Check if output directory already exists, and increment number if it does
if os.path.isdir(output_dir):
    count = 1
    while True:
        new_dir = output_dir + str(count)
        if os.path.isdir(new_dir):
            count += 1
        else:
            output_dir = new_dir
            break

# Create output directory
os.makedirs(output_dir)

# Loop through all png and webp files in input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".png") or filename.endswith(".webp"):

        # Open the image and get its size and aspect ratio
        img = Image.open(os.path.join(input_dir, filename))
        width, height = img.size
        img_aspect_ratio = round(float(width) / float(height), 2)

        # Calculate dimensions of 4 images based on aspect ratio
        new_width = int(width / 2)
        new_height = int(new_width / img_aspect_ratio)

        # Crop the image and save 4 new images
        for i in range(4):
            if i == 0:
                box = (0, 0, new_width, new_height)
            elif i == 1:
                box = (new_width, 0, width, new_height)
            elif i == 2:
                box = (0, new_height, new_width, height)
            elif i == 3:
                box = (new_width, new_height, width, height)
            img_crop = img.crop(box)
            new_filename = os.path.splitext(filename)[0] + str(i + 1) + os.path.splitext(filename)[1]
            img_crop.save(os.path.join(output_dir, new_filename))

print("Done chopping broccoli.")