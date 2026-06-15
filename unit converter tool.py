while True:
    print("\n===== UNIT CONVERTER TOOL =====")
    print("1. Kilometers to Meters")
    print("2. Meters to Kilometers")
    print("3. Celsius to Fahrenheit")
    print("4. Kilograms to Grams")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        km = float(input("Enter kilometers: "))
        print("Meters =", km * 1000)

    elif choice == 2:
        m = float(input("Enter meters: "))
        print("Kilometers =", m / 1000)

    elif choice == 3:
        c = float(input("Enter Celsius: "))
        print("Fahrenheit =", (c * 9/5) + 32)

    elif choice == 4:
        kg = float(input("Enter kilograms: "))
        print("Grams =", kg * 1000)

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Try Again.")