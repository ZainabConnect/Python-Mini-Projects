import random
import string

def pref():
    length= int(input("Enter the required length of the password: "))
    use_upper =input("Do you want to include uppercase letters? (y/n) : ").lower() == 'y'
    use_lower =input("Do you want to include lowercase letters? (y/n) : ").lower() == 'y'
    use_numbers =input("Do you want to include numbers? (y/n) : ").lower() == 'y'
    use_symbols =input("Do you want to include symbols? (y/n) : ").lower() == 'y'

    return length,use_upper,use_lower,use_numbers,use_symbols

def generate_pass(length,use_upper,use_lower,use_numbers,use_symbols):
    chars =""
    if use_lower:
        chars += string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    
    if not chars:
        return "error: select atleast one type of characters for your password!"
    
    password=""
    for i in range(length):
        password += random.choice(chars)
    return password

def main():
    length,use_upper,use_lower,use_numbers,use_symbols = pref()
    password= generate_pass(length,use_upper,use_lower,use_numbers,use_symbols)
    print("password is: ",password)

if __name__ == "__main__":
    main()  



