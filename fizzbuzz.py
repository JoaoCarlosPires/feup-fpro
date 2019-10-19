n = int(input("What is your number? "))
result = ""

for i in range(n+1):
    if i == 0:
        result += str(i) + " "
    if i % 3 == 0 and i % 5 != 0:
        result += "Fizz " 
    elif i % 5 == 0 and i % 3 != 0:
        result += "Buzz "
    elif i % 5 == 0 and i % 3 == 0:
        continue
    else:
        result += str(i) + " "