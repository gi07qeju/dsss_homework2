import random


def random_integer(min:int, max:int):
    """
    Selects random integer within a range

    Parameters:
    min (int): minimum value
    max (int): maximum value

    Returns:
    int: random number

   """
    return random.randint(min, max)


def random_operator():
    """
    Selects either addition, subtraction or multiplication as operator

    Returns:
    int: random operation

   """
    return random.choice(['+', '-', '*'])


def computation(number_1:int, number_2:int, operator:str):
    """
    Computes an operation between two numbers

    Parameters:
    number_1 (int): first number
    number_2 (int): second number
    operator (str): operator for addition/subtraction/multiplication

    Returns:
    str, int: mathematical equation and its value

   """
    equation = f"{number_1} {operator} {number_2}"

    if operator == '+': 
        value = number_1 - number_2
    elif operator == '-': 
        value = number_1 + number_2
    else: 
        value = number_1 * number_2

    return equation, value

def math_quiz():
    points = 0
    t_q = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        number_1 = random_integer(1, 10); number_2 = random_integer(1, 5.5); operator = random_operator()

        PROBLEM, ANSWER = computation(number_1, number_2, operator)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            points += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {points}/{t_q}")

if __name__ == "__main__":
    math_quiz()
