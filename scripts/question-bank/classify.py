"""Read-only source inventory; write a local manifest, never move source files."""
import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


def classify(path, root):
    rel = str(path.relative_to(root))
    match = re.search(r'剑桥雅思真题(\d+)', rel)
    if not match:
        match = re.search(r'【(\d+)】|剑(\d+)', path.name)
    volume = next((int(g) for g in match.groups() if g), None) if match else None
    if root.name.startswith('剑21'):
        volume = 21
    elif root.name.startswith('剑20'):
        volume = 20
    compilation = '456合辑' in path.name
    if compilation:
        volume = None
    suffix = path.suffix.lower()
    kind = ('explanation' if '解析' in rel or '精讲' in rel else
            'book' if suffix == '.pdf' else
            'audio' if suffix in ['.mp3', '.m4a', '.aiff'] else 'image')
    exam_type = 'G' if 'G类' in path.name else 'A' if 'A类' in path.name else 'unverified'
    test = re.search(r'(?:test|T)\s*(\d+)', rel, re.I)
    part = re.search(r'(?:part|section|_S|T\d+S)\s*(\d+)', rel, re.I)
    return dict(id=hashlib.sha256(str(path).encode()).hexdigest()[:16],
                source=str(path), root=root.name, relativePath=rel,
                volume=volume, compilation=compilation, examType=exam_type,
                kind=kind, format=suffix[1:], bytes=path.stat().st_size,
                test=int(test.group(1)) if test else None,
                part=int(part.group(1)) if part else None,
                status='indexed-not-imported')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('roots', nargs='+', type=Path)
    args = parser.parse_args()
    files = [classify(p, root) for root in args.roots for p in sorted(root.rglob('*'))
             if p.is_file() and not p.name.startswith('.')]
    volumes = []
    for number in range(4, 22):
        group = [f for f in files if f['volume'] == number]
        volumes.append(dict(volume=number, counts=dict(Counter(f['kind'] for f in group)),
                            bytes=sum(f['bytes'] for f in group),
                            examTypes=sorted(set(f['examType'] for f in group)),
                            state='待逐册核对' if group else '未找到独立原书或音频'))
    result = dict(schemaVersion=1, files=files, volumes=volumes,
                  totalBytes=sum(f['bytes'] for f in files),
                  notes=['文件名分类不代表内容完整；未标 A/G 的资料待目录核对。',
                         '剑4仅见456解析合辑，未见独立原书与音频。',
                         '剑20仅见Test 1–3 PDF及Test 1音频。',
                         '剑21两份A类PDF为同页数候选版本，待逐页去重；预览选可提取正文的一份。'])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(f'Indexed {len(files)} files; source files unchanged.')


if __name__ == '__main__':
    main()
