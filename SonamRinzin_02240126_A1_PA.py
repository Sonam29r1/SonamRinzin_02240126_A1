
def is_prime(n):
    
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, n):  # Check all numbers from 2 to n-1
        if n % i == 0:  # If n is divisible by i, it's not prime
            return False
    return True  # If no divisors are found, n is prime

def prime_sum_calculator():
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))

    prime_sum = 0

    for n in range(start, end + 1):
        if is_prime(n):  # Check if the number is prime
            prime_sum += n  # Add the prime number to the sum

    # Print the result
    print("Sum of prime numbers between",start, "and" ,end, "is: ", prime_sum)

def length_unit_converter():
    
    value = float(input("Enter the length value: "))
    direction = input("Enter 'M' for meters to feet or 'F' for feet to meters: ").upper()

    if direction == 'M':
        converted_value = value * 3.28084  # Convert meters to feet
        print(f"{value} meters = {round(converted_value, 2)} feet")
    elif direction == 'F':
        converted_value = value / 3.28084  # Convert feet to meters
        print(f"{value} feet = {round(converted_value, 2)} meters")
    else:
        print("Invalid direction. Please enter 'M' or 'F'.")

def consonant_counter():
    
    text = input("Enter a string: ")
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0

    # Loop through each character in the string
    for char in text:
        if char in consonants:  # Check if the character is a consonant
            count += 1

    print(f"Number of consonants: {count}")

def min_max_finder():
    numbers = []
    count = int(input("How many numbers do you want to enter? "))

    for i in range(count):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    smallest = min(numbers)
    largest = max(numbers)

    print(f"Smallest: {smallest}, Largest: {largest}")

def palindrome_checker():
    text = input("Enter a string: ")
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())  # Remove spaces and punctuation, convert to lowercase
    is_palindrome = cleaned_text == cleaned_text[::-1]  # Check if the string is the same when reversed

    print(f"Is '{text}' a palindrome? {is_palindrome}")

def word_counter():
    words_to_count = ["the", "was", "and"]
    file_path = input("Enter the path to the text file: ")

    try:
        with open(file_path, 'r') as file:
            text = file.read().lower()  # Read the file and convert to lowercase
            word_counts = {word: text.split().count(word) for word in words_to_count}  # Count occurrences of each word

            for word, count in word_counts.items():
                print(f"'{word}' appears {count} times.")
    except FileNotFoundError:
        print("File not found. Please check the file path.")

# Main Program

def main():
    """
    Main function to run the program.
    """
    while True:
        print("\nSelect a function (1-6):")
        print("1. Calculate the sum of prime numbers")
        print("2. Convert length units")
        print("3. Count consonants in string")
        print("4. Find min and max numbers")
        print("5. Check for palindrome")
        print("6. Word Counter")
        print("7. Exit program")

        choice = input("Enter your choice: ")

        if choice == '1':
            prime_sum_calculator()
        elif choice == '2':
            length_unit_converter()
        elif choice == '3':
            consonant_counter()
        elif choice == '4':
            min_max_finder()
        elif choice == '5':
            palindrome_checker()
        elif choice == '6':
            word_counter()
        elif choice == '7':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

        if choice != '7':
            again = input("Would you like to try another function? (y/n): ").lower()
            if again != 'y':
                print("Exiting program. Goodbye!")
                break

# Run the main program
if __name__ == "__main__":
    main()