def hotelRoom():
    month = input("Въведете месец между Май и Октомври: ")
    days = int(input("Брой нощувки: "))

    studio_room_price = 0
    apartment_price = 0

    if month == "май" or month == "октомври":
        studio_room_price = 50
        apartment_price = 65
        if days > 7 and days <= 14:
            studio_room_price -= studio_room_price * 0.05
        elif days > 14:
            studio_room_price -= studio_room_price * 0.30
            apartment_price -= apartment_price * 0.10
    elif month == "юни" or month == "септември":
        studio_room_price = 75.20
        apartment_price = 68.70
        if days > 14:
            studio_room_price -= studio_room_price * 0.20
            apartment_price -= apartment_price * 0.10
    elif month == "юли" or month == "август":
        studio_room_price = 76
        apartment_price = 77
        if days > 14:
            apartment_price -= apartment_price * 0.10

    studio_sum = days * studio_room_price
    apartment_sum = days * apartment_price
    
    print("Apartment: %.2f lv." % apartment_sum)
    print("Studio: %.2f lv." % studio_sum)

hotelRoom()