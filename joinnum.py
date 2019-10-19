n1 = int(input("What is your first number? "))
n2 = int(input("What is your second number? "))

test = n2
number_of_digits = 0
while (test > 0):
    test = test // 10
    number_of_digits += 1

result = (n1 * (10**number_of_digits)) + n2