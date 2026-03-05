"""
Validācijas funkciju modulis.
"""


def is_valid_number(value):
    """
    Pārbauda, vai ievade ir vesels skaitlis.

    :param value: Teksta ievade
    :return: True, ja ievade ir vesels skaitlis, citādi False
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    # Testi
    print(is_valid_number("10"))   # True
    print(is_valid_number("abc"))  # False