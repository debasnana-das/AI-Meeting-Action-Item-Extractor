from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))
from extractor import extract_actions

app = FastAPI(title='AI Meeting Action-Item Extractor', version='1.0')

class Meeting(BaseModel):
    transcript: str
    engine: str = 'auto'

@app.get('/')
def root():
    return {'project':'AI Meeting Action-Item Extractor','status':'ready'}

@app.post('/extract')
def extract(item: Meeting):
    if not item.transcript.strip():
        raise HTTPException(status_code=400, detail='Transcript cannot be empty.')
    try:
        actions = extract_actions(item.transcript, item.engine)
        return {'action_items': actions, 'count': len(actions), 'engine_requested': item.engine}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
