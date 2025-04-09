# Text file to write the data
file = open("collected_data.txt", "w")

# List of inputted values
questions_list = []
choices_list_a = []
choices_list_b = []
choices_list_c = []
choices_list_d = []
answers_list = []

# Input question
def question():
    user_question = str(input("\nEnter your preferred question: "))
    return user_question

# Input choices
def user_choice_a():
    choice_a = input("\nEnter choice A: ")

    return choice_a

def user_choice_b():
    choice_b = input("Enter choice B: ")

    return choice_b

def user_choice_c():
    choice_c = input("Enter choice C: ")

    return choice_c

def user_choice_d():
    choice_d = input("Enter choice D: ")

    return choice_d

# Input correct answer
def answer():
    user_ans = str(input("\nEnter the correct answer (A,B,C,D) from provided question: ")).upper()
    while user_ans not in ["A", "B", "C", "D"]:
        user_ans = input("Invalid input. Please enter A, B, C, or D: ").upper()
    return user_ans

# Loop until exit
while True:
    print("Welcome, this is your quiz creator!")
    choice = int(input("Enter '7' to exit. Enter '1' to continue: "))

    if choice == 1:
        q = question()
        ca = user_choice_a()
        cb = user_choice_b()
        cc = user_choice_c()
        cd = user_choice_d()
        a = answer()

        questions_list.append(f"Question: {q}")
        choices_list_a.append(f"\nA. {ca}")
        choices_list_b.append(f"\nB. {cb}")
        choices_list_c.append(f"\nC. {cc}")
        choices_list_d.append(f"\nD. {cd}")
        answers_list.append(f"\nCorrect Answer: {a}")

        file.write(str(questions_list))
        file.write(str(choices_list_a))
        file.write(str(choices_list_b))
        file.write(str(choices_list_c))
        file.write(str(choices_list_d))
        file.write(str(answers_list))

        file.close()

    elif choice == 7:
        print("Exiting, have a nice day!")
        break

    else:
        print("Invalid input, enter just '1' or '7'.\n")
