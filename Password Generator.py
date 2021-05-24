import random

letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+', '[', ']', '}', '{', '|']

password_list = []
letter_range = random.randint(1, 10)
symbol_range = random.randint(1, 10)
number_range = random.randint(1, 10)
for char in range(1, letter_range + 1):
    password_list.append(random.choice(letters))
for char in range(1, symbol_range + 1):
       password_list.append(random.choice(symbols)) 
for char in range(1, number_range + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
password = ''.join(password_list)
print(password)