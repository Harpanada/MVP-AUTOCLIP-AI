from extract_audio import Extract
from transcribe import Transcribe
from segmenter import build_segment
from scorer import pick_top_segments


input_path= "E:\MVP-AUTOCLIP-AI\data\input\Borong Bitcoin Episode 33 - Februari 2026 - Timothy Ronald (1080p, h264).mp4"

extracted_audio=Extract(input_path)

script=Transcribe(extracted_audio,"E:/MVP-AUTOCLIP-AI/data/transcripts/transcript.json")

segment=build_segment(script['segments'])

top_segment= pick_top_segments(segment)



