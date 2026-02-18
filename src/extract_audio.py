import subprocess
from pathlib import Path


def Extract(input_path: Path) ->str:
    input_path= Path(input_path)
    output_path="C:/Users/liyov/Desktop/MVP PROJECT/data/audio/extracted_audio.wav"#Di deployment  harus diubah

    subprocess.run(["ffmpeg","-i", str(input_path),
                    "-vn", "-ac", "1" , 
                    "-ar", "16000", str(output_path)])
    

