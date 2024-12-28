def landscapingYard():
    meters = float(input("Въведете метрите за озеленяване: "))
    price = meters * 7.61
    discound = price * 0.18
    sum = price - discound

    print(f"Необходимата сума = {sum}лв.")
    print(f"Отстъпката = {discound}лв.")

landscapingYard()