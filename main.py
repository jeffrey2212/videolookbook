import os
import argparse
from PIL import Image
from add_signature import add_signature, add_sequence_number
from sildeshow import create_video_slideshow
from datetime import datetime

def get_unique_filename(output_path, output_file):
    base, ext = os.path.splitext(output_file)
    counter = 0
    while os.path.exists(os.path.join(output_path, output_file)):
        counter += 1
        output_file = f"{base}_{counter:02d}{ext}"
    return output_file

def main():
    parser = argparse.ArgumentParser(description='Add signature and create a video slideshow.')
    parser.add_argument('-input', help='Input folder containing images', default='./input/')
    parser.add_argument('-output', help='Output folder for the signed images and video', default='./output/')
    parser.add_argument('-duration', help='Duration of each image in the video slideshow (default: 3 seconds)', default=3, type=int)
    parser.add_argument('-resolution', help='Resolution of the video slideshow: "HD" or "4K" (default: "HD")', default='HD', choices=['HD', '4K'])
    args = parser.parse_args()

    resolution = (1920, 1080) if args.resolution == 'HD' else (3840, 2160)

    input_path = args.input
    output_path = args.output
    signed_path = os.path.join(output_path, 'signed/')

    os.makedirs(signed_path, exist_ok=True)
    
    image_files = [os.path.join(input_path, f) for f in os.listdir(input_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    image_files.sort()
    total_files = len(image_files)
    num_digits = len(str(total_files))

    seq = 1
    signed_and_numbered_images = []

    for file in image_files:
        img = Image.open(file)
        formatted_seq = str(seq).zfill(num_digits)
        signed_image = add_signature(img, 'Casted by AI Caster.mo', './font/NotoSerif-Italic.ttf', int(max(img.size) * 0.02))
        numbered_image = add_sequence_number(signed_image, formatted_seq, './font/NotoSerif-Bold.ttf', int(max(img.size) * 0.05))
        numbered_image.save(signed_path + formatted_seq + ".png")
        seq += 1
        signed_and_numbered_images.append(signed_path + formatted_seq + ".png")

    date_str = datetime.now().strftime("%Y%m%d")
    output_file = f"{date_str}.mp4" 
    output_file = get_unique_filename(output_path, output_file)
    video = create_video_slideshow(signed_and_numbered_images, output_path + output_file, args.duration, resolution)


if __name__ == "__main__":
    main()
