def trakkingMania():
    number_groups = int(input("Enter number of group: "))
    musala = 0
    monblan = 0
    kilimandjaro = 0
    k2 = 0
    everest = 0
    all_people = 0

    for i in range (0, number_groups):
        current_group_people = int(input("Enter current people group: "))

        if current_group_people <= 5:
            musala += current_group_people
        elif current_group_people >= 6 and current_group_people <= 12:
            monblan += current_group_people
        elif current_group_people >= 13 and current_group_people <= 25:
            kilimandjaro += current_group_people
        elif current_group_people >= 26 and current_group_people <= 40:
            k2 += current_group_people
        elif current_group_people >= 41:
            everest += current_group_people
            
        all_people += current_group_people

    musala = musala / all_people * 100
    monblan = monblan / all_people * 100
    kilimandjaro = kilimandjaro / all_people * 100
    k2 = k2 / all_people * 100
    everest = everest / all_people * 100

    print(f"{musala:.2f}%")
    print(f"{monblan:.2f}%")
    print(f"{kilimandjaro:.2f}%")
    print(f"{k2:.2f}%")
    print(f"{everest:.2f}%")

trakkingMania()