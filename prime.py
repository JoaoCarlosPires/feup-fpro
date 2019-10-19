n = int(input("What is your number? "))

if (n % 2 == 0) or (n % 3 == 0) or (n <= 1) or (n % 5 == 0 and n > 5):
    result = False
else:
    result = True    
    