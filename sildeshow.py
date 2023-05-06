from moviepy.editor import ImageClip, CompositeVideoClip, concatenate_videoclips
from moviepy.video.fx.all import resize, fadeout, fadein 

def resize_and_center_image(image_clip, target_resolution):
    aspect_ratio = float(image_clip.w) / float(image_clip.h)
    if aspect_ratio >= 1:  # Landscape or square image
        new_clip = image_clip.fx(resize, width=target_resolution[0])
    else:  # Portrait image
        new_clip = image_clip.fx(resize, height=target_resolution[1])

    # Center the image
    new_clip = new_clip.set_position(('center', 'center'))
    return new_clip

def create_video_slideshow(image_files, output_path, image_duration=3, resolution=(1920, 1080), transition_duration=1):
    
    clips = [resize_and_center_image(ImageClip(img_path).set_duration(image_duration), resolution) for img_path in image_files]

    final_clips = []
    for i in range(len(clips) - 1):
        clip1 = clips[i]
        clip2 = clips[i+1].fadein(transition_duration).set_start(clip1.duration - transition_duration)
        final_clips.append(CompositeVideoClip([clip1, clip2]))

    final_clips.append(fadeout(clips[-1], transition_duration))

    final_clip = concatenate_videoclips(final_clips, method='compose', padding=-transition_duration)
    final_clip.write_videofile(output_path, fps=24)
