# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

Tasks
1. Make sure the file name being entered exists
2. Add names from the files to the list
3. Assign the names into groups of five
4. Display list

Purpose: Make sure the file name being entered exists  
Name: verify_file  
Parameters:   
Return: file name  
Algorithm:   
1. Prompt the user to input the name of the file they want to read the names from
2. While the file name entered is not a real file name:
   1. Output an error message
   2. Prompt the user to input the file name again

Purpose: Read names from the file and add them to a list  
Name: add_to_list  
Parameters: file name  
Return:   
Algorithm:   
1. Create an empty list
2. Open the file indicated by the file name with the intent to read
3. Read each line from the file into the list
4. Close the file

Purpose: Assign the names into groups of five  
Name: organize  
Parameters: list  
Return:   
Algorithm:
1. For each name in the list:
   1. Add the name to a different list than the main list
   2. If the length of the previous list is five:
      1. Create a new empty list and add the next name to the new list
   3. 

Purpose: Display the final list  
Name: display_list  
Parameters: lists  
Return:   
Algorithm:
1. 

Purpose: Run the program  
Name: main  
Parameters:   
Return:   
Algorithm:
1. Output the purpose of the program
2. Import os
3. 