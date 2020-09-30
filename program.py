# user input variables
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# assigns both names to full name and reverses the characters
full_name = first_name[::-1], last_name[::-1]

# outputs the reverse order of names
print(full_name[::-1])