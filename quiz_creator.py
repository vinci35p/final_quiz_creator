from colorama import Fore
import sys
import time

# Text file to collect and write the data
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
    user_question = str(input(Fore.CYAN + "\nEnter your preferred question: "))

    return user_question

# Input choices
def quest_choices():
    choices = {}
    for letter in ['A', 'B', 'C', 'D']:
        choices[letter] = input(Fore.BLUE+ f"Enter choice {letter} : ")

    return choices

# Input correct answer
def answer():
    user_ans = str(input(Fore.LIGHTBLUE_EX + "\nEnter the correct answer (A,B,C,D) from provided question: ")).upper()
    while user_ans not in ["A", "B", "C", "D"]:
        user_ans = input(Fore.RED + "Invalid input. Please enter A, B, C, or D: ").upper()

    return user_ans

# Loading text after questions, choices and answers are inputted
def loading_animation():
    print(Fore.LIGHTRED_EX + "Saving your question", end='')
    for _ in range(3):
        sys.stdout.write(Fore.RED + ".")
        sys.stdout.flush()
        time.sleep(0.75)
    print(Fore.YELLOW + "\nSaved successfully! Check your text file to see your inputted values.")
    print()

# Main loop until exit
while True:
    print(Fore.LIGHTYELLOW_EX + "Enter your question!")
    while True:
        choice = str(input(Fore.YELLOW + "Enter '7' to exit. Enter '1' to continue: "))
        if choice in ['1', '7']:
            break

        else:
            print(Fore.RED + "Invalid input. Enter just number '1' to continue, and '7' to exit\n")

    if choice == '1':
        q = question()
        c = quest_choices()
        a = answer()

        loading_animation()

        file.write(f"{question_num}. Question: {q}\n")
        for letter in ['A', 'B', 'C', 'D']:
            file.write(f"{letter}. {c[letter]}\n")
        file.write(f"Correct Answer: {a}\n\n")

        question_num += 1

    elif choice == '7':
        print(Fore.MAGENTA + "Exiting, have a nice day!")
        file.close()
        break

    else:
        print(Fore.RED + "Invalid input, enter just '1' or '7'.\n")