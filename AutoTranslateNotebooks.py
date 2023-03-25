import json, googletrans, os, re, argparse
import nbformat
from googletrans import Translator

# Google Translate API limit text to 5000 characters for each request
# this code piece splits long markdown text into shorter ones so no 
# exceptions returned
def segment_text(text_list, max_chars=2000):
    segments = []
    current_segment = ''
    current_word_count = 0

    for text in text_list.split('.'):              
        text_len = len(text)
        if current_word_count + text_len <= max_chars:
            current_segment += text + '.'
            current_word_count += text_len
        else:
            segments.append(current_segment.strip())
            current_segment = text
            current_word_count = len(text)

    if current_segment:
        segments.append(current_segment.strip())

    return segments

def TranslateNBText(Gtranslator, text, max_characters = 2000, src_lang='en', dest_lang='zh-cn'):
    translator = Gtranslator
    TranslatedTextList = []    
    TranslatedText = ''
    # null strings will return NoneType error, using strip() to handle
    if len(str(text).strip())>0:
        #limit to fewer characters for API call
        text_segments = segment_text(text, max_chars=max_characters)
        for ts in text_segments:
            outtext = translator.translate(str(ts), src=src_lang, dest=dest_lang)                
            TranslatedTextList.append(outtext.text)            
            
    for element in TranslatedTextList:
        TranslatedText += element+'.'
        
    return(TranslatedText)

# Set up translator object
translator = Translator()

# Load Jupyter notebook from arguments
parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='the input Jupyter Notebook file')
parser.add_argument('output_file', help='the output Juypter Notebook file to write to')
args = parser.parse_args()

#notebook_file = 'chapters/Chapter01-Copy.ipynb'
#notebook_path = os.path.abspath(notebook_file)
notebook_path = args.input_file
with open(notebook_path, encoding='UTF-8') as f:
    nb = nbformat.read(f, as_version=4)

# Loop through cells and translate markdown cells
for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        source_text = cell['source']
        # Translate source text to Chinese        
        translated_text = TranslateNBText(translator, source_text)
        # Replace original text with translated text
        cell['source'] = translated_text

# Save updated notebook
#notebook_path2 = notebook_path.split('.')[0]+'_cn.'+notebook_path.split('.')[1]
with open(args.output_file, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)
    