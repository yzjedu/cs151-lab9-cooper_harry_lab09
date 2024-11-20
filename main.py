# Programmers: Harry Li, Cooper Nazar
# Course:  CS151*06
# Due Date: 11/14/2024
# Lab Assignment: Lab 09
# Problem Statement: Create a program to read in all the attendees and then output the seat assignments.
# Data In: Name of chosen file
# Data Out: File containing list of names

# Purpose: Make sure the file name being entered exists
# Parameters: file_name
# Return: names
def verify_file(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file_name:
                name = line.strip()
        return names
    except FileNotFoundError:
        print(f'Error: File {file_name} not found.')
        return []

# Purpose: Assign each name to a seat for every table needed
# Parameters: names
# Return: assigned_seat (number of seats per table), num_tables (what table a person is assigned to)
def organize(names):
    table_size = 5
    num_tables = len(names) // table_size
    assigned_seat = []

    for i in range(num_tables):
        for j in range(table_size):
            guest_name = names[i * table_size + j]
            table_number = i + 1
            seat_number = j + 1
            assigned_seat.append(f'Table {table_number}, Seat {seat_number}, {guest_name}')
    
    return assigned_seat, num_tables

# Purpose: Run the program
# Parameters: None
# Return: None
def main():
    correct_name = 0
    while correct_name != 10:
        file_name = input('Enter the name of the file with attendees names: ')
        names = verify_file(file_name)
        if names:
            correct_name = 10
        else:
            print('Please enter a valid file name with attendee names.')

    # Determine assigned seats and number of tables
    assigned_seat, num_tables = organize(names)

    # Display results
    print(f'\nNumber of tables needed: {num_tables}\n')
    for assignment in assigned_seat:
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        print(assignment)
        print("~~~~~~~~~~~~~~~~~~~~~~~")

# Run the program
main()
