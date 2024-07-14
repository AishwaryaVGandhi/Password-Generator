import random
import string

symbols = ["!","@","#","$","%","&","*","(",")","+"]
password_list = []
password = ""

print("Password Generator !!\n")

n_alphabets = int(input("How many alphabets do you want in your password : "))
for i in range(n_alphabets):
    password_list.append(random.choice(string.ascii_letters))

n_numbers = int(input("How many numbers do you want in your password : "))
for i in range(n_numbers):
    password_list.append(random.choice(string.digits))
    
n_symbols = int(input("How many symbols do you want in your password : "))
for i in range(n_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
password = "".join(password_list)

print("\nGenerated Password : ", password)
