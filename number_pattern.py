def number_pattern(n):
    """
    Generates a number pattern from 1 to n.

    Args:
        n (int): A positive integer

    Returns:
        str: A string of numbers from 1 to n separated by spaces
    """
    
    if not isinstance(n, int):
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."

    result = []
    for i in range(1, n+1):
        result.append(str(i))

    return " ".join(result)

print(number_pattern(5))
