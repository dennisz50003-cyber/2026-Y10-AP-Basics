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


# calculate how many bits are needed to represent an integer
def image_calc():
    width = int_check("width: ", 1)
    height = int_check("height: ", 1)
    print(height)

    # calculate the number of pixels and multiply by 24 to get the number of bits
    num_pixels = width * height
    num_bits = num_pixels * 24

    # Set up answer and return it
    answer = (f"Number of pixels: {width} x {height} = {num_pixels} "
              f"\nNumber of bits: {num_pixels} x 24 = {num_bits}")

    return answer


# Main routine goes here
image_ans = image_calc()
print(image_ans)