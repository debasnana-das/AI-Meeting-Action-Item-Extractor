import sys
from pathlib import Path
import streamlit as st
sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))
from extractor import extract_actions

st.set_page_config(page_title='Meeting Action Extractor', layout='wide')
st.title('AI Meeting Action-Item Extractor')
text = st.text_area('Meeting transcript', height=300, value='''Manager: We need to close the sprint.
Ananya: I will prepare the Q3 sales dashboard by September 25, 2026.
Rohan: I will send the revised API documentation by September 28, 2026.''')
engine = st.selectbox('Extraction engine', ['fallback','auto','transformer'], index=0)
if st.button('Extract action items'):
    st.dataframe(extract_actions(text, engine), use_container_width=True)
