import random

# functions

def instructions():

    """Prints instructions"""
    print("""
*** Instructions ***

- Input how many questions you want to answer in the quiz (press <enter> for infinite)
- Answer random area / perimeter questions 
- Input "xxx" to end the program

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

def num_check(question, num_type=None, low=0, exit_code="xxx"):

    """checks users enter an int / float that is more than a minimum (default minimum is zero)
    Allows an 'exit' code"""

    error = f"Please enter an integer that is more than {low}."

    while True:
        # Ask user question and return response if
        # exit code is entered
        response = input(question)
        if response == exit_code:
            return response

        # Check response is more than the minimum
        try:
            response = num_type(response)

            if response > low:
                return response
            else:
                print(error)

        # Show error if response is invalid
        except ValueError:
            print(error)

def question_generator():

    """Generates a random area or perimeter question with height and width values between 1 and 100,
    calculates the correct answer, asks the user for their answer, and tells them if they're correct."""

    # initialize variables
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
    elif selected_shape == "rectangle":
        perimeter = (width * 2) + (height * 2)
        area = width * height

        question = f"What is the {question_type} of a rectangle with a width of {width} and a height of {height}? "

    # if the shape is a triangle, the 3 sides are added together to make the perimeter,
    # and to find the area, the width is multiplied by the height, and then divided by 2
    else:
        perimeter = side_a + side_b + side_c
        area = (width * height) / 2

        if question_type == "perimeter":
            question = f"What is the perimeter of a triangle with sides of {side_a}, {side_b} and {side_c}? "
        else:
            question = f"What is the area of a triangle with a width of {width} and a height of {height}? "

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

            if question_type == "area" and selected_shape == "triangle":
                answer = num_check(question, num_type=float, exit_code="xxx")
            else:
                answer = num_check(question, num_type=int, exit_code="xxx")

            # tells the user what the answer was and if they were correct or not
            if answer == "xxx":
                return answer
            elif answer == correct_answer:
                print(f"Correct! The answer was {correct_answer}")
                return "Correct ✅"
            elif answer != correct_answer:
                print(f"Incorrect! The answer was {correct_answer}")
                return "Incorrect ❌"

    return "hello miss my code is not jank at all you can keep scrolling"


# Main routine starts here

# initialize variables
correct_answers = 0
incorrect_answers = 0
questions_answered = 0
mode = "regular"

quiz_history = []

# Instructions

want_instructions = string_checker("Do you want to see the instructions? ")

# checks user entered yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# ask user for number of questions (or if they want infinite mode)
num_questions = num_check("How many questions do you want to answer? (<enter> for infinite): ",
                          low=0, exit_code="", num_type=int)

if num_questions == "":
    mode = "infinite"
    num_questions = 5

# Question loop starts here
while questions_answered < num_questions:

    # prints round number heading
    if mode == "infinite":
        question_heading = f"\n=== Question {questions_answered + 1} (Infinite Mode) ===\n"
    else:
        question_heading = f"\n=== Question {questions_answered + 1} of {num_questions} ===\n"

    print(question_heading)

    # generates random area / perimeter question, checks if user got it correct
    user_answer = question_generator()

    # if user enters exit code, end quiz
    if user_answer == "xxx":
        break
    # record whether the user got the answer correct or not
    elif user_answer == "Correct ✅":
        correct_answers += 1
    elif user_answer == "Incorrect ❌":
        incorrect_answers += 1

    questions_answered += 1

    if mode == "infinite":
        num_questions += 1

    # add results of question to quiz history
    question_feedback = f"Question {questions_answered}: {user_answer}"
    quiz_history.append(question_feedback)

# Quiz ends here

# if user has answered at least 1 question, ask if they want to display their results (history)
if questions_answered > 0:

    print("\n*** Quiz End! ***")

    # calculates what percent of the questions the user answered correctly
    question_worth = 100 / questions_answered
    percent_correct = question_worth * correct_answers

    # print quiz history and percentage of correct answers
    print(f"\nCorrect Answers: {percent_correct:.1f}%")

    see_history = string_checker("Do you want to see your quiz history? ")
    if see_history == "yes":
        print("\n*** Quiz History ***\n")
        for item in quiz_history:
            print(item)

else:
    # if user quit without answering any questions, shame them for being the chicken they are
    print("\n🐔🐔🐔 CHICKEN! BAKAW BAKAW!! *various other chicken noises because you're a chicken* "
          "(you chickened out without answering any questions) 🐔🐔🐔")
