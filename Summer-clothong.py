def summerClothing():
    degree = int(input("Enter degree: "))
    part_of_day = input("Enter part of the day: ")
    outfit = ""
    shoes = ""

    if part_of_day == "Morning":
        if degree >= 10 and degree <= 18:
            outfit = "Sweatshirt"
            shoes = "Sneakers"
        elif degree > 18 and degree <= 24:
            outfit = "Shirt"
            shoes = "Moccasins"
        elif degree >= 25:
            outfit = "T-Shirt"
            shoes = "Sandals"
    elif part_of_day == "Afternoon":
        if degree >= 10 and degree <= 18:
            outfit = "Shirt"
            shoes = "Moccasins"
        elif degree > 18 and degree <= 24:
            outfit = "T-Shirt"
            shoes = "Sandals"
        elif degree >= 25:
            outfit = "Swim suit"
            shoes = "barefool"
    elif part_of_day == "Evening":
            outfit = "Shirt"
            shoes = "Moccasins"

    print(f"It's {degree} degrees, get your {outfit} and {shoes}.")

summerClothing()