# 🔍 Google Dork Generator

A powerful and user-friendly Streamlit web application for generating Google Dorks (advanced search queries) for OSINT (Open Source Intelligence) investigations.

## ✨ Features

### 📱 **Phone Number Dorks**
- Generate comprehensive search patterns for phone numbers
- Supports multiple formatting variations (with/without parentheses, dashes, spaces)
- Useful for finding leaked phone numbers in documents and websites

### 🆔 **CPF Number Dorks**
- Create search queries for Brazilian CPF numbers
- Multiple format variations (with/without dots and dashes)
- Perfect for Brazilian OSINT investigations

### 📄 **Web Hosted Documents**
- Search for documents (PDF, Excel, Word) containing specific names
- Ideal for finding leaked documents, resumes, or official papers
- Supports multiple file formats simultaneously

### 💬 **Social Media Group Chats**
- **WhatsApp Groups**: Find public WhatsApp group links by topic
- **Telegram Groups**: Discover Telegram group invites with specific keywords
- Great for community research and social network analysis

### 📸 **Instagram Comments**
- Search for Instagram posts and comments mentioning specific usernames
- Useful for social media investigations and reputation monitoring

## 🚀 Quick Start

### Method 1: Using the Batch File (Recommended for Windows)
1. Double-click `run.bat`
2. The application will automatically start and open in your browser
3. Press `Ctrl+C` in the command window to stop

### Method 2: Manual Setup
1. **Open Command Prompt**
   ```cmd
   cd path\to\GoogleDorkGenerator
   ```

2. **Create Virtual Environment**
   ```cmd
   pip install virtualenv
   virtualenv .env
   ```

3. **Activate Virtual Environment**
   ```cmd
   .env\Scripts\activate
   ```

4. **Install Dependencies**
   ```cmd
   pip install -r requirements.txt
   ```

5. **Run the Application**
   ```cmd
   streamlit run main.py
   ```

## 📋 Requirements

- Python 3.7+
- Streamlit
- Pyperclip

All dependencies are listed in `requirements.txt`

## 🛠️ Usage Guide

1. **Launch the Application**: Use `run.bat` or follow manual setup
2. **Choose Your Dork Type**: Navigate to the section you need
3. **Enter Your Query**: Fill in the required information (phone, name, username, etc.)
4. **Generate Dork**: Click the generate button
5. **Copy & Use**: The dork is automatically copied to clipboard, or use the copy button
6. **Clear Results**: Use the clear button when you're done

## 📊 Example Outputs

### Phone Number Dork
```
"1234567890" OR "12345-67890" OR "(12)34567-67890" OR "(12) 34567-67890"
```

### Document Search Dork
```
"John Doe" filetype:pdf OR filetype:xlsx OR filetype:docx
```

### WhatsApp Group Dork
```
site:chat.whatsapp.com "hacking"
```

## 🔧 Development

### Adding New Dork Types
1. Add session state variable for the new dork type
2. Create a formatting function following the existing pattern
3. Add the UI section with input, generate button, and copy/clear functionality

### Updating Dependencies
```cmd
pip freeze > requirements.txt
```

## ⚠️ Ethical Usage

This tool is designed for legitimate OSINT investigations, security research, and educational purposes. Please ensure you:

- Comply with local laws and regulations
- Respect privacy and data protection guidelines
- Use responsibly for legitimate research purposes
- Don't use for malicious activities or harassment

## 🤝 Contributing

Contributions are welcome! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) file for detailed guidelines on how to contribute to this project.

## 🔒 Security

Security vulnerabilities should be reported responsibly. Please see our [SECURITY.md](SECURITY.md) file for detailed instructions on how to report security issues.

## 📄 License

This project is open source. Please use responsibly and ethically.

## 🚨 Disclaimer

This tool is for educational and legitimate research purposes only. Users are responsible for ensuring their usage complies with applicable laws and regulations. The developers are not responsible for any misuse of this tool.

---

**Happy Dorking! 🔍✨**