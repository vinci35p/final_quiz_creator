# List of inputted values
questions_list = []
choices_list = []
answers_list = []

# Input question
def question():
    user_question = str(input("Enter your preferred question: "))
    return user_question

# Input choices
def choices():
    user_choice = {
        "A": input("Enter choice A: "),
        "B": input("Enter choice B: "),
        "C": input("Enter choice C: "),
        "D": input("Enter choice D: ")
    }
    return user_choice

# Input correct answer
def answer():
    user_ans = str(input("Enter the correct answer (A,B,C,D) from provided question: ")).upper()
    while user_ans not in ["A", "B", "C", "D"]:
        user_ans = input("Invalid input. Please enter A, B, C, or D: ").upper()
    return user_ans

# Loop until exit
while True:
    print("This is your quiz creator!")
    choice = int(input("Enter '7' to exit. Enter '1' to continue: "))

    if choice == 1:
        q = question()
        c = choices()
        a = answer()

        questions_list.append(a)
        choices_list.append(c)
        answers_list.append(a)

    elif choice == 7:
        print("Exiting, have a nice day!")
        break

    else:
        print("Invalid input, enter just '1' or '7'.\n")
