def projectPreparation():
    name = input("Въведете име на архитекта: ")
    projects = int(input("Въведете броя на проектите: "))

    time = projects * 3
    print(f"The architect {name} will need {time} hours to complete {projects} project/s.")

projectPreparation()