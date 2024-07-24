# ImagetoPDFMerger
This Python script merges all image files (JPG, PNG, BMP, etc.) in a specific directory into a single PDF file.

## Features

- Automatically detects and processes various image formats in the script's directory.
- Merges all detected images into a single PDF file.
- Uses the `Pillow` library to handle image processing.

## Requirements

- Python 3.x
- `Pillow` library

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/GeigerLaszlo/ImagetoPDFMerger.git
    cd ImagetoPDFMerger
    ```

2. **Install the required library:**

    ```sh
    pip3 install Pillow
    ```

## Usage

1. **Place your image files in the same directory as the script:**

    Ensure all the image files you want to merge are in the same directory as `ImagetoPDFMerger.py`.

2. **Run the script:**

    Open a terminal or command prompt, navigate to the directory containing the script and your image files, and execute:

    ```sh
    python3 ImagetoPDFMerger.py
    ```

3. **Output:**

    After running the script, a PDF file named `output_file.pdf` will be created in the same directory.

## Script Details

```python
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
