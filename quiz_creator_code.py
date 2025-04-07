# Input question
def question():
    user_question = str(input("Enter your preferred question: "))

# Input choices
def choices():
    user_choice_a = str(input("Enter choice a.: "))
    user_choice_b = str(input("Enter choice b.: "))
    user_choice_c = str(input("Enter choice c.: "))
    user_choice_d = str(input("Enter choice d.: "))

# Input correct answer
def answer():
    user_ans = str(input("Enter the correct answer letter from provided question: "))

# Loop until exit
while True:
    print("This is your quiz creator!")
    choice = int(input("Enter '7' to exit. Enter '1' to continue: "))

    if choice == 1:
        question()
        choices()
        answer()

    elif choice == 7:
        print("Exiting, have a nice day!")
        break

    else:
        print("Invalid input, enter just '1' or '7'.\n")
