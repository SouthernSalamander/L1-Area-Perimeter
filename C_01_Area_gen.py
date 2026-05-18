import random

def area_generator():

    """Generates a random area question with height and width values between 1 and 100,
    calculates the correct answer, asks the user for their answer, and tells them if they're correct."""

    error = "Please enter an integer"
    answer = ""
    shapes = ["square", "rectangle", "triangle"]
    width = random.randint(1, 100)
    height = random.randint(1, 100)

    selected_shape = random.choice(shapes)

    # calculates area depending on what shape has been selected
    if selected_shape == "rectangle":
        area = width * height
    elif selected_shape == "square":
        area = width * 2
    else:
        area = width * height / 2

    # asks user question based on what shape has been selected
    if selected_shape == "square":
        question = f"What is the area of a square with a width of {width} and a height of {width}? "
    else:
        question = f"What is the area of a {selected_shape} with a width of {width} and a height of {height}? "

    print(f"Answer: {area}")

    # asks user for answer to question and tells them if they're correct
    while answer == "":
        try:
            answer = int(input(f"{question}"))

            if answer == area:
                print(f"Correct! The answer was {area}")
            else:
                print(f"Incorrect! The answer was {area}")
        except ValueError:
            print(error)

area_generator()
