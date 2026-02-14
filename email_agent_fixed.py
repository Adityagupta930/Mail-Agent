import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class EmailAgent:
    def __init__(self, sender_email, sender_password):
        self.sender_email = sender_email
        self.sender_password = sender_password
        
    def send_emails(self, content, hr_list_file, resume_folder):
        # Read HR email list
        with open(hr_list_file, 'r') as f:
            hr_emails = [line.strip() for line in f if line.strip()]
        
        # Get PDF files
        pdf_files = [f for f in os.listdir(resume_folder) if f.endswith('.pdf')]
        
        # Try different SMTP settings
        smtp_configs = [
            ('smtp.gmail.com', 587),
            ('smtp.gmail.com', 465),
        ]
        
        for smtp_server, port in smtp_configs:
            try:
                print(f"Trying {smtp_server}:{port}...")
                
                if port == 465:
                    server = smtplib.SMTP_SSL(smtp_server, port)
                else:
                    server = smtplib.SMTP(smtp_server, port)
                    server.starttls()
                
                server.login(self.sender_email, self.sender_password)
                
                for hr_email in hr_emails:
                    try:
                        msg = MIMEMultipart()
                        msg['From'] = self.sender_email
                        msg['To'] = hr_email
                        msg['Subject'] = "Job Application"
                        
                        msg.attach(MIMEText(content, 'plain'))
                        
                        # Attach PDFs
                        for pdf_file in pdf_files:
                            pdf_path = os.path.join(resume_folder, pdf_file)
                            with open(pdf_path, "rb") as attachment:
                                part = MIMEBase('application', 'octet-stream')
                                part.set_payload(attachment.read())
                            
                            encoders.encode_base64(part)
                            part.add_header('Content-Disposition', f'attachment; filename= {pdf_file}')
                            msg.attach(part)
                        
                        server.send_message(msg)
                        print(f"Email sent to {hr_email}")
                        
                    except Exception as e:
                        print(f"Failed to send to {hr_email}: {e}")
                
                server.quit()
                return True
                
            except Exception as e:
                print(f"SMTP {smtp_server}:{port} failed: {e}")
                continue
        
        print("All SMTP methods failed!")
        return False