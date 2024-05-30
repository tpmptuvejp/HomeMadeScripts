import random

def generate_equation():
    var = random.choice(['x', 'y', 'z'])
    coeff = random.randint(1, 5)
    c = random.randint(1, 5)
    operator = random.choice(['+', '-', '*', '/'])
    rhs = random.randint(1, 5)

    if operator == '+':
        lhs = coeff * rhs + c
    elif operator == '-':
        lhs = coeff * rhs - c
    elif operator == '*':
        lhs = coeff * rhs * c
    elif operator == '/':
        # Ensure rhs and c are not equal to zero to avoid division by zero
        if rhs == 0:
            rhs = 1
        if c == 0:
            c = 1
        lhs = coeff * rhs / c

    equation = f"Solve for {var} in the following equation: {coeff}{var} {operator} {c} = {lhs}"
    return equation, rhs, var

def main():
    print("Welcome to Algebra Quiz.")
    print("Each equation will have a single variable: x, y, or z.")
    print("Solve for the variable in the following equations:")

    while True:
        equation, correct_answer, var = generate_equation()

        print(equation)

        user_answer = input(f"Your answer for {var}: ")

        try:
            # Evaluating the user's expression to check if it satisfies the equation
            if eval(user_answer) == correct_answer:
                print("Correct!")
            else:
                print("Incorrect. The correct answer is:", correct_answer)
        except (NameError, SyntaxError):
            print("Please enter a valid expression for the variable.")

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            break

if __name__ == "__main__":
    main()

#Developed in 2024 - SoloStudio, GPT3.5
#SoloStudio
