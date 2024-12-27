def skiVacation():
    days = int(input("Enter the number of days: "))
    type_room = input("Enter room type: ")
    rating = input("Enter the rating of room type: ")

    sleep_night = days - 1
    price = 0

    if type_room == "room for one person":
        price = sleep_night * 18
    elif type_room == "apartment":
        price = sleep_night * 25
        if days < 10:
            price -= price * 0.30
        elif days >= 10 and days <= 15:
            price -= price * 0.35
        else:
            price -= price * 0.50
    elif type_room == "president apartment":
        price = sleep_night * 35
        if days < 10:
            price -= price * 0.10
        elif days >= 10 and days <= 15:
            price -= price * 0.15
        else:
            price -= price * 0.20

    if rating == "positive":
        price += price * 0.25
    elif rating == "negative":
        price -= price * 0.10

    print("The price is %.2f" % price)

skiVacation()