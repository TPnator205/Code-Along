import stdrandom
import random


capital_letters = [chr(i) for i in range(65, 65 + 26)]
lowercase_letters = [chr(i) for i in range(97, 97 + 26)]
numbers = [chr(i) for i in range(48, 58)]
special_char = ["!","@","#","$","%","^","&","*","-","_","+","=","<",">",".","?"]

def get_input():
    action = input("'create' or 'check' password: ")
    return action

def is_upcase_letter(char):
    if char in capital_letters:
        return True
    else:
        return False

def is_lowcase_letter(char):
    if char in lowercase_letters:
        return True
    else:
        return False

def is_allowed_spec_char(char):
    if char in special_char:
        return True
    else:
        return False

def password_check(password: str):
    criteria = [False, False, False, False, False] #[length >= 8, special char, number, lowcase, upcase letter]

    if len(password) >= 8:
        criteria[0] = True

    for i in range(len(password)):
        if all(criteria) == True:
            break

        if is_allowed_spec_char(password[i]):
            criteria[1] = True
        elif password[i].isdigit():
            criteria[2] = True
        elif is_lowcase_letter(password[i]):
            criteria[3] = True
        elif is_upcase_letter(password[i]):
            criteria[4] = True
        else:
            print("Invalid character: Only letters(uppercase and lowercase), digits(0-9), and special characters(!@#$%^&*-_+=<>.?) are allowed")

    if all(criteria):
        return True
    else:
        return False

def password_create():
    password = ''
    while password_check(password) == False:
        password = ''
        password_len = random.randint(8, 20)
        all_chars = capital_letters+ lowercase_letters+ numbers+ special_char
        for i in range(password_len):
            password += all_chars[random.randint(0, len(all_chars)-1)]

    print(password)


def main():
    action = get_input()
    if action == 'check':
        password_to_check = input("Enter password to check: ")
        
        if password_check(password_to_check):
            print("Valid password")
        else:
            print("Invalid password\nPassword must:\n   be 8 characters or longer\n   have at least one uppercase letter and one lowercase letter\n   have at least one digit\n   have at least one special character(!@#$%^&*-_+=<>.?)")


    elif action == 'create':
        password_create()

    else:
        print("Invalid Action")

if __name__ == "__main__":
    main()