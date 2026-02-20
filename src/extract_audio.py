import subprocess
from pathlib import Path
from transcribe import Transcribe

def Extract(input_path) ->str:
    # input_path = Path(input_path)
    output_path="E:/MVP-AUTOCLIP-AI/data/audio/extracted_audio.wav"#Di deployment  harus diubah

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
    


