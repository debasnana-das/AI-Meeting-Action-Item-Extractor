try:
    from .fallback_extractor import extract as fallback_extract
except ImportError:
    from fallback_extractor import extract as fallback_extract

def extract_actions(transcript, engine='auto'):
    if engine == 'fallback':
        return fallback_extract(transcript)
    if engine == 'transformer':
        from .transformer_extractor import extract_with_transformer
        return extract_with_transformer(transcript)
    try:
        from .transformer_extractor import extract_with_transformer
        return extract_with_transformer(transcript)
    except Exception:
        return fallback_extract(transcript)
