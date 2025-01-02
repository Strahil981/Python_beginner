def oscars():
    actor_name = input("Enter actor name: ")
    actors_point = float(input("Enter actors point in academy: "))
    evaluative = int(input("Enter evaluative: "))
    
    for i in range (0, evaluative):
        current_evaluative_name = input("Enter evaluative name: ")
        current_evaluative_point = float(input("Enter evaluative point: "))

        actors_point += ((len(current_evaluative_name) * current_evaluative_point) / 2)

        if actors_point >= 1250.5:
            print(f"Congratulations, {actor_name} got a nominee for leading role with {actors_point:.2f}!")
            break

    if actors_point < 1250.5:
        need_point = 1250.5 - actors_point
        print(f"Sorry, {actor_name} you need {need_point:.2f} more!")

oscars()