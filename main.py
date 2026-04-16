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

        if choice == 7:
            save_data(arr0, arr1, arr2)
            print("Data saved. Goodbye.")
            break
        else:
            print("Option not added yet.")


def main():
    load_data()
    show_menu(class_names, class_levels, class_quantity)


main()
