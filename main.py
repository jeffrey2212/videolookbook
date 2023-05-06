import argparse
from PIL import Image
from add_signature import add_signature, add_sequence_number
from sildeshow import create_video_slideshow
from datetime import datetime
import os 

def main():
    parser = argparse.ArgumentParser(description="Create a video slideshow from images.")
    parser.add_argument("-input", default="./input/", help="Input folder containing the images.")
    parser.add_argument("-output", default="./output/", help="Output folder for the signed images and video.")
    args = parser.parse_args()

    input_path = args.input
    output_path = args.output
    signed_path = os.path.join(output_path, 'signed/')

    if not os.path.exists(signed_path):
        os.mkdir(signed_path)

    image_files = [os.path.join(input_path, f) for f in os.listdir(input_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    image_files.sort()
    total_files = len(image_files)
    num_digits = len(str(total_files))

    seq = 1
    signed_and_numbered_image = []
    
    for file in image_files:
        img = Image.open(file)
        formatted_seq = str(seq).zfill(num_digits)
        signed_image = add_signature(img, 'Casted by AI Caster.mo', './font/NotoSerif-Italic.ttf', int(max(img.size) * 0.02))
        numbered_image = add_sequence_number(signed_image, formatted_seq, './font/NotoSerif-Bold.ttf', int(max(img.size) * 0.05))
        numbered_image.save(os.path.join(signed_path, f"{formatted_seq}.png"))
        seq += 1
        signed_and_numbered_image.append(os.path.join(signed_path, f"{formatted_seq}.png"))

    date_str = datetime.now().strftime("%Y%m%d")
    output_file = f"{date_str}.mp4"
    video = create_video_slideshow(signed_and_numbered_image, os.path.join(output_path, output_file), 5)

if __name__ == "__main__":
    main()
