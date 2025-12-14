first_name = input("Please enter your first name:\n")
middle_name = input("Please enter your middle name:\n")
last_name = input("Please enter your last name:\n")

initial_first = first_name[0].upper()
initial_middle = middle_name[0].upper()
initial_last = last_name[0].upper()
initials = f"{initial_first}.{initial_middle}.{initial_last}"

print(f"Hi,your initials are {initials}")
