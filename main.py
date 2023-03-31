import os
from PIL import Image

# Get current directory
current_dir = os.getcwd()

# Define output folder name
output_folder = "output1"
output_folder_exists = True
folder_count = 0

# Check if output folder exists, increment count if it does
while output_folder_exists:
    folder_count += 1
    output_folder_check = output_folder + str(folder_count)
    if os.path.isdir(os.path.join(current_dir, output_folder_check)):
        continue
    else:
        output_folder = output_folder_check
        output_folder_exists = False

# Create output folder
os.makedirs(output_folder)

# Scan directory for png files
png_files = [f for f in os.listdir(current_dir) if f.endswith('.png')]

# Define image dimensions
img_width = 900
img_height = 600

# Loop through png files and create cropped images
for file in png_files:
    # Open image and get dimensions
    img_path = os.path.join(current_dir, file)
    with Image.open(img_path) as im:
        width, height = im.size

        # Calculate dimensions for 4 cropped images
        crop_width = int(width / 2)
        crop_height = int(height / 2)

        # Crop images and save them
        for i, coords in enumerate([(0, 0), (crop_width, 0), (0, crop_height), (crop_width, crop_height)]):
            x, y = coords
            cropped_img = im.crop((x, y, x + crop_width, y + crop_height))
            cropped_img.save(os.path.join(output_folder, f"{os.path.splitext(file)[0]}_{i + 1}.png"))

# Done chopping broccoli
print("Done chopping broccoli.")