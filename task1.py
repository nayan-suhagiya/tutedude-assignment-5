student_dict = {
    "Tanny": 45,
    "Lucais": 41,
    "Galvin": 74,
    "Elijah": 84,
    "Micheal": 61,
    "Winfred": 57,
    "Amby": 49,
    "Amerigo": 40,
    "Karney": 99,
    "Ody": 99,
    "Calvin": 84,
    "Drugi": 75,
    "Keenan": 49,
    "Reidar": 99,
    "Eric": 53,
    "Hebert": 73,
    "Gayle": 59,
    "Alon": 60,
    "Goraud": 94,
    "Sherm": 58,
}

student_name = input("Enter the student's name: ")

try:
    marks = student_dict.get(student_name)
    if marks:
        blueprint = "{0}'s marks: {1}"
        print(blueprint.format(student_name, marks))
    else:
        print("Student not found.")
except:
    print("Unable to find marks! please try later.")
