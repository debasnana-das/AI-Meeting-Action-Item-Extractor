# AI Meeting Action-Item Extractor

An AI-powered meeting intelligence system designed to automatically extract and structure actionable tasks from meeting transcripts, including task ownership, deadlines, status, and confidence. Developed using Python, NLP, transformer-based models, FastAPI, and Streamlit.

## Objective
Convert a meeting transcript into structured action items containing task, owner, deadline, status, and confidence.

## Extraction Design
The project supports Transformer mode using Hugging Face Transformers and google/flan-t5-small, plus a deterministic fallback engine for reliable local and Streamlit deployment.

## Architecture
transcript -> speaker/sentence segmentation -> action extraction -> validation -> duplicate removal -> structured JSON

## Installation
```bash
pip install -r requirements.txt
```

## Generate Development Data
```bash
python data/generate_dataset.py
```

## Evaluate
```bash
python src/evaluate.py
```

## Run API
```bash
uvicorn app.api:app --reload
```

## Run Streamlit
Use app/streamlit_app.py as the main file.

```bash
streamlit run app/streamlit_app.py
```

The UI defaults to fallback extraction for reliable startup. Transformer mode remains available and may download google/flan-t5-small on first use.

## Development Data
The dataset is synthetic and intended for development and demonstration.
