import subprocess
from pathlib import Path


def Extract(input_path,output_path) ->str:
    # input_path = Path(input_path)
    

    subprocess.run([   
        "ffmpeg",
        "-i", input_path,
        "-vn",           # No video
        "-acodec", "pcm_s16le",  # WAV format
        "-ar", "16000",  # Sample rate 16kHz (required by Whisper)
        "-ac", "1",     # Mono
        output_path,
        "-y"])
    return output_path
    


