temperatures = [30, 22, 35, 19, 40]
mean = sum(temperatures)/ len(temperatures)
for temparature in temperatures:
    if temparature > mean:
        print(temparature)
    else:
        continue