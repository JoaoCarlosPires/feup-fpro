# first situation

principal_amount1 = 1000
interest_rate1 = 1
frequency1 = 2
years1 = 2

final_amount1 = principal_amount1 * ((1 + (interest_rate1 / frequency1))**(frequency1 * years1))
print(final_amount1)

# second situation

principal_amount2 = 650
interest_rate2 = -0.05
frequency2 = 1
years2 = 2

final_amount2 = principal_amount2 * ((1 + (interest_rate2 / frequency2))**(frequency2 * years2))
print("\n" + final_amount2)

# third situation

principal_amount3 = float(input("What is your principal amount? "))
interest_rate3 = float(input("What is your interest rate? ")) 
frequency3 = float(input("What is your frequency? "))
years3 = 2

final_amount3 = principal_amount3 * ((1 + (interest_rate3 / frequency3))**(frequency3 * years3))
print("\n" + final_amount3)