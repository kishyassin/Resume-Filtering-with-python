# Resume-Filtering-with-python
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://resume-filter.streamlit.app)

This project streamlines the recruitment process by automating the analysis and selection of candidates. It combines Python-based automation, advanced text extraction, and language model processing to deliver a comprehensive dashboard for candidate evaluation.

## Features

- Extract text from PDF resumes
- Convert extracted text to structured JSON format
- Filter candidates by tags
- Generate PDF reports of selected candidates
- Send recruitment messages to selected candidates

## Prerequisites

- Python 3.12
- Required Python packages (listed in `requirements.txt`)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/kishyassin/Resume-Filtering-with-python.git
    cd Resume-Filtering-with-python
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. Open the [configuration.py](http://_vscodecontentref_/0) file and add your API key, email, and password:
    ```python
    api_key = "your_grok_ai_api_key"
    email = "your_email@example.com"
    password = "your_password"
    ```

## Usage

1. Place your CVs in PDF format in the [Banque-CV](http://_vscodecontentref_/1) folder.

2. Run the [pdf-to-text-to-json.py](http://_vscodecontentref_/2) script to extract text from the PDFs and convert it to JSON format:
    ```sh
    python pdf-to-text-to-json.py
    ```

3. Run the [dashboard.py](http://_vscodecontentref_/3) script to start the Streamlit dashboard:
    ```sh
    streamlit run dashboard.py
    ```

## Project Structure

- [Banque-CV](http://_vscodecontentref_/4): Folder to store CVs in PDF format.
- [banque-cv.json](http://_vscodecontentref_/5): JSON file containing extracted and structured CV data.
- [configuration.py](http://_vscodecontentref_/6): Configuration file for API key, email, and password.
- [dashboard.py](http://_vscodecontentref_/7): Streamlit dashboard for managing and filtering CVs.
- [functions_logic](http://_vscodecontentref_/8): Folder containing logic for various functions.
  - [extract_json_from_text.py](http://_vscodecontentref_/9): Extracts JSON data from text using Groq AI.
  - [extract_text_from_pdf.py](http://_vscodecontentref_/10): Extracts text from PDF files.
  - [filter_by_tags.py](http://_vscodecontentref_/11): Filters CVs by tags.
  - [generate_pdf.py](http://_vscodecontentref_/12): Generates PDF reports of selected CVs.
  - [send_recruitment_message.py](http://_vscodecontentref_/13): Sends recruitment messages via email.
- [LICENSE](http://_vscodecontentref_/14): License file.
- [pdf-to-text-to-json.py](http://_vscodecontentref_/15): Script to process CVs from PDF to JSON.
- [README.md](http://_vscodecontentref_/16): This file.
- [requirements.txt](http://_vscodecontentref_/17): List of required Python packages.

## License

This project is licensed under the MIT License - see the [LICENSE](http://_vscodecontentref_/18) file for details.

## Acknowledgments

- Groq AI for text extraction and language model processing.
- Streamlit for the interactive dashboard.
- PyPDF2 for PDF text extraction.
- FPDF for PDF generation.