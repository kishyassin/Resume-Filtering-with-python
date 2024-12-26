import os
import json
from functions_logic.extract_text_from_pdf import extract_text_from_pdf
from functions_logic.extract_json_from_text import extract_json_from_text_with_grok_ai

def process_cv_folder(folder_path="Banque-CV"):
    json_results = []

    pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
    pdf_paths = [os.path.join(folder_path, f) for f in pdf_files]

    for pdf_path in pdf_paths:
        output_text = extract_text_from_pdf(pdf_path)
        result = extract_json_from_text_with_grok_ai(output_text)
        json_results.append(result)

    with open('banque-cv2.json', 'w', encoding='utf-8') as json_file:
        json.dump(json_results, json_file, ensure_ascii=False, indent=4)


process_cv_folder()