from PIL import Image, ImageDraw, ImageFont

def add_signature(image, signature, font_path, font_size, text_color=(255, 255, 255), background_color=(0, 0, 0, 128), padding=10):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, size=font_size)

    text_size = font.getsize(signature)
    vertical_offset = font.getoffset(signature)[1]
    text_position = (image.width - text_size[0] - font_size // 2 - padding, image.height - text_size[1] - vertical_offset - padding)

    background_rect = Image.new('RGBA', (text_size[0] + 2 * padding, text_size[1] + 2 * padding), background_color)
    image.paste(background_rect, (text_position[0] - padding, text_position[1] - padding), background_rect)

    draw.text(text_position, signature, font=font, fill=text_color)
    return image

def add_sequence_number(image, number, font_path, font_size, text_color=(255, 255, 255), background_color=(0, 0, 0, 128), padding=10, vertical_adjustment=10):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, size=font_size)

    text_size = font.getsize(str(number))
    text_position = (font_size // 2 + padding, image.height - text_size[1] -  padding - vertical_adjustment *2 )

    background_rect = Image.new('RGBA', (text_size[0] + 2 * padding, text_size[1] + 2 * padding), background_color)
    image.paste(background_rect, (text_position[0] - padding, text_position[1] - padding + vertical_adjustment), background_rect)

    draw.text(text_position, str(number), font=font, fill=text_color)
    return image
