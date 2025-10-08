
def fact(num:int) -> int:
    """this function find the factorial of a number

    Args:
        num (int): _description_

    Returns:
        int: _description_
    """
    
    result = 1
    while num > 1:
        result = num * result
        num -= 1
    return result
print(fact(7))


