# mjChoppa

mjChoppa is a Python program that scans a directory for PNG and WEBP images, determines their aspect ratio, and then crops them into four images in the configuration of two on top and two on bottom. The output images are saved in a new directory with the same name as the original image but with "1", "2", "3", or "4" appended as a suffix. If the output directory name already exists, the program increments the number by 1 until it finds an available directory name.

## Installation

1. Clone the repository: `git clone https://github.com/annias/mjChoppa.git`
2. Install the required dependencies: `pip install -r requirements.txt`

## Usage

1. Navigate to the mjChoppa directory.
2. Place the PNG and WEBP images you want to crop in the "input" directory.
3. Run the program: `python mjChoppa.py`
4. The cropped images will be saved in a new directory named "outputX" where X is the lowest number that makes the directory name unique.

## Dependencies

- Python 3.x
- Pillow (PIL) 8.x.x

## Annias art and socials

You can find more of my art and social links on my linktree: https://linktr.ee/annias

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Acknowledgements
## Pillow (PIL) Library
## Python

## Changelog
## Made first iteration of the program, works
## Modified to modify png and webp files
## Added support for multiple input files
## Added support for multiple output directories
## Added support for multiple aspect ratios

### 1.0.2