number = int(input("Enter a positive integer: "))
digits = 0
while number > 0:
    number //= 10
    digits += 1
print("The number has", digits, "digits.")