import random

def area_generator():

    """Generates a random area question with height and width values between 1 and 100,
    calculates the correct answer, asks the user for their answer, and tells them if they're correct."""

    error = "Please enter an integer"

    width = random.randint(1, 100)
    height = random.randint(1, 100)

    area = width * height

    question = f"What is the area of a shape with a width of {width} and a height of {height}? "

    print(f"Answer: {area}")
    answer = int(input(f"{question}"))

    if answer == area:
        print(f"Correct! The answer was {area}")
    elif answer == ValueError:
        print(error)
    else:
        print(f"Incorrect! The answer was {area}")

area_generator()
