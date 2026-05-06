
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

    if mode == "infinite":
        question_heading = f"\nQuestion {questions_answered + 1} (Infinite Mode)"
    else:
        question_heading = f"\nQuestion {questions_answered + 1} of {num_questions}"

    print(question_heading)