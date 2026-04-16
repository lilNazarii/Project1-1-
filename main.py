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


def show_menu(arr0, arr1, arr2):
    while True:
        print()
        print("1. Show languages")
        print("2. Show levels")
        print("3. Show Availability")
        print("4. X")
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
