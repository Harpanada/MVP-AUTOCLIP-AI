import whisper
import json
from pathlib import Path

def Transribe(audio_path: Path, transicript_path: Path) ->str:
    model= whisper.load_model('small')
    result=model.transcribe(audio_path,transicript_path)
    Path(transicript_path).write_text(json.dump(result,indent=2))
    return result