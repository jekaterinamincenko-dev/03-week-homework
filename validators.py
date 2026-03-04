# Validācijas bibliotēka
"""Validācijas bibliotēka: e-pasts, telefons, vecums, parole, datums."""

import re

# E-PASTA VALIDĀCIJA
def is_email(text):
    """Pārbauda, vai teksts atbilst vienkāršam e-pasta formātam.

    Nosacījumi:
    - Satur '@'
    - Satur '.'
    - '@' nav pirmais vai pēdējais simbols
    - Punkts atrodas aiz '@'

    Args:
        text (str): ievades teksts

    Returns:
        bool: True, ja atbilst formātam; False citādi

    Example:
        >>> is_email("anna@inbox.lv")
        True
    """
    if not isinstance(text, str):
        return False

    if "@" not in text or "." not in text:
        return False

    if text.startswith("@") or text.endswith("@"):
        return False

    at_index = text.find("@")
    dot_index = text.rfind(".")

    return at_index < dot_index

# TELEFONA NUMURA VALIDĀCIJA

def is_phone_number(text):
    """Pārbauda, vai teksts atbilst Latvijas telefona formātam.

    Formāts: +371 XXXXXXXX (8 cipari pēc atstarpes)

    Args:
        text (str): ievades teksts

    Returns:
        bool: True, ja atbilst formātam; False citādi

    Example:
        >>> is_phone_number("+371 26123456")
        True
    """
    if not isinstance(text, str):
        return False

    pattern = r"^\+371 \d{8}$"
    return bool(re.match(pattern, text))

# VECUMA VALIDĀCIJA

def is_valid_age(age):
    """Pārbauda, vai vecums ir derīgs (0–150).

    Args:
        age (int): vecums

    Returns:
        bool: True, ja vecums ir vesels skaitlis diapazonā 0–150

    Example:
        >>> is_valid_age(25)
        True
    """
    if not isinstance(age, int):
        return False

    return 0 <= age <= 150

# PAROLES VALIDĀCIJA
def is_strong_password(text):
    """Pārbauda, vai parole ir pietiekami droša.

    Nosacījumi:
    - Vismaz 8 simboli
    - Satur vismaz vienu burtu
    - Satur vismaz vienu ciparu

    Args:
        text (str): parole

    Returns:
        bool: True, ja parole atbilst prasībām; False citādi

    Example:
        >>> is_strong_password("abc12345")
        True
    """
    if not isinstance(text, str):
        return False

    if len(text) < 8:
        return False

    has_letter = any(c.isalpha() for c in text)
    has_digit = any(c.isdigit() for c in text)

    return has_letter and has_digit

# DATUMA VALIDĀCIJA

def is_valid_date(text):
    """Pārbauda, vai datums ir formātā YYYY-MM-DD (pamata pārbaude).

    Nepārbauda reālu kalendāra pareizību (piem., 2023-99-99 būs False,
    bet 2023-02-31 var iziet kā True).

    Args:
        text (str): datums tekstā

    Returns:
        bool: True, ja atbilst formātam; False citādi

    Example:
        >>> is_valid_date("2024-05-20")
        True
    """
    if not isinstance(text, str):
        return False

    pattern = r"^\d{4}-\d{2}-\d{2}$"
    if not re.match(pattern, text):
        return False

    year, month, day = text.split("-")

    month = int(month)
    day = int(day)

    if not (1 <= month <= 12):
        return False

    if not (1 <= day <= 31):
        return False

    return True

# TESTI
if __name__ == "__main__":

    print("is_email")
    print(is_email("yeka@inbox.lv"))   # True
    print(is_email("yeka"))            # False
    print(is_email("yeka@"))           # False

    print("\nis_phone_number")
    print(is_phone_number("+371 26123456"))  # True
    print(is_phone_number("26123456"))       # False
    print(is_phone_number("+371 123"))       # False

    print("\nis_valid_age")
    print(is_valid_age(24))     # True
    print(is_valid_age(0))      # True (robežgadījums)
    print(is_valid_age(168))    # False

    print("\nis_strong_password")
    print(is_strong_password("abc12345"))  # True
    print(is_strong_password("abcabcab"))   # False
    print(is_strong_password("12345678"))  # False

    print("\nis_valid_date")
    print(is_valid_date("2024-05-20"))  # True
    print(is_valid_date("2024-13-01"))  # False
    print(is_valid_date("20-05-2024"))  # False

    # Import
    import validators
print(validators.is_email("yeka@inbox.lv"))