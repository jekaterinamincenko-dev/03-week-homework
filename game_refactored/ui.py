"""
Lietotāja saskarnes modulis.

Atbild par ievadi un izvadi.
Nesatur spēles loģiku.
"""

from validators import is_valid_number


def get_player_guess():
    """
    Pieprasa spēlētāja minējumu un validē ievadi.

    :return: Vesels skaitlis vai None, ja ievade nav derīga
    """
    user_input = input("Ievadi skaitli (1-100): ")

    if not is_valid_number(user_input):
        print("Nederīga ievade! Lūdzu ievadi veselu skaitli.")
        return None

    return int(user_input)


def show_hint(result):
    """
    Parāda padomu, balstoties uz rezultātu.

    :param result: "too_high" vai "too_low"
    """
    if result == "too_high":
        print("Par lielu!")
    elif result == "too_low":
        print("Par mazu!")


def show_game_over(secret, attempts, won):
    """
    Parāda spēles beigu ziņojumu.

    :param secret: Slepenais skaitlis
    :param attempts: Mēģinājumu skaits
    :param won: True, ja spēlētājs uzvarēja
    """
    if won:
        print(f"Uzvara! Tu uzminēji {secret} ar {attempts} mēģinājumiem!")
    else:
        print(f"Spēle beigusies! Pareizais skaitlis bija {secret}.")


def ask_play_again():
    """
    Pajautā, vai spēlēt vēlreiz.

    :return: True, ja jāspēlē vēlreiz, pretējā gadījumā False
    """
    answer = input("Vai spēlēt vēlreiz? (j/n): ").lower()
    return answer == "j"


if __name__ == "__main__":
    # UI tests
    guess = get_player_guess()
    print("Tu ievadīji:", guess)
    show_hint("too_high")
    show_game_over(42, 5, True)