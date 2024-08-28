import os
import glob
import shutil
from PIL import Image
from tkinter import Tk, filedialog

IMAGE_EXTENSIONS = ("png", "jpg", "jpeg", "gif")
PDF_OUTPUT_FILENAME = "output.pdf"


def select_images(destination_folder):
    """
    Opens a file dialog for the user to select images and copies them to the specified destination folder.
    """
    # Create a hidden Tkinter root window
    root = Tk()
    root.withdraw()

    # Open file dialog to select images
    file_paths = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )

    if not file_paths:
        print("No images selected.")
        return

    # Copy selected images to the destination folder
    for file_path in file_paths:
        shutil.copy(file_path, destination_folder)
    print(f"{len(file_paths)} images copied to {destination_folder}.")

 #Deletes all files in the specified folder.
def delete_all_input_images(folder_path):  
    files = glob.glob(os.path.join(folder_path, "*"))   
    for file in files:
        os.remove(file)
    

def get_output_path(output_dir):
    output_path = os.path.join(output_dir, PDF_OUTPUT_FILENAME)
    return output_path

    # Converts all supported images in the source directory to a list of PIL Image objects ready for PDF conversion.

def image_to_pdf_converter(source_dir):
    image_list = []
    files = os.listdir(source_dir)

    for file in files:
        if file.lower().split(".")[-1] in IMAGE_EXTENSIONS:
            try:
                image_path = os.path.join(source_dir, file)
                with Image.open(image_path) as image:
                    converted_image = image.convert("RGB")
                    image_list.append(converted_image)
            except Exception as e:
                print(f"Error converting {file}: {e}")

    if not image_list:
        print("No valid images found for conversion.")
    else:
        print(f"{len(image_list)} images converted to PDF.")

    return image_list
