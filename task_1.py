grade = float(input("Enter your university grade: "))
if 3.49 < grade <= 4.0:
    print("First Class Honours")
elif 2.99 < grade <= 3.49:
    print("Second Class Upper")
elif 1.99 < grade <= 2.99:
    print("Second Class Lower")
elif 0.99 < grade <= 1.99:
    print("Third Class")
else:
    print("No pass")