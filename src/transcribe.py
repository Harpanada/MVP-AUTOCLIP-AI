import whisper
import json
from pathlib import Path

def Transribe(audio_path: Path, transicript_path: Path) ->str:
    model= whisper.load_model('tiny')
    result=model.transcribe(audio_path,word_timestamps=True)
    Path(transicript_path).write_text(json.dumps(result,indent=2))
    return result

Transribe("C:/Users/liyov/Desktop/MVP PROJECT/data/audio/extracted_audio.wav", "C:/Users/liyov/Desktop/MVP PROJECT/data/transcripts/transcript.json")