class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


questions = [
    Question("What is the capital of France?\n(a) Paris\n(b) Madrid\n(c) Rome\n", "a"),
    Question("Who wrote 'To Kill a Mockingbird'?\n(a) Harper Lee\n(b) J.K. Rowling\n(c) Stephen King\n", "a"),
    Question("What is the largest planet in our solar system?\n(a) Earth\n(b) Jupiter\n(c) Saturn\n", "b"),
    Question("What is the powerhouse of the cell?\n(a) Nucleus\n(b) Mitochondria\n(c) Ribosome\n", "b"),
    Question("What is the chemical symbol for water?\n(a) Wo\n(b) Wa\n(c) H2O\n", "c")
]


def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", question.answer.upper())

    total_questions = len(questions)
    pass_mark = total_questions * 0.7
    print("\nQuiz Completed!")
    print("You scored {} out of {}.".format(score, total_questions))
    if score >= pass_mark:
        print("Congratulations! You passed.")
    else:
        print("Sorry! You failed.")


run_quiz(questions)
