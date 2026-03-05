"""
Demonstrācijas skripts.

Parāda, kā darbojas funkcijas no utils.py un validators.py.
Demonstrē gan veiksmīgus, gan kļūdainus gadījumus.
"""

from utils import capitalize, clamp, is_prime, average, factorial
from validators import is_email, is_strong_password, is_valid_date


def demo_utils():
    """Demonstrē utils moduļa funkcijas."""
    print("=== Utils demonstrācija ===")

    try:
        result = capitalize("hello")
        print(f"capitalize('hello') → {result}")
    except Exception as e:
        print(f"capitalize('hello') → {type(e).__name__}: {e}")

    try:
        result = clamp(15, 0, 10)
        print(f"clamp(15, 0, 10) → {result}")
    except Exception as e:
        print(f"clamp(15, 0, 10) → {type(e).__name__}: {e}")

    try:
        result = is_prime(17)
        print(f"is_prime(17) → {result}")
    except Exception as e:
        print(f"is_prime(17) → {type(e).__name__}: {e}")

    try:
        result = average([10, 20, 30])
        print(f"average([10, 20, 30]) → {result}")
    except Exception as e:
        print(f"average([10, 20, 30]) → {type(e).__name__}: {e}")

    try:
        result = factorial(-1)
        print(f"factorial(-1) → {result}")
    except Exception as e:
        print(f"factorial(-1) → {type(e).__name__}: {e}")

    print()


def demo_validators():
    """Demonstrē validators moduļa funkcijas."""
    print("=== Validators demonstrācija ===")

    try:
        result = is_email("test@test.lv")
        print(f"is_email('test@test.lv') → {result}")
    except Exception as e:
        print(f"is_email('test@test.lv') → {type(e).__name__}: {e}")

    try:
        result = is_strong_password("abc")
        print(f"is_strong_password('abc') → {result}")
    except Exception as e:
        print(f"is_strong_password('abc') → {type(e).__name__}: {e}")

    try:
        result = is_valid_date("2025-13-01")
        print(f"is_valid_date('2025-13-01') → {result}")
    except Exception as e:
        print(f"is_valid_date('2025-13-01') → {type(e).__name__}: {e}")


if __name__ == "__main__":
    demo_utils()
    demo_validators()