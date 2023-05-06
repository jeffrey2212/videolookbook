# Video Slideshow Creator

This Python script creates a video slideshow from a collection of images. It adds a signature and a sequence number to each image, and then combines them into a video slideshow with a specified duration per slide.

## Dependencies
Python 3.6 or later
Pillow (PIL) for image manipulation
moviepy for video creation

Install the dependencies using pip:

```bash
pip install pillow moviepy
```

## Usage
Place your images in the input folder (you can customize the folder using the -input argument).
Run the script:

```bash
python main.py
```

By default, the script will process the images in the input folder and save the signed and numbered images in the output/signed/ folder, and the final video in the output/ folder.

You can specify custom input and output folders using the -input and -output arguments:

```bash
python main.py -input /path/to/input/folder -output /path/to/output/folder
```


The slideshow video will have a default duration of 5 seconds per slide. You can customize the duration in the create_video_slideshow function call within main.py.

## Customization

You can customize the signature text, font, and size in the add_signature function call within main.py.

You can customize the sequence number font and size in the add_sequence_number function call within main.py.

## License

This project is licensed under the MIT License. See the LICENSE file for details.