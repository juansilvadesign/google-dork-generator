import streamlit as st
import pyperclip

# Initialize session state
if 'phone_result' not in st.session_state:
    st.session_state.phone_result = None
if 'cpf_result' not in st.session_state:
    st.session_state.cpf_result = None
if 'docs_result' not in st.session_state:
    st.session_state.docs_result = None
if 'whatsapp_result' not in st.session_state:
    st.session_state.whatsapp_result = None
if 'telegram_result' not in st.session_state:
    st.session_state.telegram_result = None
if 'instagram_result' not in st.session_state:
    st.session_state.instagram_result = None

def format_phone_number(phone_number):
  """Formats a phone number as (XX) XXXXX-XXXX.

  Args:
      phone_number: A string containing the phone number.

  Returns:
      The formatted phone number, or None if the input is invalid.
  """

  # Remove non-numeric characters
  digits = "".join([char for char in phone_number if char.isdigit()])

  # Format the phone number
  area_code = digits[:2]
  first_part = digits[2:7]
  second_part = digits[7:]
  spare_part1 = digits[2:3]
  spare_part2 = digits[3:7]
  formatted_number = f'"{area_code}{first_part}{second_part}" OR "{area_code}{first_part}-{second_part}" OR "({area_code}){first_part}-{second_part}" OR "({area_code}) {first_part}-{second_part}" OR "{area_code} {spare_part1} {spare_part2} {second_part}" OR "({area_code}) {spare_part1} {spare_part2}-{second_part}" OR "({area_code}) {spare_part1} {spare_part2} - {second_part}" OR "({area_code}){spare_part1}-{spare_part2}-{second_part}"'


  return formatted_number

# OR "{area_code} {first_part} {second_part}" OR "({area_code}) {first_part} - {second_part}" OR "( {area_code} ) {first_part} - {second_part}" OR "( {area_code} ) {spare_part1} {spare_part2} - {second_part}" OR "({area_code}) {first_part}-{second_part}"

def format_cpf_number(cpf_number):
  digits = "".join([char for char in cpf_number if char.isdigit()])

  cpf_part1 = digits[:3]
  cpf_part2 = digits[3:6]
  cpf_part3 = digits[6:9]
  cpf_part4 = digits[9:]
  formatted_cpf = f'"{cpf_part1}{cpf_part2}{cpf_part3}{cpf_part4}" OR "{cpf_part1}.{cpf_part2}.{cpf_part3}-{cpf_part4}"'

  return formatted_cpf

def format_docs_dork(name):
  """Generate Google dork for documents containing a specific name."""
  formatted_docs = f'"{name}" filetype:pdf OR filetype:xlsx OR filetype:docx'
  return formatted_docs

def format_whatsapp_dork(search_term):
  """Generate Google dork for WhatsApp group chats."""
  formatted_whatsapp = f'site:chat.whatsapp.com "{search_term}"'
  return formatted_whatsapp

def format_telegram_dork(search_term):
  """Generate Google dork for Telegram group chats."""
  formatted_telegram = f'site:t.me/joinchat "{search_term}"'
  return formatted_telegram

def format_instagram_dork(username):
  """Generate Google dork for Instagram comments/mentions."""
  formatted_instagram = f'site:instagram.com intext:"{username}" OR site:instagram.com "{username}"'
  return formatted_instagram

# Streamlit app
st.title("Phone Number")

# Input field for phone number
phone_number = st.text_input("Enter a phone number:")

# Button to trigger formatting and copy functionality
if st.button("Generate Phone Dork"):
  # Call the formatting function and display the result
  formatted_number = format_phone_number(phone_number)
  if formatted_number:
    try:
      pyperclip.copy(formatted_number)
      st.session_state.phone_result = formatted_number
      st.success(f"Phone number Dork created: {formatted_number}")
    except Exception as e:
      st.error(f"Error copying to clipboard: {e}")
  else:
    st.error("Invalid phone number format.")

# Display copy and clear buttons for phone if result exists
if st.session_state.phone_result:
  col1, col2 = st.columns([1, 4])
  with col1:
    if st.button("📋 Copy dork", key="copy_phone"):
      pyperclip.copy(st.session_state.phone_result)
      st.success("✅ Copied")
  with col2:
    if st.button("🗑️ Clear Result", key="clear_phone"):
      st.session_state.phone_result = None
      st.rerun()

# Streamlit app
st.title("CPF Number")

# Input field for phone number
cpf_number = st.text_input("Enter a CPF number:")

# Button to trigger formatting and copy functionality
if st.button("Generate CPF Dork"):
  # Call the formatting function and display the result
  formatted_cpf = format_cpf_number(cpf_number)
  if formatted_cpf:
    try:
      pyperclip.copy(formatted_cpf)
      st.session_state.cpf_result = formatted_cpf
      st.success(f"CPF number Dork created: {formatted_cpf}")
    except Exception as e:
      st.error(f"Error copying to clipboard: {e}")
  else:
    st.error("Invalid CPF number format.")

