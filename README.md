# KrishiGyanAI Email Agent 🚀

**Automated email marketing agent for KrishiGyanAI partnership outreach**

## 📋 Quick Start

### Prerequisites
- Python 3.7+
- Gmail account with 2-factor authentication

### Installation & Setup

1. **Create Virtual Environment**
   ```bash
   # Windows
   python -m venv email_agent_env
   email_agent_env\Scripts\activate
   
   # Mac/Linux
   python3 -m venv email_agent_env
   source email_agent_env/bin/activate
   ```

2. **Install Dependencies**
   ```bash
   pip install pandas openpyxl
   ```

3. **Gmail Setup**
   - Go to [Google Account Security](https://myaccount.google.com/security)
   - Enable **2-Step Verification**
   - Generate **App Password** for Mail
   - Copy the 16-digit password

4. **Configure Credentials**
   Edit `run_excel_agent.py`:
   ```python
   SENDER_EMAIL = "your_email@gmail.com"
   SENDER_PASSWORD = "your_16_digit_app_password"
   ```

5. **Run the Agent**
   ```bash
   python run_excel_agent.py
   ```

## 📁 Project Structure
```
New folder/
├── 📄 email_agent_final.py    # Main email agent
├── 🚀 run_excel_agent.py      # Runner script
├── 📊 contacts.csv            # Your contact data
├── 📋 requirements.txt        # Dependencies
└── 📖 README.md              # This file
```

## 📊 CSV File Format

### Required Columns
| Column | Description | Example |
|--------|-------------|---------|
| **State** | Company state | Maharashtra |
| **District** | Company district | Mumbai |
| **CIN** | Company ID | U12345MH2020PTC123456 |
| **Company Name** | Full company name | ABC FARMERS PRODUCER COMPANY |
| **Date of Registration** | Registration date | 2020-01-15 |
| **Registered Office Address** | Company address | 123 Main Street Mumbai |
| **Contact Person** | Contact name | Mr. Sharma |
| **Contact No.** | Phone number | 9876543210 |
| **EMAIL** | Email address | hr@company1.com |
| **Email_Sent** | Tracking status | No/Yes (auto-added) |

### Sample CSV
```csv
State,District,CIN,Company Name,Date of Registration,Registered Office Address,Contact Person,Contact No.,EMAIL,Email_Sent
Maharashtra,Mumbai,U12345MH2020PTC123456,ABC FARMERS PRODUCER COMPANY,2020-01-15,123 Main Street Mumbai,Mr. Sharma,9876543210,hr@company1.com,No
```

## ✨ Features

### 🎯 Smart Email Targeting
- Personalized greetings using **Contact Person**
- Company-specific content with **Company Name**
- Professional HTML formatting with Georgia font

### 🔄 Duplicate Prevention
- **Email_Sent** column tracks sent emails
- Automatically skips already contacted companies
- Safe to run multiple times

### 📧 Email Content
- **KrishiGyanAI** partnership proposal
- **Bold keywords** and professional formatting
- **Green signature** with contact details
- **LinkedIn** integration

### 🛡️ Error Handling
- Multiple SMTP configurations
- Detailed error logging
- Automatic file updates

## 🚀 Usage Workflow

1. **Prepare CSV** with company data
2. **Update credentials** in runner script
3. **Run agent** - sends emails to new contacts
4. **Check results** - Email_Sent column updated
5. **Add more contacts** - only new ones get emails

## 🔧 Troubleshooting

### Gmail Authentication Error (535)
- ✅ Enable 2-factor authentication
- ✅ Use App Password (not regular password)
- ✅ Check 16-digit password format

### Module Not Found
- ✅ Activate virtual environment
- ✅ Install dependencies: `pip install pandas openpyxl`

### CSV Reading Error
- ✅ Check column names match exactly
- ✅ Save as UTF-8 encoding
- ✅ No extra spaces in headers

### Email Not Sending
- ✅ Check internet connection
- ✅ Verify email addresses are valid
- ✅ Check Gmail sending limits

## 📝 Email Template

The agent sends professional partnership emails with:
- Personal greeting to **Contact Person**
- **KrishiGyanAI** company introduction
- **3-layer digital ecosystem** explanation
- **Partnership benefits** for their company
- **Demo request** call-to-action
- **Professional signature** with contact details

## 🎨 Email Formatting
- **Font**: Georgia (professional serif)
- **Bold keywords**: KrishiGyanAI, key benefits
- **Green signature**: #228B22 color
- **HTML structure**: Proper headings and bullet points

## 📞 Support

For issues:
1. Check Gmail App Password setup
2. Verify CSV file format
3. Ensure virtual environment is activated
4. Confirm all dependencies are installed

---

**Built for KrishiGyanAI partnership outreach** 🌱