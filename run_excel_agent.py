from email_agent_final import EmailAgent

# Configuration
SENDER_EMAIL = "goravgupta021103@gmail.com"
SENDER_PASSWORD = "crdv vpap cftv aoct"  # Update this!

# Run the agent
if __name__ == "__main__":
    print("Starting KrishiGyanAI Email Agent...")
    
    agent = EmailAgent(SENDER_EMAIL, SENDER_PASSWORD)
    
    try:
        agent.send_emails_from_excel(
            excel_file="contacts.csv"
        )
        print("All emails sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure:")
        print("1. contacts.csv has 'Email' and 'Company' columns")
        print("2. Gmail app password is correct")