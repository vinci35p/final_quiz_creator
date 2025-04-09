# Text file to write the data
file = open("collected_data.txt", "a")

# Input question
def question():
    user_question = str(input("\nEnter your preferred question: "))
    return user_question

# Input choices
def user_choice_a():
    return input("\nEnter choice A: ")

def user_choice_b():
    return input("Enter choice B: ")

def user_choice_c():
    return input("Enter choice C: ")

def user_choice_d():
    return input("Enter choice D: ")

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

        file.write(f"Question: {q}\n")
        file.write(f"A. {ca}\n")
        file.write(f"B. {cb}\n")
        file.write(f"C. {cc}\n")
        file.write(f"D. {cd}\n")
        file.write(f"Correct Answer: {a}\n\n")

        file.close()

    elif choice == 7:
        print("Exiting, have a nice day!")
        break

    else:
        print("Invalid input, enter just '1' or '7'.\n")
