def calculate_average(numbers):
    """Returns the average of a list of numbers."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def divide(a, b):
    """Returns a divided by b."""
    if b == 0:
        return 0.0
    return a / b
