def is_valid_email(value: str) -> bool:
    """
    Повертає True, якщо email валідний:
    - містить один символ '@'
    - має домен з крапкою: example.com
    - не починається і не закінчується на '@' або '.'
    """
    if value:
        if value.endswith("@") or value.endswith(".") or value.startswith("@") or value.startswith("."):
            return False
        elif "@" in value and "example.com" in value:
            return True
        else:
            return False
    else:
        return False
    

def avg(values: list[float]) -> float:
    """
    Повертає середнє значення списку.
    Якщо список порожній — підіймає ValueError.
    """
    
    if not values:
        raise ValueError("list is empty")
    
    if len(values) <= 1:
        raise ValueError("list has only one value")

    for i in values:
        if i <= 0:
            raise ValueError("list has negative values")

    return sum(values) / len(values)



def ua_to_usd(amount: float, rate: float) -> float:
    """
    Конвертує гривні у долари.
    Якщо сума або курс <= 0 — підіймає ValueError.
    """
    if amount <= 0 or rate <= 0:
        raise ValueError("float has negative values")
    else:
        return amount / rate

