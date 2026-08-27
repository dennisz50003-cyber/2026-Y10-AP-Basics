def num_check(question):

    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            response = float(input(question))

            if response >  0:
                return response
            else:
                print(error)

        except ValueError:

            print(error)

#Main Routine starts here:

keep_going = ""
while keep_going == "":
    # Get width and height
    width = float(input("Width: "))
    height = float(input("Height: "))
    cost = float(input("Cost per meter: "))

    # Calculate perimeter and price for the fence
    perimeter = 2 * (width + height)
    price = perimeter * cost

    #Display output
    print()
    print(f"perimeter: {perimeter} units")
    print(f"Price: ${price:.2f}")

    # Ask user if they want to keep going
    keep_going = input("Press enter to keeping going or any key to quit. ")
    print()

print("Thank you for using the Fence Cost Per Meter Calculator ")