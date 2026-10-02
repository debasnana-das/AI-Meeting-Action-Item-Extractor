def validate_item(item):
    required = ['task', 'owner', 'deadline', 'status', 'confidence']
    errors = [k for k in required if not item.get(k)]
    if item.get('status') not in {'open', 'in_progress', 'done', 'unknown'}:
        errors.append('status')
    conf = item.get('confidence')
    if conf is not None and not (0.0 <= float(conf) <= 1.0):
        errors.append('confidence')
    return errors

def normalize_status(text):
    t = text.lower()
    if any(x in t for x in ['done', 'completed', 'finished']):
        return 'done'
    if any(x in t for x in ['working on', 'in progress', 'started']):
        return 'in_progress'
    return 'open'
