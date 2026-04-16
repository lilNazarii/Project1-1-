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


def main():
    load_data()
    print(class_names)
    print(class_levels)
    print(class_quantity)


main()