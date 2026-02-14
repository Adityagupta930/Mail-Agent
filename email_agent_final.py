import smtplib
import os
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailAgent:
    def __init__(self, sender_email, sender_password):
        self.sender_email = sender_email
        self.sender_password = sender_password
        
    def send_emails_from_excel(self, excel_file):
        # Read Excel/CSV file
        if excel_file.endswith('.csv'):
            df = pd.read_csv(excel_file)
        else:
            df = pd.read_excel(excel_file)
        
        # Add Email_Sent column if not exists
        if 'Email_Sent' not in df.columns:
            df['Email_Sent'] = 'No'
        
        # SMTP setup with multiple configs
        smtp_configs = [
            ('smtp.gmail.com', 587),
            ('smtp.gmail.com', 465),
        ]
        
        for smtp_server, port in smtp_configs:
            try:
                print(f"Connecting to {smtp_server}:{port}...")
                
                if port == 465:
                    server = smtplib.SMTP_SSL(smtp_server, port)
                else:
                    server = smtplib.SMTP(smtp_server, port)
                    server.starttls()
                
                server.login(self.sender_email, self.sender_password)
                
                # Send emails
                for index, row in df.iterrows():
                    # Check if email already sent
                    if row.get('Email_Sent', 'No') == 'Yes':
                        print(f"Email already sent to {row['EMAIL']} - Skipping")
                        continue
                    
                    name = row['Contact Person']
                    email = row['EMAIL']
                    company = row['Company Name']
                    
                    try:
                        # Create personalized HTML content
                        html_content = f"""<html>
<body style="font-family: Georgia, serif; font-size: 14px; line-height: 1.6;">
<p>Dear {name},</p>

<p>Greetings from <strong style="font-size: 16px;">KrishiGyanAI</strong>, the agritech division of <strong style="font-size: 16px;">Luminoid Technologies Private Limited</strong>.</p>

<p>I am <strong style="font-size: 16px;">Nandini Bankar</strong>, and I am writing to explore a strategic collaboration to support <strong style="font-size: 16px;">digital transformation, technology adoption, and performance monitoring of FPOs</strong> under your esteemed organisation's ecosystem.</p>

<h3><strong>Who We Are</strong></h3>
<p><strong style="font-size: 16px;">KrishiGyanAI</strong> is an AI-driven agritech initiative focused on <strong style="font-size: 16px;">digitising FPOs and empowering farmers through actionable, localised intelligence</strong>. Our solutions are designed to help FPOs and their member farmers <strong style="font-size: 16px;">improve productivity by 25% to 50%</strong>, while strengthening governance, communication, and decision-making.</p>

<h3><strong>Our Core Thought & Vision (Beyond a Generic App)</strong></h3>
<p>Our approach is <strong style="font-size: 16px;">not a one-size-fits-all agriculture app</strong>. Instead, we are building a <strong style="font-size: 16px;">structured digital ecosystem</strong> with three clear layers:</p>

<h4><strong>1. Dedicated Mobile App for Every FPO</strong></h4>
<ul>
<li>Each FPO gets its own branded mobile application</li>
<li><strong style="font-size: 16px;">Aligned and role-based communication:</strong> Messages, advisories, and updates are delivered only to relevant members, ensuring clarity and trust</li>
<li>Digital farmer onboarding, crop records, advisory alerts, and productivity tracking</li>
</ul>

<h4><strong>2. AI-Powered, Geography-Specific Intelligence</strong></h4>
<ul>
<li>AI analyses <strong style="font-size: 16px;">crop, soil, weather, input usage, and field data</strong></li>
<li>Challenges are <strong style="font-size: 16px;">tracked geographically</strong> (village / cluster / FPO-wise)</li>
<li>Enables <strong style="font-size: 16px;">early identification of stress, gaps, and risks</strong>, instead of generic recommendations</li>
<li>Supports precision decisions tailored to local cropping patterns and conditions</li>
</ul>

<h4><strong>3. Unified CBBO Monitoring Dashboard</strong></h4>
<ul>
<li>A <strong style="font-size: 16px;">single central dashboard</strong> for CBBOs to monitor <strong style="font-size: 16px;">all supported FPOs</strong></li>
<li>Real-time visibility into:
<ul>
<li>Farmer engagement and adoption</li>
<li>Crop stages and productivity indicators</li>
<li>Input distribution and utilisation</li>
<li>Advisory impact and response</li>
<li>Red-flag challenges mapped geographically</li>
</ul>
</li>
<li>AI assists CBBO teams in <strong style="font-size: 16px;">prioritising interventions, audits, and support</strong>, improving governance efficiency</li>
</ul>

<h3><strong>Why KrishiGyanAI Is the Right Partner</strong></h3>
<ul>
<li>Designed specifically for <strong style="font-size: 16px;">FPO–CBBO ecosystems</strong></li>
<li>AI that supports <strong style="font-size: 16px;">decision-making, not just data display</strong></li>
<li>Scalable across districts, states, and commodity clusters</li>
<li>Strong alignment with national priorities on <strong style="font-size: 16px;">FPO digitisation and tech adoption</strong></li>
<li>Built by a product-focused team with real on-ground farmer engagement</li>
</ul>

<p>We believe <strong style="font-size: 16px;">KrishiGyanAI</strong> can significantly support <strong>{company}</strong> in enhancing FPO performance, transparency, and farmer outcomes at scale.</p>

<p>We would welcome the opportunity to <strong style="font-size: 16px;">present a short demo and pilot framework</strong> aligned to your operational objectives. Kindly let us know a suitable time for a discussion.</p>

<p>Thank you for your time and consideration. We look forward to the possibility of working together.</p>

<p style="color: #228B22;">--<br>
<strong>Warm Regards,</strong><br>
Nandini Bankar<br>
KrishiGyanAI | Luminoid Technologies Pvt. Ltd.<br>
+91 7558421307<br>
nandani@krishigyanai.com<br>
www.krishigyanai.com<br>
<a href="https://www.linkedin.com/company/luminoidtechnologies" style="color: #228B22;">LinkedIn</a></p>

</body>
</html>"""

                        # Create message
                        msg = MIMEMultipart()
                        msg['From'] = self.sender_email
                        msg['To'] = email
                        msg['Subject'] = f"Strategic Partnership Opportunity - KrishiGyanAI & {company}"
                        
                        msg.attach(MIMEText(html_content, 'html'))
                        
                        server.send_message(msg)
                        print(f"Email sent to {email} ({name} - {company})")
                        
                        # Mark as sent
                        df.at[index, 'Email_Sent'] = 'Yes'
                        
                    except Exception as e:
                        print(f"Failed to send to {email}: {e}")
                
                server.quit()
                
                # Save updated CSV/Excel file
                if excel_file.endswith('.csv'):
                    df.to_csv(excel_file, index=False)
                else:
                    df.to_excel(excel_file, index=False)
                
                print(f"File updated with email status: {excel_file}")
                return True
                
            except Exception as e:
                print(f"SMTP {smtp_server}:{port} failed: {e}")
                continue
        
        print("All SMTP methods failed!")
        return False