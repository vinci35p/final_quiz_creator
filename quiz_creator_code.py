# Text file to write the data
file = open("collected_data.txt", "a")

# Question number, and proceeding
def starting_num():
    try:
        with open("collected_data.txt", "r") as f:
            lines = f.readlines()
            return sum(1 for line in lines if line.startswith("Question: " or line[0].isdigit()))
    except FileNotFoundError:
        return 0

question_num = starting_num() + 1

# Input question
def question():
    user_question = str(input("\nEnter your preferred question: "))
    return user_question

# Input choices
def quest_choices():
    choices = {}
    for letter in ['A', 'B', 'C', 'D']:
        choices[letter] = input(f"Enter choice {letter} : ")

    return choices

# Input correct answer
def answer():
    user_ans = str(input("\nEnter the correct answer (A,B,C,D) from provided question: ")).upper()
    while user_ans not in ["A", "B", "C", "D"]:
        user_ans = input("Invalid input. Please enter A, B, C, or D: ").upper()
    return user_ans

# Main loop until exit
while True:
    print("Enter your question!")
    while True:
        choice = str(input("Enter '7' to exit. Enter '1' to continue: "))
        if choice in ['1', '7']:
            break
        else:
            print("Invalid input. Enter just number '1' to continue, and '7' to exit\n")

    if choice == '1':
        q = question()
        c = quest_choices()
        a = answer()

        file.write(f"{question_num}. Question: {q}\n")
        for letter in ['A', 'B', 'C', 'D']:
            file.write(f"{letter}. {c[letter]}\n")
        file.write(f"Correct Answer: {a}\n\n")

        question_num += 1

    elif choice == '7':
        print("Exiting, have a nice day!")
        file.close()
        break

    else:
        print("Invalid input, enter just '1' or '7'.\n")
