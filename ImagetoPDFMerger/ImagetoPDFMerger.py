import os
from PIL import Image

def convert_images_to_pdf(output_pdf):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Supported image extensions
    extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff']
    
    # Get all image files from the directory
    image_files = [f for f in os.listdir(script_dir) if os.path.splitext(f)[1].lower() in extensions]
    image_files.sort()  # Sort files to maintain the timeline

    if not image_files:
        print("No image files found in the directory.")
        return

    # Open images and convert them to RGB mode
    images = [Image.open(os.path.join(script_dir, img)).convert('RGB') for img in image_files]

    # Save all images as a PDF
    if images:
        images[0].save(output_pdf, save_all=True, append_images=images[1:])
        print(f"PDF created successfully: {output_pdf}")

if __name__ == "__main__":
    # Define the output PDF file
    output_pdf = 'output_file.pdf'
    
    # Convert images to PDF
    convert_images_to_pdf(output_pdf)
