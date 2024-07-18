import string
import random

lowercase_alphabets = list(string.ascii_lowercase)
uppercase_alphabets = list(string.ascii_uppercase)
symbol = list(r'\/:*?"<>|')

def password_generator(n, m,):
    random_letters = []
    for _ in range(n):
        upper_letters = random.choice(uppercase_alphabets)
        lower_letters = random.choice(lowercase_alphabets)
        random_letters.append(upper_letters)
        random_letters.append(lower_letters)
    for _ in range(m):
        symbols = random.choice(symbol)
        random_letters.append(symbols)

    random.shuffle(random_letters)
    password = "".join(random_letters)
    return password

#put the parameters m=number of letters and n is number of symbols
n = int(input('number of letters you want: \n'))
m = int(input('number of symbols you want: \n'))

password = password_generator(n,m)
print(f"Your password is {password}")