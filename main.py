class_names = []
class_levels = []
class_quantity = []


def load_data():
    with open("bookings.txt", "r") as file:
        for line in file:
            line = line.strip().split(",")

            class_names.append(line[0])
            class_levels.append(line[1])
            class_quantity.append(int(line[2]))


def save_data(arr0, arr1, arr2):
    with open("bookings.txt", "w") as file:
        for i in range(len(arr0)):
            file.write(f"{arr0[i]},{arr1[i]},{arr2[i]}\n")


def show_languages(arr0, arr1):
    used_languages = []

    for i in range(len(arr0)):
        if arr0[i] not in used_languages:
            used_languages.append(arr0[i])

            print(f"{arr0[i]} Levels:", end=" ")
            for j in range(len(arr0)):
                if arr0[j] == arr0[i]:
                    print(arr1[j], end=" ")
            print()


def show_levels(arr0, arr1):
    language = input("Choose the subject: ")

    found = False

    print("=" * 15)
    print(f"Levels of {language}:")
    print("-" * 15)

    for i in range(len(arr0)):
        if arr0[i].lower() == language.lower():
            print(arr1[i])
            found = True

    print("=" * 15)

    if found == False:
        print("Unknown language")


def show_availability(arr0, arr1, arr2):
    language = input("Enter language: ")

    found = False
    available = False

    for i in range(len(arr0)):
        if arr0[i].lower() == language.lower():
            found = True

            if arr2[i] < 20:
                if available == False:
                    print("Currently there is space in:")
                print(f"{arr0[i]} Level {arr1[i]}")
                available = True

    if found == False:
        print("There are currently no classes in this language.")
    elif available == False:
        print("There is no availability in this language.")


def book_place(arr0, arr1, arr2):
    student_name = input("Enter student name: ")
    student_id = input("Enter student id: ")
    language = input("Enter language: ")
    level = input("Enter level: ")

    for i in range(len(arr0)):
        if arr0[i].lower() == language.lower() and arr1[i] == level:
            if arr2[i] < 20:
                arr2[i] = arr2[i] + 1
                save_data(arr0, arr1, arr2)

                file_name = f"{arr0[i]}_{arr1[i]}_{student_id}.txt"

                with open(file_name, "w") as file:
                    file.write("Booking Invoice\n")
                    file.write(f"Student Name: {student_name}\n")
                    file.write(f"Student ID: {student_id}\n")
                    file.write(f"Language: {arr0[i]}\n")
                    file.write(f"Level: {arr1[i]}\n")
                    file.write("Amount Owed: 200 Euros\n")

                print("Booking successful.")
                print(f"Invoice file created: {file_name}")
                return
            else:
                print("There is no class available.")
                return

    print("There is no class available.")


def show_menu(arr0, arr1, arr2):
    while True:
        print()
        print("1. Show languages")
        print("2. Show levels")
        print("3. Show Availability")
        print("4. Book a place")
        print("5. X")
        print("6. X")
        print("7. Exit")

        choice = input("Choose option from 1 to 7: ")

        try:
            choice = int(choice)
        except ValueError:
            print("Error")
            continue

        if choice == 1:
            show_languages(arr0, arr1)

        elif choice == 2:
            show_levels(arr0, arr1)

        elif choice == 3:
            show_availability(arr0, arr1, arr2)

        elif choice == 4:
            book_place(arr0, arr1, arr2)

        elif choice == 7:
            save_data(arr0, arr1, arr2)
            print("Data saved. Goodbye.")
            break

        else:
            print("Option not added yet.")


def main():
    load_data()
    show_menu(class_names, class_levels, class_quantity)


main()
