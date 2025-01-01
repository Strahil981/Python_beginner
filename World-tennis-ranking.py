import math

def worldTennisRanking():
    turnirnQuantity = int(input("Enter quantity turnirs: "))
    startPoint = int(input("Enter start point: "))
    bonus_point = 0
    winner_turnirs = 0
    average_point = 0
    percent = 0

    for i in range(0, turnirnQuantity):
        current_turnir = input("Enter SF or F or W: ")

        if current_turnir == "F":
            bonus_point += 1200
            startPoint += 1200
        elif current_turnir == "W":
            bonus_point += 2000
            startPoint += 2000
            winner_turnirs += 1
        elif current_turnir == "SF":
            bonus_point += 720
            startPoint += 720

    average_point = bonus_point / turnirnQuantity
    percent = (winner_turnirs / turnirnQuantity) * 100

    print(f"Final points: {startPoint}")
    print(f"Average points: {math.floor(average_point)}")
    print("{:.2f}%".format(percent))

worldTennisRanking()