import os
import datetime

def save_image(upload_folder, image_file):
    """Saves an uploaded image and returns its file path."""
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = os.path.join(upload_folder, f"animal_{timestamp}.jpg")
    image_file.save(file_path)
    return file_path

def categorize_animal(species):
    """Categorizes an animal based on predefined risk levels."""
    categories = {
        "Safe": ["deer", "rabbit", "squirrel"],
        "Moderate": ["fox", "wild boar"],
        "Harmful": ["wolf", "bear"],
        "Lethal": ["tiger", "lion"]
    }
    
    for category, species_list in categories.items():
        if species in species_list:
            return category
    
    return "Unknown"