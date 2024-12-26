import json
import re
import configuration #file with your configurations
from groq import Groq

def extract_json_from_text_with_grok_ai(output_text):
    client = Groq(
    api_key=configuration.api_key,
    )
    prompt  = f"""
        Extract the following fields from the given resume text and correct the ortograph/spelling and return them in the specified JSON format:
        name: The candidate's full name.
        email: The candidate's email address.
        phone: The candidate's phone number.
        skills: A list of skills mentioned in the resume.
        experience: A list of job experiences. Each job should include:
        job_title: The title of the job.
        company: The name of the company.
        start_date: The start date of the job (if available).
        end_date: The end date of the job (or "Present" if ongoing).
        responsibilities: A summary of the responsibilities or achievements in the job.
        education: A list of educational qualifications. Each qualification should include:
        degree: The degree obtained.
        institution: The name of the educational institution.
        start_date: The start date of the program (if available).
        end_date: The end date of the program.
        certifications: A list of certifications. Each certification should include:
        name: The name of the certification.
        issuing_organization: The organization that issued the certification.
        issue_date: The date the certification was issued (if available).
        location: The candidate's current location (if mentioned).
        Resume text:
        {output_text}
        """
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
    )

    # Extraire la réponse du chat
    json_pattern = r'\{.*\}'
    match = re.search(json_pattern, chat_completion.choices[0].message.content, re.DOTALL)

    if match:
        # Extraire le JSON
        json_data = match.group(0)
        try:
            # Charger le JSON extrait
            parsed_json = json.loads(json_data)
            return parsed_json
        except json.JSONDecodeError as e:
            print(f"Erreur de décodage JSON: {e}")
    else:
        print("Aucun JSON trouvé.")