import hashlib
from pathlib import Path


def build_dir(input_path,):
    fille=Path(input_path).read_bytes()
    fille_hash=hashlib.sha256(fille).hexdigest()[:12]

    fille_dir= Path('fille') / fille_hash
    fille_dir.mkdir(parents=True , exist_ok= True)
    return fille_dir



