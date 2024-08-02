def calculate_median(numbers):
    if len(numbers) == 0:
        raise ValueError("The list is empty")

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2

    if n % 2 == 0:
        # If even, average the two middle numbers
        median = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        # If odd, take the middle number
        median = sorted_numbers[mid]

    return median


# Example usage:
numbers = [1, 2, 3, 4, 5]
median = calculate_median(numbers)
print("Median:", median)
