"""Rebuild the local preview from user-owned source materials, without uploading them."""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--pdf', required=True, type=Path)
p.add_argument('--audio-dir', required=True, type=Path)
p.add_argument('--source-root', required=True, action='append', type=Path)
p.add_argument('--output', type=Path, default=ROOT / 'work/question-preview')
a = p.parse_args()
if not a.pdf.is_file():
    p.error('PDF does not exist')
for folder in [a.audio_dir, *a.source_root]:
    if not folder.is_dir():
        p.error(f'Directory does not exist: {folder}')
audio = [a.audio_dir / f'Test1-Part{i}.mp3' for i in range(1, 5)]
if not all(f.is_file() for f in audio):
    p.error('Expected Test1-Part1.mp3 through Test1-Part4.mp3 in the audio directory')
renderer = shutil.which('pdftoppm')
if not renderer:
    p.error('Install Poppler and make pdftoppm available on PATH')
out = a.output.resolve()
assets = out / 'assets'
assets.mkdir(parents=True, exist_ok=True)
subprocess.run([renderer, '-f', '30', '-l', '30', '-scale-to', '1500', '-jpeg',
                '-jpegopt', 'quality=82', str(a.pdf.resolve()), str(assets/'page')], check=True)
subprocess.run([sys.executable, str(HERE/'classify.py'), '--output', str(out/'inventory.json'),
                *[str(f.resolve()) for f in a.source_root]], check=True)
subprocess.run([sys.executable, str(HERE/'prepare_computer_test.py'), '--pdf', str(a.pdf.resolve()),
                '--output', str(out)], check=True)
for i, source in enumerate(audio, 1):
    shutil.copyfile(source, assets/f'part-{i}.mp3')
shutil.copyfile(HERE/'computer-preview.html', out/'index.html')
print(f'Preview ready: {out}')
print(f'Run: python3 -m http.server 5184 --bind 127.0.0.1 --directory "{out}"')
