# image_processing_package_Theodoro_Fraga_DIO

This is a simple Python package for educational purposes, focused on basic image processing functionalities. It was developed as part of a challenge from the Digital Innovation One (DIO) platform.

## Installation

You can install this package directly via pip:

```bash
pip install image_processing_package_Theodoro_Fraga_DIO
Note: Make sure you have Python and pip installed.

Usage
To use the functionalities of this package, import it in your Python script:

Python

# Basic usage example (assuming you have a test image file)
from image_processing_package_theodoro_fraga_dio import process_image_basic
from image_processing_package_theodoro_fraga_dio import greet
import os

# Example of the greet function
message = greet("DIO User")
print(message)

# Example of the image processing function (requires a test image)
test_image_path = "path/to/your/image.jpg" # Replace with the actual path to your test image
output_image_path = "processed_image.jpg"

if os.path.exists(test_image_path):
    process_image_basic(test_image_path, output_image_path)
else:
    print(f"Test file '{test_image_path}' not found.")

*Note: The image processing functions in `file2_name.py` require the Pillow library to be installed, which will be done automatically when you install the package.*

#Features
*Currently, this package includes the following basic functionalities:

greet(name): A simple greeting function (located in file1_name.py).
process_image_basic(image_path, output_path): Opens an image, converts it to grayscale, and saves it (located in file2_name.py).
** Author
- Theodoro Fraga
- Email: theodorofragadecastro.dev@gmail.com
- GitHub: https://github.com/tedtheotheodoro

*License
- This project is licensed under the MIT License - see the https://www.google.com/search?q=LICENSE file for more details.

