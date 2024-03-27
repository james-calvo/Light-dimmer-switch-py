def adjust_light(level):
    if level == 0:
        print("Turning off the light.")
    elif level == 1:
        print("Setting light to Low (25%).")
    elif level == 2:
        print("Setting light to Medium (50%).")
    elif level == 3:
        print("Setting light to High (75%).")
    elif level == 4:
        print("Setting light to Maximum (100%).")


def get_input():
    while True:
        try:
            user_input = int(input("Enter the desired light level (0 for Off, 1-4 for Low to Maximum): "))
            if user_input < 0 or user_input > 4:
                raise ValueError
            return user_input
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 4.")


def main():
    print("Welcome to the light dimmer switch!")
    while True:
        level = get_input()
        adjust_light(level)
        if level == 0:
            break  # Exit loop if user chooses to turn off the light


if __name__ == "__main__":
    main()
