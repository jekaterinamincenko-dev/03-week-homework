"""
Spēles loģikas modulis.

Šis modulis satur tikai tīru loģiku.
Tajā NAV print() vai input().
"""

import random


def generate_secret(low=1, high=100):
    """
    Ģenerē nejaušu slepeno skaitli dotajā diapazonā.

    :param low: Mazākā iespējamā vērtība
    :param high: Lielākā iespējamā vērtība
    :return: Nejaušs vesels skaitlis
    """
    return random.randint(low, high)


def check_guess(guess, secret):
    """
    Salīdzina minējumu ar slepeno skaitli.

    :param guess: Lietotāja minējums
    :param secret: Slepenais skaitlis
    :return: "correct", "too_high" vai "too_low"
    """
    if guess == secret:
        return "correct"
    elif guess > secret:
        return "too_high"
    else:
        return "too_low"


def is_game_over(attempts, max_attempts=10):
    """
    Pārbauda, vai spēle ir beigusies pēc mēģinājumu skaita.

    :param attempts: Pašreizējais mēģinājumu skaits
    :param max_attempts: Maksimālais atļautais mēģinājumu skaits
    :return: True, ja spēle beigusies, pretējā gadījumā False
    """
    return attempts >= max_attempts


if __name__ == "__main__":
    # Vienkārši testi
    secret = generate_secret()
    print("Testa slepenais skaitlis:", secret)
    print("Minējums 50:", check_guess(50, secret))
    print("Vai spēle beigusies (10)?", is_game_over(10))