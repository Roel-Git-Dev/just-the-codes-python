from FunctionList import Stack_Helper
print("This simple console app checks if your braces, brackets, and parentheses are balance")
sample = input("Type the string you want to check: ")

def Is_Balance_String(given_string):
    if len(given_string) % 2 != 0:
        return False
    
    tester_list = Stack_Helper(given_string)
    if len(tester_list) > 0:
        return False
    else:
        return True
print("Balance Checker")
print(f"{sample} is balance? {Is_Balance_String(sample)}")



