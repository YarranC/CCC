# Speed fines are not fine!

limit = int(input("Enter the speed limit: "))
speed = int(input("Enter the recorded speed of the car: "))

if speed <= limit:
    print("Congratulations, you are within the speed limit")
else:
    print("You are speeding and your fine is $ ", end='')
    diff = speed - limit
    if diff >= 1 and diff <= 20:
        print(100)
    elif diff >= 21 and diff <= 30:
        print(270)
    else:
        print(500)
