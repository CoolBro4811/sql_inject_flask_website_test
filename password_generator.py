import random
import string

def generate_password(length : int, is_let = True, is_dig = True, is_punc = True):
    # Define the characters to use in the password
    characters = string.ascii_letters*is_let + string.digits*is_dig + string.punctuation*is_punc
    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Ask the user how long they want their password to be
password_length = int(input("How long do you want your password to be? "))
temp = input("Choose of the following your password will have:\n[1]:letters, [2]:numbers, [3]:punctuation\n[A]ll, [N]one, [12]:letters and numbers, [23]:numbers and punctuation, [13]:letters and punctuation")
if "1" in temp:
    if temp == "1":
        print("Your new password is:", generate_password(password_length, is_dig=False, is_punc=False))
        exit()
    elif temp == "13":
        print("Your new password is:", generate_password(password_length, is_dig=False))
        exit()
    print("Your new password is:", generate_password(password_length, is_punc=False))
    exit()
elif "2" in temp:
    if temp == "2":
        print("Your new password is:", generate_password(password_length, is_let=False, is_punc=False))
        exit()
    print("Your new password is:", generate_password(password_length, is_let=False))
    exit()
elif temp == "3":
    print("Your new password is:", generate_password(password_length, is_let=False, is_dig=False))
    exit()
else:
    print("Not enough characters or incorrect syntax, please try again")
    exit()

print("Your new password is:", generate_password(password_length))
