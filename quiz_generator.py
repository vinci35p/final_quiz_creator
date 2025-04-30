from colorama import Fore
import sys
import time
import random

# Text file to collect and write the data
file = open("quiz_txt.txt", "a")

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

# Read quiz file and randomly select question with choices
def read_txt_file(quiz_txt):
    with open("quiz_txt.txt", "r") as f:
        file_txt = f.read().strip()

    solo_quests = file_txt.split("\n\n")
    question_list = []

    for solo_quest in solo_quests:
        lines = solo_quest.strip().split("\n")
        if len(lines) >= 6:
            quest_part = lines[0]
            choices_part = lines[1:5]
            answer_part = lines[5]
            answer_key = answer_part.split(":")[-1].strip()
            question_list.append({
                "question" : quest_part,
                "choices" : choices_part,
                "answer" : answer_key
            })

    return question_list

# Print the questions randomly then let the user answer every rambled question
def execute_quiz(question_list):
    score = 0
    total = len(question_list)
    quiz = random.sample(question_list, total)

    for num, question_list in enumerate(quiz, 1):
        print(f"\n{question_list['question']}")
        for choice in question_list['choices']:
            print(choice)

        while True:
            user_ans = input("Enter your answer (A, B, C, or D): ").strip().upper()
            if user_ans in ['A', 'B', 'C', 'D']:
                break
            else:
                print("Invalid input. Please enter a viable answer (A, B, C, or D).")

        if user_ans == question_list["answer"]:
            print("You got it!")
            score += 1

        else:
            print("Didn't got it, keep up!")

    print(f"\nYou got {score} out of {total}.")


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
        questions = question()
        choices = quest_choices()
        answers = answer()

        loading_animation()

        file.write(f"{question_num}. Question: {questions}\n")
        for letter in ['A', 'B', 'C', 'D']:
            file.write(f"{letter}. {choices[letter]}\n")
        file.write(f"Correct Answer: {answers}\n\n")

        question_num += 1

    elif choice == '7':
        print(Fore.MAGENTA + "Exiting, have a nice day!\n")
        file.close()
        break

# ---- MAIN QUIZ ----
file = 'quiz_txt.txt'

quiz_questions = read_txt_file(file)
execute_quiz(quiz_questions)