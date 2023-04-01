# mjChoppa

mjChoppa is a Python program that scans a directory for PNG and WEBP images, determines their aspect ratio, and then crops them into four images in the configuration of two on top and two on bottom. The output images are saved in a new directory named "chopped" within the directory selected by the user. If the "chopped" directory already exists, the program increments the number by 1 until it finds an available directory name.

## Installation

1. Clone the repository: `git clone https://github.com/annias/mjChoppa.git`
2. Install the required dependencies: `pip install -r requirements.txt`

## Usage

1. Navigate to the mjChoppa directory.
2. Run the program: `python mjChoppa.py`
3. A dialog box will appear for you to select the directory containing the PNG and WebM images you want to crop.
4. The cropped images will be saved in a new directory named "chopped" within the selected directory.

## Dependencies

- Python 3.x
- Pillow (PIL) 8.x.x

## Annias art and socials

You can find more of my art and social links on my linktree: https://linktr.ee/annias

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Acknowledgements
Pillow (PIL) Library
Python

## Changelog
- Made first iteration of the program, works
- Modified to modify png and webp files
- Added support for multiple input files
- Added support for multiple output directories
- Added support for multiple aspect ratios
- Added support for selecting input directory with Windows dialog box
- Added support for saving output in new "chopped" folder within selected directory

## Current Version

1.0.3
