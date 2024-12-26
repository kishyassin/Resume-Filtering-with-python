from fpdf import FPDF


def generate_pdf(filtered_data):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Selected Results", ln=True, align="C")
    pdf.ln(10)

    for person in filtered_data:
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(0, 10, txt=person["name"], ln=True)
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, txt=f"Email: {person['email']}", ln=True)
        pdf.cell(0, 10, txt=f"Phone: {person['phone']}", ln=True)
        pdf.cell(0, 10, txt=f"Location: {person['location']}", ln=True)
        skills = person.get("skills", [])
        if isinstance(skills, list):
            flat_skills = []
            for skill in skills:
                if isinstance(skill, dict):
                    for key in skill:
                        flat_skills.extend(skill[key])
                elif isinstance(skill, str):
                    flat_skills.append(skill)
            pdf.cell(0, 10, txt=f"Skills: {', '.join(flat_skills)}", ln=True)
        pdf.ln(10)

    return pdf.output(dest="S").encode("latin1")
