import random

# functions

def instructions():

    """Prints instructions"""
    print("""
*** Instructions ***

-Instructions go here
    """)

def string_checker(question, valid_ans=("yes", "no")):

    """Check that users enter a valid word / first
    letter of the word based on a list of options. Defaults to yes / no"""

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for var_item in valid_ans:
            # check if the user response is a word in the list
            if var_item == user_response:
                return var_item

            # check if the user response is the same as
            # the first letter of an item from the list
            elif user_response == var_item[0]:
                return var_item

        # print error if user does not enter something that is valid
        print(error)
        print()

def int_check(question, low=None, high=None, exit_code=None):

   # if any integer is allowed...
   if low is None and high is None:
       error = "Please enter an integer"

   # if the number needs to be more than an
   # integer (ie: rounds / 'high number')
   elif low is not None and high is None:
        error = (f"Please enter an integer that is "
             f"more than / equal to {low}")

    # if the number needs to be between low & high
   else:
       error = (f"Please enter an integer that"
                f" is between {low} and {high} (inclusive)")

   while True:
       response = input(question).lower()

       # check for infinite mode / exit code
       if response == exit_code:
           return response

       try:
           response = int(response)

           # Check the integer is not too low...
           if low is not None and response < low:
               print(error)

           # check response is more than the low number
           elif high is not None and response > high:
               print(error)

           # if response is valid, return it
           else:
               return response

       except ValueError:
           print(error)

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

    # if the shape is a square, the width and height are the same value
    if selected_shape == "square":
        perimeter = width * 4
        area = width * width

        question = f"What is the {question_type} of a square with a width of {width} and a height of {width}? "

    # if the shape is a rectangle, the width and height are two separate values
    elif question_type == "rectangle":
        perimeter = (width * 2) + (height * 2)
        area = width * height

        question = f"What is the {question_type} of a rectangle with a width of {width} and a height of {height}? "

    # if the shape is a triangle, the 3 sides are added together to make the perimeter,
    # and to find the area, the width is multiplied by the height, and then divided by 2
    else:
        perimeter = side_a + side_b + side_c
        area = (width * height) / 2

        if question_type == "perimeter":
            question = f"What is the {question_type} of a triangle with sides of {side_a}, {side_b} and {side_c}? "
        else:
            question = f"What is the {question_type} of a triangle with a width of {width} and a height of {height}? "

    if question_type == "perimeter":
        print(f"Answer: {perimeter}")
    else:
        print(f"Answer: {area}")

    # sets the correct answer to either the perimeter or area depending on the question
    if question_type == "perimeter":
        correct_answer = perimeter
    else:
        correct_answer = area

    # asks user for answer to question and checks to see if they're correct
    while answer == "":
        try:
            answer = int(input(f"{question}"))

            # tells the user what the answer was and if they were correct or not
            if answer == correct_answer:
                print(f"Correct! The answer was {correct_answer}")
            else:
                print(f"Incorrect! The answer was {correct_answer}")

        except ValueError:
            print(error)

# Main routine starts here

# initialize variables
mode = "regular"
end_game = "no"
questions_answered = 0

# Instructions

want_instructions = string_checker("Do you want to see the instructions? ")

# checks user entered yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# ask user for number of questions (or if they want infinite mode)
num_questions = int_check("How many questions do you want to answer? (<enter> for infinite): ",
                          low=1, exit_code="")

if num_questions == "":
    mode = "infinite"
    num_questions = 5

# Question loop starts here
while questions_answered < num_questions:

    # prints round number heading
    if mode == "infinite":
        question_heading = f"\n=== Question {questions_answered + 1} (Infinite Mode) === \n"
    else:
        question_heading = f"\nQuestion {questions_answered + 1} of {num_questions}"

    print(question_heading)

    question_generator()

    questions_answered += 1