# Display copy and clear buttons for CPF if result exists
if st.session_state.cpf_result:
  col1, col2 = st.columns([1, 4])
  with col1:
    if st.button("📋 Copy dork", key="copy_cpf"):
      pyperclip.copy(st.session_state.cpf_result)
      st.success("✅ Copied!")
  with col2:
    if st.button("🗑️ Clear Result", key="clear_cpf"):
      st.session_state.cpf_result = None
      st.rerun()

# Web Hosted Documents Section
st.title("📄 Web Hosted Documents")

# Input field for name
docs_name = st.text_input("Enter a name to search in documents:")

# Button to trigger formatting and copy functionality
if st.button("Generate Documents Dork"):
  # Call the formatting function and display the result
  formatted_docs = format_docs_dork(docs_name)
  if formatted_docs and docs_name.strip():
    try:
      pyperclip.copy(formatted_docs)
      st.session_state.docs_result = formatted_docs
      st.success(f"Documents Dork created: {formatted_docs}")
    except Exception as e:
      st.error(f"Error copying to clipboard: {e}")
  else:
    st.error("Please enter a valid name.")

# Display copy and clear buttons for documents if result exists
if st.session_state.docs_result:
  col1, col2 = st.columns([1, 4])
  with col1:
    if st.button("📋 Copy dork", key="copy_docs"):
      pyperclip.copy(st.session_state.docs_result)
      st.success("✅ Copied!")
  with col2:
    if st.button("🗑️ Clear Result", key="clear_docs"):
      st.session_state.docs_result = None
      st.rerun()

# WhatsApp Group Chats Section
st.title("💬 WhatsApp Group Chats")

# Input field for search term
whatsapp_term = st.text_input("Enter search term for WhatsApp groups:")

# Button to trigger formatting and copy functionality
if st.button("Generate WhatsApp Dork"):
  # Call the formatting function and display the result
  formatted_whatsapp = format_whatsapp_dork(whatsapp_term)
  if formatted_whatsapp and whatsapp_term.strip():
    try:
      pyperclip.copy(formatted_whatsapp)
      st.session_state.whatsapp_result = formatted_whatsapp
      st.success(f"WhatsApp Dork created: {formatted_whatsapp}")
    except Exception as e:
      st.error(f"Error copying to clipboard: {e}")
  else:
    st.error("Please enter a valid search term.")

# Display copy and clear buttons for WhatsApp if result exists
if st.session_state.whatsapp_result:
  col1, col2 = st.columns([1, 4])
  with col1:
    if st.button("📋 Copy dork", key="copy_whatsapp"):
      pyperclip.copy(st.session_state.whatsapp_result)
      st.success("✅ Copied!")
  with col2:
    if st.button("🗑️ Clear Result", key="clear_whatsapp"):
      st.session_state.whatsapp_result = None
      st.rerun()

# Telegram Group Chats Section
st.title("✈️ Telegram Group Chats")

# Input field for search term
telegram_term = st.text_input("Enter search term for Telegram groups:")

# Button to trigger formatting and copy functionality
if st.button("Generate Telegram Dork"):
  # Call the formatting function and display the result
  formatted_telegram = format_telegram_dork(telegram_term)
  if formatted_telegram and telegram_term.strip():
    try:
      pyperclip.copy(formatted_telegram)
      st.session_state.telegram_result = formatted_telegram
      st.success(f"Telegram Dork created: {formatted_telegram}")
    except Exception as e:
      st.error(f"Error copying to clipboard: {e}")
  else:
    st.error("Please enter a valid search term.")

# Display copy and clear buttons for Telegram if result exists
if st.session_state.telegram_result:
  col1, col2 = st.columns([1, 4])
  with col1:
    if st.button("📋 Copy dork", key="copy_telegram"):
      pyperclip.copy(st.session_state.telegram_result)
      st.success("✅ Copied!")
  with col2:
    if st.button("🗑️ Clear Result", key="clear_telegram"):
      st.session_state.telegram_result = None
      st.rerun()

# Instagram Comments Section
st.title("📸 Instagram Comments")

# Input field for username
instagram_username = st.text_input("Enter username to search on Instagram:")

# Button to trigger formatting and copy functionality
if st.button("Generate Instagram Dork"):
  # Call the formatting function and display the result
  formatted_instagram = format_instagram_dork(instagram_username)
  if formatted_instagram and instagram_username.strip():
    try:
      pyperclip.copy(formatted_instagram)
      st.session_state.instagram_result = formatted_instagram
      st.success(f"Instagram Dork created: {formatted_instagram}")
    except Exception as e:
      st.error(f"Error copying to clipboard: {e}")
  else:
    st.error("Please enter a valid username.")

# Display copy and clear buttons for Instagram if result exists
if st.session_state.instagram_result:
  col1, col2 = st.columns([1, 4])
  with col1:
    if st.button("📋 Copy dork", key="copy_instagram"):
      pyperclip.copy(st.session_state.instagram_result)
      st.success("✅ Copied!")
  with col2:
    if st.button("🗑️ Clear Result", key="clear_instagram"):
      st.session_state.instagram_result = None
      st.rerun()
