def calculate_range(numbers):
    if len(numbers) == 0:
        raise ValueError("The list is empty")

    min_value = min(numbers)
    max_value = max(numbers)
    range_value = max_value - min_value

    return range_value


# Example usage:
numbers = [1, 2, 3, 4, 5]
range_value = calculate_range(numbers)
print("Range:", range_value)
