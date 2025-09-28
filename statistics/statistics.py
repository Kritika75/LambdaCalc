from typing import List
import math

def mean(data: List[float]) -> float:
    """
    Calculates the arithmetic mean (average) of a list of numbers.

    Args:
        data (List[float]): A list of numbers.

    Returns:
        float: The mean of the numbers.
        
    Raises:
        ValueError: If the input list is empty.
    """
    if not data:
        raise ValueError("Input list cannot be empty")
    return sum(data) / len(data)

def std_dev(data: List[float]) -> float:
    """
    Calculates the standard deviation of a list of numbers.

    Args:
        data (List[float]): A list of numbers.

    Returns:
        float: The standard deviation of the numbers.
    """
    n = len(data)
    if n < 2:
        return 0.0
    
    mu = mean(data)
    variance = sum([(x - mu) ** 2 for x in data]) / (n - 1)
    return math.sqrt(variance)