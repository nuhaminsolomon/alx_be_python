import datetime

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.datetime.now()
    # Format the current date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    # Print the formatted current date and time
    print(f"Current date and time: {formatted_current_date}")
    return current_date

def calculate_future_date(days):
    # Get the current date
    current_date = display_current_datetime()
    # Calculate the future date by adding the specified number of days
    future_date = current_date + datetime.timedelta(days=days)
    # Format the future date as "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    # Print the formatted future date
    print(f"Future date: {formatted_future_date}")
    return future_date

if __name__ == "__main__":
    # Display the current date and time
    display_current_datetime()
    # Prompt the user to enter the number of days to add
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    # Calculate and display the future date
    calculate_future_date(days_to_add)

