# Programmers: Harry Li, Cooper Nazar
# Course:  CS151*06
# Due Date: 11/14/2024
# Lab Assignment: Lab 09
# Problem Statement: Create a program to read in all the attendees and then output the seat assignments.
# Data In: Name of chosen file
# Data Out: File containing list of names

import os

# Purpose: Make sure the file name being entered exists
# Parameters: file_name
# Return: names
def verify_file(file_name):
    try:
        with open(file_name, 'r') as file:
            names = []
            for line in file:
                stripped_line = line.strip()
                if stripped_line:
                    names.append(stripped_line)
        return names
    except FileNotFoundError:
        print(f'Error: File {file_name} not found.')
        return []

# Purpose: calculate the number of tables needed
# Parameters: names, table_size
# Return: number of tables
def calculate_tables(names, table_size):
    return (len(names) // table_size)
    
    
# Purpose: Assign each name to a seat for every table needed
# Parameters: names
# Return: assigned_seat (number of seats per table), num_tables (what table a person is assigned to)
def organize(names, num_tables, table_size):
    assigned_seat = []
    
    for i in range(num_tables):
        for j in range(table_size):
            guest_name = names[i * table_size + j]
            table_number = i + 1
            seat_number = j + 1
            assigned_seat.append(f'Table {table_number}, Seat {seat_number}, {guest_name}')
    
    return assigned_seat

# Purpose: Run the program
# Parameters: None
# Return: None
def main():
    correct_name = 0
    while correct_name != 10:
        file_name = input('Enter the name of the file with attendees names: ')
        if os.path.isfile(file_name):
            names = verify_file(file_name)
            if names:
                correct_name = 10
            else:
                print('Please enter a valid file name with attendee names.')
        else: 
            print('Please enter a valid file name with attendee names.' )
    
    # Set table size to amount of seats at each table 
    table_size = 5
    
    # Find the number of tables needed
    num_tables = calculate_tables(names, table_size)

    # Determine assigned seats and number of tables
    orgainize_seat = organize(names, num_tables, table_size)

    # Display results
    print(f'\nNumber of tables needed: {num_tables}\n')
    for seat in orgainize_seat:
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        print(seat)
        print("~~~~~~~~~~~~~~~~~~~~~~~")

# Run the program
main()
