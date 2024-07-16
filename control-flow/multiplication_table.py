#!/usr/bin/env python3

def main():
    # Prompt the user to enter a number for which they want to see the multiplication table
    number = int(input("Enter a number to see its multiplication table: "))

    # Use a for loop to iterate through the numbers 1 to 10
    for i in range(1, 11):
        # Calculate the product of the user's number and the current number in the loop
        product = number * i
        # Print each line of the multiplication table in the format: "X * Y = Z"
        print(f"{number} * {i} = {product}")

if __name__ == "__main__":
    main()

