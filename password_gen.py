# collect user preferences
# length
# should contain uppercase
# should contain special character
# should contain digits

# get all available characters
# randomly pick characters upto length
# ensure we have at least one of each character type 
# ensure length is valid

""""imports random and string modules to use their functionality"""
import random
import string

""""main function"""
def password_gen():
    length = int(input("enter the desired password length: ").strip().lower())
    include_uppercase = input("include uppercase letters? (yes/no): ").strip().lower()
    include_special = input("include special characters? (yes/no): ").strip().lower()
    include_digits = input("include digits? (yes/no): ").strip().lower()        

    if length < 4:
        print("password length must be at least 4 characters")
        return
    
    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase == "yes" else ""
    special = string.punctuation if include_special == "yes" else ""
    digits = string.digits if include_digits == "yes" else ""
    all_characters = lower + uppercase + special + digits

    required_characters = []
    if include_uppercase == "yes":
        required_characters.append(random.choice(uppercase))
    if include_special == "yes":
        required_characters.append(random.choice(special))
    if include_digits == "yes":
        required_characters.append(random.choice(digits))

    remaining_length = length - len(required_characters)        
    password = required_characters

    for _ in range(remaining_length):
        character = random.choice(all_characters) 
        password.append(character)

    random.shuffle(password)
    str_password = "".join(password)
    return str_password

password = password_gen()
print(password) 