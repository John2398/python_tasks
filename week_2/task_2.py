for a in range(101):
    if a % 3 == 0:
        print("Fizz")
    elif a % 5 == 0:
        print("Buzz")
    elif (a % 3) == 0 & (a % 5) == 0:
        print("FizzBuzz")
    else:
        print("Not a multiple")