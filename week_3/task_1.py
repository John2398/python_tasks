sales = [120, 450, 800, 50, 900, 300]
low = []
medium = []
high = []
for item in sales:
    if item <= 300:
        low.append(sales)
    elif 300 > item <= 700:
        medium.append(sales)
    elif item > 700:
        high.append(sales)
    else:
        break
print("Count of Low: " + low.count(), "The sum of low is: " + sum(low))
print("Count of Medium: " + medium.count(), "The sum of medium is: " + sum(medium))
print("Count of High: " + high.count(), "The sum of high is: " + sum(high))
