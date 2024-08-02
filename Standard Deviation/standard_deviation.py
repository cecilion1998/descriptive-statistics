import math


def calculate_mean(numbers):
    return sum(numbers) / len(numbers)


def calculate_standard_deviation(numbers):
    if len(numbers) == 0:
        raise ValueError("The list is empty")

    mean = calculate_mean(numbers)
    squared_differences = [(x - mean) ** 2 for x in numbers]
    variance = sum(squared_differences) / len(numbers)
    standard_deviation = math.sqrt(variance)

    return standard_deviation


# Example usage:
numbers = [1, 2, 3, 4, 5]
std_dev = calculate_standard_deviation(numbers)
print("Standard Deviation:", std_dev)
