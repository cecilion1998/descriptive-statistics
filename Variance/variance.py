def calculate_mean(numbers):
    return sum(numbers) / len(numbers)


def calculate_variance(numbers):
    if len(numbers) == 0:
        raise ValueError("The list is empty")

    mean = calculate_mean(numbers)
    squared_differences = [(x - mean) ** 2 for x in numbers]
    variance = sum(squared_differences) / len(numbers)

    return variance


# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 10]
variance = calculate_variance(numbers)
print("Variance:", variance)
