# Function to send recruitment message via SMTP
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import configuration


def send_recruitment_message(filtered_data, subject, body):
    sender_email = configuration.email
    sender_password = configuration.password
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    recipient_email = sender_email

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        for person in filtered_data:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject

            body_content = f"Message sent to {person['name']} ({person['email']}):\n\n{body}\n\n" \
                           f"Name: {person['name']}\n" \
                           f"Email: {person['email']}\n" \
                           f"Phone: {person['phone']}\n" \
                           f"Location: {person['location']}\n" \
                           f"Skills: {', '.join(person.get('skills', []))}"

            msg.attach(MIMEText(body_content, 'plain'))
            server.sendmail(sender_email, recipient_email, msg.as_string())

        server.quit()
        return True
    except Exception as e:
        print(f"Error sending emails: {e}")
        return False
