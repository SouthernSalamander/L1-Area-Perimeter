import random
import math

def question_generator():

    """Generates a random area or perimeter question with height and width values between 1 and 100,
    calculates the correct answer, asks the user for their answer, and tells them if they're correct."""

    # initialize variables
    error = "Please enter an integer"
    answer = ""
    shapes = ["square", "rectangle", "triangle"]
    type_list = ["area", "perimeter"]
    side_a = random.randint(1, 100)
    side_b = random.randint(1, 100)
    side_c = random.randint(1, 100)
    width = random.randint(1, 100)
    height = random.randint(1, 100)

    # chooses random shape (square, triangle, rectangle)
    # and random type of question (area or perimeter)
    question_type = random.choice(type_list)
    selected_shape = random.choice(shapes)

    # calculates area and perimeter depending on the shape and generates a question
    if selected_shape == "square":
        perimeter = width * 4
        area = width * width

        question = f"What is the {question_type} of a square with a width of {width} and a height of {width}? "

    elif question_type == "rectangle":
        perimeter = (width * 2) + (height * 2)
        area = width * height

        question = f"What is the {question_type} of a rectangle with a width of {width} and a height of {height}? "

    else:
        perimeter = side_a + side_b + side_c
        area = width * height / 2

        if question_type == "perimeter":
            question = f"What is the {question_type} of a triangle with sides of {side_a}, {side_b} and {side_c}"
        else:
            question = f"What is the {question_type} of a triangle with a width of {width} and a height of {height}? "

    if question_type == "perimeter":
        print(f"Answer: {perimeter}")
    else:
        print(f"Answer: {area}")

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

question_generator()
