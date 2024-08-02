def calculate_mode(numbers):
    if len(numbers) == 0:
        raise ValueError("The list is empty")

    frequency_dict = {}
    for number in numbers:
        if number in frequency_dict:
            frequency_dict[number] += 1
        else:
            frequency_dict[number] = 1

    max_count = max(frequency_dict.values())
    modes = [num for num, freq in frequency_dict.items() if freq == max_count]

    if len(modes) == len(numbers):
        # If every number appears only once, there is no mode
        return None

    return modes


# Example usage:
numbers = [1, 2, 2, 3, 4, 4, 4, 5]
mode = calculate_mode(numbers)
print("Mode:", mode)
