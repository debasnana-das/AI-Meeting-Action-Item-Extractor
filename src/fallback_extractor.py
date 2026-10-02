import re

try:
    from .validator import normalize_status
except ImportError:
    from validator import normalize_status

MONTHS = r'January|February|March|April|May|June|July|August|September|October|November|December'
DATE_RE = re.compile(rf'\b(?:{MONTHS})\s+\d{{1,2}},\s+\d{{4}}\b|\b\d{{4}}-\d{{2}}-\d{{2}}\b', re.I)
SPEAKER_RE = re.compile(r'^(?P<speaker>[A-Za-z][A-Za-z ._-]{1,30}):\s*(?P<text>.*)$')
ACTION_RE = re.compile(r'\b(?:i will|i can|i’ll|i need to|(?:will|can)\s+\w+)', re.I)

def extract(transcript):
    items = []
    for line in transcript.splitlines():
        m = SPEAKER_RE.match(line.strip())
        if not m:
            continue
        speaker, text = m.group('speaker').strip(), m.group('text').strip()
        if not ACTION_RE.search(text):
            continue
        task = re.sub(r'^(?:I will|I can|I’ll|I need to)\s+', '', text, flags=re.I).strip()
        d = DATE_RE.search(task)
        deadline = d.group(0) if d else 'unknown'
        if d:
            task = re.sub(r'\bby\s*$', '', task[:d.start()].strip(), flags=re.I).strip(' .')
        items.append({
            'task': task,
            'owner': speaker,
            'deadline': deadline,
            'status': normalize_status(text),
            'confidence': 0.82
        })

    seen = set()
    unique = []
    for x in items:
        key = (
            re.sub(r'\W+', ' ', x['task'].lower()).strip(),
            x['owner'].lower(),
            x['deadline'].lower()
        )
        if key not in seen:
            seen.add(key)
            unique.append(x)
    return unique
