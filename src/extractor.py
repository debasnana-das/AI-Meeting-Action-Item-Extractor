try:
    from .fallback_extractor import extract as fallback_extract
except ImportError:
    from fallback_extractor import extract as fallback_extract

def _transformer_extract(transcript):
    try:
        from .transformer_extractor import extract_with_transformer
    except ImportError:
        from transformer_extractor import extract_with_transformer
    return extract_with_transformer(transcript)

def extract_actions(transcript, engine='auto'):
    if engine == 'fallback':
        return fallback_extract(transcript)

    if engine == 'transformer':
        # Transformer dependencies are optional in the lightweight deployment.
        try:
            return _transformer_extract(transcript)
        except Exception:
            return fallback_extract(transcript)

    # Auto mode prefers the transformer when its optional dependencies/model
    # are available and otherwise falls back to the deterministic extractor.
    try:
        return _transformer_extract(transcript)
    except Exception:
        return fallback_extract(transcript)
