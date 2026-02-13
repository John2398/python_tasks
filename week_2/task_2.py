for a in range(100):
    if a % 3:
        print("Fizz")
    elif a % 5:
        print("Buzz")
    elif (a % 3) & (a % 5):
        print("FizzBuzz")
    else:
        print("Not a multiple")