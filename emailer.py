import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(to_email: str, topic: str, zip_file_path: str):
    msg = EmailMessage()
    msg['Subject'] = f"Your Report on '{topic}'"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    msg.set_content(f"Hi,\n\nPlease find attached your report on: {topic}.\n\nBest regards,\nThe Report Bot")

    with open(zip_file_path, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(zip_file_path)
        msg.add_attachment(file_data, maintype='application', subtype='zip', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
