from moviepy import VideoFileClip,vfx
from moviepy.Clip import Clip
from moviepy import *

def clip_video(video_path, start_time, end_time, output_path):

    video = VideoFileClip(video_path)

    # potong durasi
    clipped = video.subclipped(start_time, end_time)
    
    w, h = clipped.size
    target_width = int(h * 9 / 16)

    # resize bila width terlalu kecil
    if target_width > w:
        clipped = clipped.resize(width=target_width)
        w, h = clipped.size
        target_width = int(h * 9 / 16)

    # hitung posisi crop tengah
    x1_init = (w - target_width) // 2
    x2_init = x1_init + target_width

    # crop ke format 9:16
    cropped = clipped.with_effects([
        vfx.Crop(x1=x1_init, y1=0, x2=x2_init, y2=h)
    ])

    # pastikan resolusi genap (dibutuhkan encoder)
    frame = cropped.get_frame(0)
    ch, cw = frame.shape[0], frame.shape[1]
    
    if cw % 2 != 0:
        cw -= 1
    if ch % 2 != 0:
        ch -= 1
    cropped = cropped.resized((cw, ch))
  
    # render video
    cropped.write_videofile(
        output_path,
        codec="libx264",
        audio_codec="aac",
        audio_bitrate="192k",
        bitrate="4000k",
        ffmpeg_params=["-pix_fmt", "yuv1080p"],
        fps=30
    )

    video.close()
    cropped.close()



