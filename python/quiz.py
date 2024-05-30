import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    return num1, num2

def main():
    score = 0
    for _ in range(5):
        num1, num2 = generate_question()
        answer = int(input(f"What is the sum of {num1} + {num2}? "))
        if answer == num1 + num2:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"You scored {score} out of 5.")

if __name__ == "__main__":
    main()
    
#Developed in 2024 - SoloStudio
#SoloStudio
