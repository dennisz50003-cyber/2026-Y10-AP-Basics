# Ask user for width and loop until they
# Enter a number that is more than zero
def int_check(question, low):

    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            response = int(input(question))

            if response >=  low:
                return response
            else:
                print(error)

        except ValueError:

            print(error)


# calculates how many bits are needed to represent an integer
def integer_calc():
    # Ask the user to enter an integer (more than / equal to 0)
    integer = int_check("Integer: ", 0)

    # convert the integer to binary and work out the number of bits needed
    raw_binary = bin(integer)

    # remove the leading '0b' from the raw binary conversion
    binary = raw_binary[2:]
    num_bits = len(binary)

    # Set up answer and return it
    answer = f"{integer} in binary is {binary}.  We ned {num_bits} to represent it."

    return answer


# Main routine goes here
integer_ans = integer_calc()
print(integer_ans)