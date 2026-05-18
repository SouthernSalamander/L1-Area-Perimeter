import random

def perimeter_generator():

    """Generates a random perimeter question with height and width values between 1 and 100,
    calculates the correct answer, asks the user for their answer, and tells them if they're correct."""

    error = "Please enter an integer"
    answer = ""
    shapes = ["square", "rectangle", "triangle"]
    width = random.randint(1, 100)
    height = random.randint(1, 100)

    selected_shape = random.choice(shapes)

    # calculates perimeter depending on what shape has been selected
    if selected_shape == "rectangle":
        perimeter = (width * 2) + (height * 2)
    elif selected_shape == "square":
        perimeter = width * 4
    else:
        perimeter =

    # asks user question based on what shape has been selected
    if selected_shape == "square":
        question = f"What is the perimeter of a square with a width of {width} and a height of {width}? "
    elif:
        question = f"What is the perimeter of a rectangle with a width of {width} and a height of {height}? "
    elif:
        question = f"What is the perimeter of a triangle"

    print(f"Answer: {perimeter}")

    # asks user for answer to question and tells them if they're correct
    while answer == "":
        try:
            answer = int(input(f"{question}"))

            if answer == perimeter:
                print(f"Correct! The answer was {perimeter}")
            else:
                print(f"Incorrect! The answer was {perimeter}")
        except ValueError:
            print(error)

perimeter_generator()
