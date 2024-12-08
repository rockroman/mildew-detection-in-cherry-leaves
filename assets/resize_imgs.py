import os
from PIL import Image

def resize_images(input_dir, output_dir, size=(60, 60)):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Iterate through all files in the input directory
    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)
        
        # Check if it's a file and has an image extension
        if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            try:
                # Open an image file
                with Image.open(file_path) as img:
                    # Resize image
                    img = img.resize(size)
                    # Save it to the output directory
                    img.save(os.path.join(output_dir, filename))
                    print(f"Resized and saved: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Define directories for validation sets
validation_dir_healthy = 'inputs/cherry-leaves_dataset/cherry-leaves/validation/healthy/'
validation_dir_fungal_infected = 'inputs/cherry-leaves_dataset/cherry-leaves/validation/fungal-infected/'

# Create output directories for resized images (optional)
output_dir_healthy = 'inputs/cherry-leaves_dataset/cherry-leaves/validation/healthy_resized/'
output_dir_fungal_infected = 'inputs/cherry-leaves_dataset/cherry-leaves/validation/fungal-infected_resized/'

# Resize images in both directories
resize_images(validation_dir_healthy, output_dir_healthy)
resize_images(validation_dir_fungal_infected, output_dir_fungal_infected)