from pathlib import Path
import json
import random

random.seed(42)
OUT = Path(__file__).resolve().parent / 'meeting_samples.jsonl'
people = ['Ananya','Rohan','Priya','Arjun','Meera','Kunal']
tasks = [
    'prepare the Q3 sales dashboard',
    'send the revised API documentation',
    'review the security checklist',
    'schedule the client demo',
    'update the onboarding workflow',
    'share the budget spreadsheet',
    'test the new mobile build',
]
dates = ['September 25, 2026','September 28, 2026','October 2, 2026','October 5, 2026']
status = 'open'

with OUT.open('w', encoding='utf-8') as f:
    for i in range(180):
        owner = random.choice(people)
        task = random.choice(tasks)
        deadline = random.choice(dates)
        transcript = (
            f"Meeting {i+1}.\n"
            f"Manager: We need to close the next sprint items.\n"
            f"{owner}: I will {task} by {deadline}.\n"
            f"Manager: Please confirm the deadline.\n"
            f"{owner}: Confirmed. It is {deadline}.\n"
        )
        gold = [{
            'task': task,
            'owner': owner,
            'deadline': deadline,
            'status': status,
            'confidence': 1.0,
        }]
        f.write(json.dumps({'transcript': transcript, 'gold': gold}) + '\n')
print(f'Wrote {180} examples to {OUT}')
