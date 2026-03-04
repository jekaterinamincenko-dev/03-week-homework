# Utilītu bibliotēka
def capitalize(text):
    """Pārvērš virknes pirmo burtu lielu, pārējos mazus.
    
    Args:
        text: ievades virkne
        
    Returns:
        str: virkne ar lielu pirmo burtu
        
    Example:
        >>> capitalize("hello")
        'Hello'
        >>> capitalize("HELLO world")
        'Hello world'
    """
    if not isinstance(text, str):
        raise ValueError("Ievadei jābūt virknei")
    return text[0:1].upper() + text[1:].lower()


def truncate(text, max_len=20):
    """Apgriež virkni, ja tā pārsniedz norādīto garumu, pievienojot "...".
    
    Args:
        text: ievades virkne
        max_len: maksimālais garums (noklusēti 20)
        
    Returns:
        str: saīsinātā virkne
        
    Example:
        >>> truncate("Ļoti gara virkne šeit", 10)
        'Ļoti gar...'
        >>> truncate("īsa")
        'īsa'
    """
    if not isinstance(text, str):
        raise ValueError("Ievadei jābūt virknei")
    if len(text) <= max_len:
        return text
    return text[:max_len-3] + "..."


def count_words(text):
    """Saskaita vārdus virknē (vārdi atdalīti ar atstarpēm).
    
    Args:
        text: ievades virkne
        
    Returns:
        int: vārdu skaits
        
    Example:
        >>> count_words("Hello world!")
        2
        >>> count_words("viens divi trīs")
        3
    """
    if not isinstance(text, str):
        raise ValueError("Ievadei jābūt virknei")
    return len(text.split())


def clamp(num, low, high):
    """Ierobežo skaitli norādītajā diapazonā.
    
    Args:
        num: skaitlis, ko ierobežot
        low: minimālā robeža
        high: maksimālā robeža
        
    Returns:
        int vai float: ierobežotā vērtība
        
    Example:
        >>> clamp(15, 0, 10)
        10
        >>> clamp(-5, 0, 10)
        0
    """
    if not isinstance(num, (int, float)) or not isinstance(low, (int, float)) or not isinstance(high, (int, float)):
        raise ValueError("Visiem parametriem jābūt skaitļiem")
    if low > high:
        raise ValueError("low nevar būt lielāks par high")
    return max(low, min(num, high))


def is_prime(num):
    """Pārbauda, vai skaitlis ir pirmskaitlis.
    
    Args:
        num: pārbaudāmais skaitlis
        
    Returns:
        bool: True, ja ir pirmskaitlis
        
    Example:
        >>> is_prime(17)
        True
        >>> is_prime(4)
        False
    """
    if not isinstance(num, int) or num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def factorial(n):
    """Aprēķina faktoriāli (n!).
    
    Args:
        n: vesels skaitlis >= 0
        
    Returns:
        int: n!
        
    Raises:
        ValueError: ja n < 0
        
    Example:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    if not isinstance(n, int):
        raise ValueError("n jābūt veselim skaitlim")
    if n < 0:
        raise ValueError("Faktoriālis definēts tikai n >= 0")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def total(numbers):
    """Aprēķina skaitļu saraksta summu (izmanto for ciklu).
    
    Args:
        numbers: skaitļu saraksts
        
    Returns:
        float: summa
        
    Raises:
        ValueError: ja tukšs saraksts vai nav skaitļi
        
    Example:
        >>> total([1, 2, 3])
        6.0
    """
    if not isinstance(numbers, list):
        raise ValueError("Ievadei jābūt sarakstam")
    if not numbers:
        raise ValueError("Saraksts nevar būt tukšs")
    result = 0.0
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("Sarakstā drīkst būt tikai skaitļi")
        result += num
    return result


def average(numbers):
    """Aprēķina skaitļu saraksta vidējo aritmētisko vērtību.
    
    Args:
        numbers: skaitļu saraksts
        
    Returns:
        float: vidējā vērtība
        
    Example:
        >>> average([1, 2, 3, 4])
        2.5
    """
    return total(numbers) / len(numbers)


if __name__ == "__main__":
    # Demonstrācijas izsaukumi
    print("Virkņu funkcijas")
    print(capitalize("spring"))
    print(truncate("Today is spring", 10))
    print(count_words("Today is spring"))
    
    print("\nSkaitļu funkcijas")
    print(clamp(15, 0, 10))
    print(is_prime(17))
    print(factorial(5))
    
    print("\nSarakstu funkcijas")
    print(total([1, 2, 3, 4]))
    print(average([1, 2, 3, 4]))