import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy version, sequential
pwd = ""
for char in range(0, nr_letters):
    pwd += random.choice(letters)
for char in range(0, nr_numbers):
    pwd += random.choice(numbers)
for char in range(0, nr_symbols):
    pwd += random.choice(symbols)
print(pwd)

#Hard version, totally random order

password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

print(f"Sequential mode {password_list}")
random.shuffle(password_list)
print(f"Random mode {password_list}")

for char in password_list:
    pwd += char
print(f"Your password is: {pwd}")

