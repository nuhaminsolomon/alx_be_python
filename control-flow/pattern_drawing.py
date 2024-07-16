#!/usr/bin/env python3

def main():
    # Prompt the user to enter a positive integer for the size of the pattern
    size = int(input("Enter the size of the pattern: "))

    # Initialize the row counter for the while loop
    row = 0

    # Use a while loop to iterate through each row
    while row < size:
        # Use a for loop to print asterisks (*) side by side
        for _ in range(size):
            print("*", end="")
        # Print a newline character to move to the next row
        print()
        # Increment the row counter
        row += 1

if __name__ == "__main__":
    main()

