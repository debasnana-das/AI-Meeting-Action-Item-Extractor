import json

PROMPT = '''Extract action items from the meeting transcript below. Return ONLY a JSON array. Each object must have exactly these keys: task, owner, deadline, status, confidence. Use status open, in_progress, or done. Use unknown when a field is missing. confidence must be a number from 0 to 1.\n\nTRANSCRIPT:\n'''

def extract_with_transformer(transcript, model_name='google/flan-t5-small'):
    try:
        from transformers import pipeline
    except ImportError as exc:
        raise RuntimeError('transformers is not installed') from exc
    pipe = pipeline('text2text-generation', model=model_name)
    raw = pipe(PROMPT + transcript, max_new_tokens=512, do_sample=False)[0]['generated_text']
    raw = raw.strip().replace('`' * 3 + 'json', '').replace('`' * 3, '').strip()
    data = json.loads(raw)
    if not isinstance(data, list):
        raise ValueError('Transformer did not return a JSON array.')
    return data
