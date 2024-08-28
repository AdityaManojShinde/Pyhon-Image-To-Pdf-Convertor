from converter import get_output_path, image_to_pdf_converter, delete_all_input_images, select_images

SOURCE_DIR = "./images"
OUTPUT_DIR = "./output"

def convert_images_to_pdf():
    # Select and copy images to the source directory
    select_images(SOURCE_DIR)
    
    # Convert images to PDF
    images = image_to_pdf_converter(source_dir=SOURCE_DIR)
    if not images:
        print("No images found in the source directory.")
        return

    # Generate output path for the PDF
    output_path = get_output_path(output_dir=OUTPUT_DIR)

    # Separate the first image from the rest
    first_image, other_images = images[0], images[1:]

    # Save the first image and append the rest
    first_image.save(output_path, save_all=True, append_images=other_images)
    print(f"PDF saved successfully at: {output_path}")

def cleanup_images():
    # Delete all images in the source directory
    delete_all_input_images(SOURCE_DIR)
    print(f"All images deleted from {SOURCE_DIR}")

def main():
    convert_images_to_pdf()
    cleanup_images()

if __name__ == "__main__":
    main()
