
def is_prime(num:int):
    """_summary_

    Args:
        num (int): _description_
    """
    if num < 2:
        is_prime = False
    for i in range(2,num):
        if num%i == 0:
            is_prime = False
            break
    return is_prime

print(is_prime(8))
