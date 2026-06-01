import random

letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S',
'T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
'p','q','r','s','t','u','v','w','x','y','z']

numbers=['0','1','2','3','4','5','6','7','8','9']

symbols=['@','#','$','^','&','*','!','/','?']

n_letters=int(input("how many letters you want in your password?\n"))
n_numbers=int(input("how many numbers you want in your password?\n"))
n_symbols=int(input("how many symbols you want in your password?\n"))

password=""

for i in range(1,n_letters+1):
    char = random.choice(letters)
    password+=char
for i in range(1,n_numbers+1):
    char = random.choice(numbers)
    password+=char
for i in range(1,n_symbols+1):
    char = random.choice(symbols)
    password+=char
    
password_list=list(password)
random.shuffle(password_list)
password=""
for char in password_list:
    password+=char
    
print("Generated Password:",password)
