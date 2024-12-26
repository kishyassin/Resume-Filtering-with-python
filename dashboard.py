import streamlit as st
import json

from functions_logic.filter_by_tags import filter_by_tags
from functions_logic.generate_pdf import generate_pdf
from functions_logic.send_recruitment_message import send_recruitment_message


# Load data from JSON file
def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

data = load_data('banque-cv.json')


# Streamlit interface
st.set_page_config(page_title="CV Management Dashboard", layout="wide")
st.title("CV Management Dashboard")

# Sidebar for actions
st.sidebar.title("Actions")
tags_input = st.sidebar.text_input("Add a tag (separated by commas)", key="tag_input")
if st.sidebar.button("Add Tags"):
    tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
    if "tags" in st.session_state:
        st.session_state["tags"].extend(tags)
    else:
        st.session_state["tags"] = tags

if st.sidebar.button("Clear Tags"):
    st.session_state["tags"] = []

# Display added tags
if "tags" in st.session_state and st.session_state["tags"]:
    st.sidebar.write("Selected tags:", ", ".join(st.session_state["tags"]))

# Display filtered results in real-time
if "tags" not in st.session_state or not st.session_state["tags"]:
    filtered_data = data
else:
    tags = st.session_state["tags"]
    filtered_data = filter_by_tags(data, tags)

selected_cvs = []
st.write(f"**{len(filtered_data)} result(s) found:**")
for person in filtered_data:
    if st.checkbox(f"Select {person['name']}", key=person['email']):
        selected_cvs.append(person)
    st.subheader(person["name"])
    st.write(f"📧 Email: {person['email']}")
    st.write(f"📞 Phone: {person['phone']}")
    st.write(f"📌 Location: {person['location']}")
    skills = person.get("skills", [])
    if isinstance(skills, list):
        flat_skills = []
        for skill in skills:
            if isinstance(skill, dict):
                for key in skill:
                    flat_skills.extend(skill[key])
            elif isinstance(skill, str):
                flat_skills.append(skill)
        st.write("💼 Skills:", ", ".join(flat_skills))
    st.write("---")

# Button to download selected results as PDF
if st.sidebar.button("Download selected results as PDF"):
    if selected_cvs:
        pdf_output = generate_pdf(selected_cvs)
        st.sidebar.download_button(
            label="Download PDF",
            data=pdf_output,
            file_name="selected_results.pdf",
            mime="application/pdf"
        )
    else:
        st.sidebar.error("No CVs selected for download.")

# Form to send recruitment message
st.sidebar.title("Send Recruitment Message")
subject = st.sidebar.text_input("Subject")
body = st.sidebar.text_area("Message")

if st.sidebar.button("Send message to candidates"):
    if subject and body:
        send_recruitment_message(selected_cvs, subject, body)
        st.sidebar.success("All messages have been sent successfully!", icon="✅")
    else:
        st.sidebar.error("Please provide both subject and message.")
st.write("Add tags to see filtered results.")