from extract_audio import Extract
from transcribe import Transcribe
from segmenter import build_segment
from scorer import pick_top_segments
from build_name import build_dir
from clipper import clip_video

input_path= "E:/MVP-AUTOCLIP-AI/data/input/Bedah Bisnis Internet Rakyat 100rb, Gimmick Doang! - Raymond Chin (1080p, h264).mp4"
global_dir=build_dir(input_path)

audio_dir= global_dir/"audio"
audio_dir.mkdir(exist_ok=True)
audio_path=audio_dir/"extracted_audio.wav"
extracted_audio=Extract(input_path,audio_path)



script_dir= global_dir/"transcripts"
script_dir.mkdir(exist_ok=True)
script_path=script_dir/"transctipt.json"
script=Transcribe(str(extracted_audio),script_path)


segment=build_segment(script['segments'])
top_segment= pick_top_segments(segment)





clips_dir=global_dir/"clips"
clips_dir.mkdir(exist_ok=True)
for i,seg in enumerate(top_segment):
    print("On Clipper")
    clip_path=clips_dir/f"clip_{i}.mp4"
    clip_video(input_path,seg['start'],seg['end'],str(clip_path))
    print("done...")

