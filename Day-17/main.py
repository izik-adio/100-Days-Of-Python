from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for items in question_data:
    question_bank_data = Question(items["question"], items["correct_answer"])
    question_bank.append(question_bank_data)

quiz = QuizBrain(question_bank)

quiz.quiz_amount_choice()
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the Quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
