import random

score = 0
num_problems = 5

print('Welcome to the Simple Multiplication Quiz!')
print(f'You will be given {num_problems} multiplication problems to solve.\n')

for i in range(1, num_problems + 1):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    print(f'Problem {i}: What is {num1} x {num2}?')

    user_answer = input('Your answer: ')

    while not user_answer.isdigit():
        print('Please enter a valid integer.')
        user_answer = input('Your answer: ')

    user_answer = int(user_answer)
    correct_answer = num1 * num2

    if user_answer == correct_answer:
        print('Correct!\n')
        score += 1
    else:
        print(f'Incorrect. The correct answer was {correct_answer}.\n')

if score == num_problems:
    print(f'You scored {score} out of {num_problems}. Excellent! 🏆')

elif score >= num_problems * 0.8:    # more than 80% of aswers are correct
    print(f'You scored {score} out of {num_problems}. Well done! 👍')

elif score >= num_problems * 0.5:
    print(f'You scored {score} out of {num_problems}. Good effort! 👌')

else:   # less than 50% of aswers are correct
    print(f'You scored {score} out of {num_problems}. Keep practicing...')
