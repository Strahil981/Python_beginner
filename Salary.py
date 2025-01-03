def salary():
    open_tabs = int(input("Enter all open tabs: "))
    salary_sum = int(input("Enter salary between 500 and 1500: "))

    for i in range (0, open_tabs):

        if salary_sum <= 0:
            print("You have lost your salary.")
            break

        current_tab = input("Enter website name: ")

        if current_tab == "Facebook":
            salary_sum -= 150
        elif current_tab == "Instagram":
            salary_sum -= 100
        elif current_tab == "Reddit":
            salary_sum -= 50

    if salary_sum > 0:
        print(salary_sum)

salary()