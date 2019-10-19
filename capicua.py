num = int(input("What is your number? "))

inverse = {}
capicua = {}
test = num
test2 = num
number_of_digits = 0
number_of_digits2 = -1
verification = 0
a = 0

while (test > 0):
    test = test // 10
    number_of_digits += 1
    number_of_digits2 += 1
    
for i in range(number_of_digits):
    inverse[i] = test2 // (10**(number_of_digits2))
    test2 = test2 % (10**(number_of_digits2))
    number_of_digits2 -= 1


for x in range(number_of_digits-1, -1, -1):
    a = number_of_digits-1 - x
    capicua[a] = inverse[x]
       
for y in range(number_of_digits):
    if capicua[y] == inverse[y]:
        verification += 1
        
if verification == number_of_digits:
    result = str(num) + " is a palindrome."
else:
    result = str(num) + " is not a palindrome."