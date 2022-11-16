import re


regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

def check_valid_email(address):
    """Returns True if e-mail is valid"""
    return bool(re.fullmatch(regex, address))