def histogram():
    quantity_number = int(input("Enter number 1 - 1000: "))
    percent1 = 0
    percent1_number = 0
    percent2 = 0
    percent2_number = 0
    percent3 = 0
    percent3_number = 0
    percent4 = 0
    percent4_number = 0
    percent5 = 0
    percent5_number = 0

    for i in range (0, quantity_number):
        current_number = int(input("Enter number: "))

        if current_number < 200:
            percent1_number += 1
        elif current_number >= 200 and current_number <= 399:
            percent2_number += 1
        elif current_number >= 400 and current_number <= 599:
            percent3_number += 1
        elif current_number >= 600 and current_number <= 799:
            percent4_number += 1
        elif current_number >= 800:
            percent5_number += 1

    percent1 = (percent1_number / quantity_number) * 100
    percent2 = (percent2_number / quantity_number) * 100
    percent3 = (percent3_number / quantity_number) * 100
    percent4 = (percent4_number / quantity_number) * 100
    percent5 = (percent5_number / quantity_number) * 100

    print(f"{percent1:.2f}%")
    print(f"{percent2:.2f}%")
    print(f"{percent3:.2f}%")
    print(f"{percent4:.2f}%")
    print(f"{percent5:.2f}%")

histogram()