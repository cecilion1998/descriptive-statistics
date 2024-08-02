def calculate_mean(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


# Example usage:
numbers = [1, 2, 3, 4, 5]
mean = calculate_mean(numbers)
print("Mean:", mean)
