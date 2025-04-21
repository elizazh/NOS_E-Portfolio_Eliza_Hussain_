import string


def check_password_strength(password):
    special_chars = string.punctuation
    messages = []

    if len(password) < 8:
        messages.append("at least 8 characters")
    if not any(c.isupper() for c in password):
        messages.append("one uppercase letter")
    if not any(c.islower() for c in password):
        messages.append("one lowercase letter")
    if not any(c in special_chars for c in password):
        messages.append("one special character")

    if not messages:
        print("Password is strong")
    else:
        print("Password must contain " + ", ".join(messages))


# Test it
check_password_strength("Pa$$word123")
check_password_strength("password")
