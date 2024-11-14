def verify_file(file_name):
    try:
        with open(file_name, 'r') as file:
            names = [line.strip() for line in file]
        return names
    except FileNotFoundError:
        print(f'Error: File {file_name} not found.')
        return []

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
