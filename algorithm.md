# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

Tasks
1. Make sure the file name being entered exists
2. Add names from the files to the list
3. Assign the names into groups of five
4. Display list

Purpose: Make sure the file name being entered exists  
Name: verify_file  
Parameters: file_name
Return: names- names on the list, [] - empty list
Algorithm:   
1. Prompt the user to input the name of the file they want to read the names from
2. While the file name entered is not a real file name:
   1. Output an error message
   2. Prompt the user to input the file name again

Purpose: to assign each name to a seat for every table needed
Name: organize  
Parameters: names  
Return: assigned_seat - seat number for the table , num_tables - what table your assigned to
Algorithm:
1. determine how many tables are needed
2. for every table needed
   1. assign 5 names to specific seats at the table 

Purpose: Run the program  
Name: main  
Parameters:   
Return:   
Algorithm:
1. create a sentinel
2. prompt the user to input a valid file name
3. when the file does not exist
   1. prompt the user to input a valid file
4. output the assigned seat, name, and table number
