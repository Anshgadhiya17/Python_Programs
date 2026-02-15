score = 0

questions = {
    "What is the capital of India? ": "Delhi",
    "2 + 2 = ? ": "4",
    "Python is a programming language? (yes/no): ": "yes"
}

for question, answer in questions.items():
    user_answer = input(question)
    if user_answer.lower() == answer.lower():
        score += 1

print("Your Score:", score, "/", len(questions))
