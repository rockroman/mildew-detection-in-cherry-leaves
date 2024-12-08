import os

def get_directory_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            # Check if it's a file and add its size
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)
    return total_size

# Define your directories
fungal_infected_dir = 'inputs/cherry-leaves_dataset/cherry-leaves/validation/fungal-infected'
healthy_dir = 'inputs/cherry-leaves_dataset/cherry-leaves/validation/healthy'

# Get sizes
fungal_infected_size = get_directory_size(fungal_infected_dir)
healthy_size = get_directory_size(healthy_dir)

# Print results
print(f"Total size of fungal-infected directory: {fungal_infected_size / (1024 * 1024):.2f} MB")
print(f"Total size of healthy directory: {healthy_size / (1024 * 1024):.2f} MB")