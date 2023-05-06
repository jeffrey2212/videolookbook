from moviepy.editor import CompositeVideoClip, ImageClip, concatenate_videoclips
from moviepy.video.fx.all import resize

def crossfade_transition(clip1, clip2, transition_duration=1):
    clip1_end = clip1.duration - transition_duration
    clip2_start = clip2.set_start(clip1_end)
    return CompositeVideoClip([clip1, clip2_start])

def create_video_slideshow(image_files, output_path, image_duration=3, resolution=(1920, 1080), transition_duration=2):
    
    def resize_and_center_image(image_clip, target_resolution):
        aspect_ratio = float(image_clip.w) / float(image_clip.h)
        if aspect_ratio >= 1:  # Landscape or square image
            new_clip = image_clip.fx(resize, width=target_resolution[0])
        else:  # Portrait image
            new_clip = image_clip.fx(resize, height=target_resolution[1])
        
        # Center the image
        new_clip = new_clip.set_position(('center', 'center'))
        return new_clip
    
    clips = [resize_and_center_image(ImageClip(img_path).set_duration(image_duration), resolution) for img_path in image_files]
    final_clips = []

    for i in range(len(clips) - 1):
        clip1 = clips[i]
        clip2 = clips[i+1]

        # Apply crossfade transition between two clips
        transition = crossfade_transition(clip1, clip2, transition_duration)
        final_clips.append(transition)

    final_clips.append(clips[-1])  # Append the last clip without a transition
    final_clip = concatenate_videoclips(final_clips, method='compose', padding=-transition_duration)
    final_clip.write_videofile(output_path, fps=24)

