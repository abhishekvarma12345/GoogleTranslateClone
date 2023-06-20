import streamlit as st
from languages import LANGUAGES
from translator import LanguageTranslator


# initializing language translator object
langtranslator = LanguageTranslator()

# streamlit app
# Page configs (tab title, favicon)
st.set_page_config(
    page_title="Google Translate Clone",
    page_icon="🤓",
)

st.write("<h2>Translate any language to any other language</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    src_lang = st.selectbox('Source Language', LANGUAGES, index=26)
    text = st.text_area('Enter text to translate', placeholder="Enter the text",height=150)

with col2:
    dest_lang = st.selectbox('Destination Language', LANGUAGES, index=52)
    translation_text = st.empty()
    translation_text.text_area('Translation', placeholder="translating...", height=150)

if st.button('Translate'):
    dst_translation = langtranslator.translate(source_lang=src_lang, dst_lang=dest_lang, text=text)
    translation_text.text_area('Translation', value=dst_translation, height=150)