#FizzBuzz challenge in python
# 1-100 
# %3 Fizz
# %5 Buzz
# %3 & %5 FizzBuzz
# else number of loop 

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
