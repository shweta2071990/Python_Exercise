# Import the random module to generate random numbers
import random

# Create a list of 100 random numbers between 0 and 1000
random_numbers = [random.randint(0, 1000) for _ in range(100)]

# Print the original list
print("Original list:", random_numbers)

# Sort the list from min to max without using the sort() method
# Using bubble sort algorithm
for i in range(len(random_numbers)):
    for j in range(0, len(random_numbers) - i - 1):
        if random_numbers[j] > random_numbers[j + 1]:
            # Swap the numbers if they are in the wrong order
            random_numbers[j], random_numbers[j + 1] = random_numbers[j + 1], random_numbers[j]

# Print the sorted list
print("Sorted list:", random_numbers)

# Separate the even and odd numbers into two lists
even_numbers = [num for num in random_numbers if num % 2 == 0]
odd_numbers = [num for num in random_numbers if num % 2 != 0]

# Calculate the average for even numbers
even_average = sum(even_numbers) / len(even_numbers) if even_numbers else 0

# Calculate the average for odd numbers
odd_average = sum(odd_numbers) / len(odd_numbers) if odd_numbers else 0

# Print the calculated averages
print("Average of even numbers:", even_average)
print("Average of odd numbers:", odd_average)