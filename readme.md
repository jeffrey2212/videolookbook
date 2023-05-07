# Video Slideshow Creator

This Python script creates a video slideshow from a collection of images. It adds a signature and a sequence number to each image, and then combines them into a video slideshow with a specified duration per slide.

## Features

- Adds a custom signature to the bottom left corner of each image
- Adds a sequence number to the bottom right corner of each image
- Creates a video slideshow with crossfade transitions between images
- Fades in the first image from black and fades out the last image to black
- Resizes and centers images to fit the chosen resolution (HD or 4K)
- Provides command line arguments to customize input folder, output folder, image duration, and resolution
- Ensures that the output video filename is unique and does not overwrite any existing file

## Dependencies
Python 3.6 or later
Pillow (PIL) for image manipulation
moviepy for video creation

Install the dependencies using pip:

```bash
pip install -r requirements.txt
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

3. Customize the script with the following optional command line arguments:

- `-input` - Input folder containing the images (default: `./input/`)
- `-output` - Output folder where the signed images and video will be saved (default: `./output/`)
- `-duration` - Duration of each image in the video in seconds (default: `3`)
- `-resolution` - Resolution of the video, either `"HD"` (1920x1080) or `"4K"` (3840x2160) (default: `"HD"`)

Example usage with command line arguments:

```bash
    python main.py -input ./input/ -output ./output/ -duration 3 -resolution "4K"
```


## License

This project is licensed under the MIT License. See the LICENSE file for details.