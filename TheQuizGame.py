quiz_questions = [
    "how many strings does a guitar have?",
    "What is the capital of the U.S.A.'?",
    "What is the largest planet in our solar system?",
    "What is the square root of 64?"
]

quiz_answers = [
    "6",
    "Washington D.C.",
    "Jupiter",
    "8"
]


def quiz_game(questions, answers):
    score = 0
    total_questions = len(questions)

    for i in range(total_questions):
        print(f"Question {i + 1}: {questions[i]}")
        user_answer = input("Your answer: ").strip().lower()

        if user_answer == answers[i].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answers[i]}\n")

    return score



user_score = quiz_game(quiz_questions, quiz_answers)

print(f"Your score: {user_score}/{len(quiz_questions)}")
if user_score == len(quiz_questions):
    print("Congratulations! You got all the answers correct.")
else:
    print("Keep practicing! You can do better next time.")

    
