def petStore():
    dog_food = int(input("Въведете броя храна за кучета: "))
    cat_food = int(input("Въведете броя храна за котки: "))

    dog_food_price = dog_food * 2.50
    cat_food_price = cat_food * 4

    sum = dog_food_price + cat_food_price

    print(f"Необходимата цена е: {sum} лв.")

petStore()