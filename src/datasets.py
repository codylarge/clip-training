import os
import random
from PIL import Image

def load_random_images(dataset_dir, split='train', num_images=8):
    # Define the path to the split directory (train, test, or val)
    split_dir = os.path.join(dataset_dir, split)

    # Check if the split directory exists
    if not os.path.isdir(split_dir):
        raise ValueError(f"The specified split directory '{split}' does not exist.")

    # Get all class directories from the split (train/test/val)
    class_dirs = [d for d in os.listdir(split_dir) if os.path.isdir(os.path.join(split_dir, d))]
    
    # Randomly select num_images directories (in this case, 8)
    random_class_dirs = random.sample(class_dirs, num_images)

    images_and_classes = []

    # For each selected class directory, pick one random image
    for class_name in random_class_dirs:
        class_dir = os.path.join(split_dir, class_name)
        image_files = [f for f in os.listdir(class_dir) if f.endswith((".png", ".jpg", ".jpeg"))]
        
        if not image_files:
            continue

        # Select a random image from the class directory
        random_image_file = random.choice(image_files)
        image_path = os.path.join(class_dir, random_image_file)

        # Load image and store with its class name
        image = Image.open(image_path).convert("RGB")
        images_and_classes.append((image, class_name))

    return images_and_classes
