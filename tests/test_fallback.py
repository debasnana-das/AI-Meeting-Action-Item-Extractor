import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))
from fallback_extractor import extract

def test_extract_action():
    out = extract('Ananya: I will prepare the report by September 25, 2026.')
    assert len(out) == 1
    assert out[0]['owner'] == 'Ananya'
    assert 'prepare the report' in out[0]['task']
