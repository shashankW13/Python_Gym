import streamlit as st
import string
from db import queries

def validate_username(username):
    if len(username) < 5:
        return False, "Username must be atleast 5 characters long"
    
    if queries.check_username(username):
        return False, "Username already exists!"

    else:
        return True, "Username is valid"
    

def validate_password(password):

    if len(password) < 8:
        return False, "Password must be atleast 8 characters long"
    
    char_counts = {
        "alphabet_count": 0,
        "digit_count": 0,
        "special_count": 0,
        "capital_count": 0,
        "lower_count": 0
    }
    
    for word in password:
        if word.isdigit():
            char_counts["digit_count"] += 1

        if word.isalpha():
            char_counts["alphabet_count"] += 1

        if word.isupper():
            char_counts["capital_count"] += 1

        if word.islower():
            char_counts["lower_count"] += 1

        if word in string.punctuation:
            char_counts["special_count"] += 1
    

    if char_counts["alphabet_count"] < 1:
        return False, "Password must contain atleast 1 alphabet"
    
    if char_counts["digit_count"] < 1:
        return False, "Password must contain atleast 1 number"

    if char_counts["capital_count"] < 1:
        return False, "Password must contain atleast 1 capital letter"

    if char_counts["lower_count"] < 1:
        return False, "Password must contain atleast 1 small letter"

    if char_counts["special_count"] < 1:
        return False, "Password must contain atleast 1 special character"

    return True, "Password is valid"
        